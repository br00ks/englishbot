import logging
import uuid
from typing import Optional, Text, Any, List, Dict, Iterable
from sanic import Blueprint, response
from sanic.request import Request
from rasa.core.channels.channel import InputChannel, UserMessage, OutputChannel
from socketio import AsyncServer
from apis.languagetool_api import LanguageTool
from apis.nlu_api import NLUApi

logger = logging.getLogger(__name__)


class RasaAppBlueprint(Blueprint):
    """
    Rasa Socket.io channel for socket connection with client
    Create sanic blueprint to attach to sanic server
    """
    def __init__(self, sio, socketio_path, *args, **kwargs):
        self.sio = sio
        self.socketio_path = socketio_path
        super(RasaAppBlueprint, self).__init__(*args, **kwargs)

    def register(self, app, options):
        self.sio.attach(app, self.socketio_path)
        super(RasaAppBlueprint, self).register(app, options)


class RasaAppOutput(OutputChannel):
    """
    Rasa socket output channel
    """
    @classmethod
    def name(cls):
        return "rasa_app"

    def __init__(self, sio, sid, bot_message_evt, language_errors):
        self.sio = sio
        self.sid = sid
        # socket.io events
        self.bot_message_evt = bot_message_evt
        # list of found language errors
        self.language_errors = language_errors

    async def _send_message(self, socket_id: Text, response: Any) -> None:
        """Sends a message to the recipient using the bot event."""
        await self.sio.emit(self.bot_message_evt, response, room=socket_id)

    async def send_text_message(
            self, recipient_id: Text, text: Text, **kwargs: Any
    ) -> None:
        """Send a message through this channel."""
        await self._send_message(self.sid, {"text": text})

    async def send_language_errors_message(
            self, recipient_id: Text, text: Text, **kwargs: Any
    ) -> None:
        """Send a list of errors detected by LanguageTool."""
        await self._send_message(self.sid, {"text": text})

    async def send_image_url(
            self, recipient_id: Text, image: Text, **kwargs: Any
    ) -> None:
        """Sends an image to the output"""

        message = {"attachment": {"type": "image", "payload": {"src": image}}}
        await self._send_message(self.sid, message)

    async def send_text_with_buttons(
            self,
            recipient_id: Text,
            text: Text,
            buttons: List[Dict[Text, Any]],
            **kwargs: Any
    ) -> None:
        """Sends buttons to the output."""

        message = {"text": text, "quick_replies": []}

        for button in buttons:
            message["quick_replies"].append(
                {
                    "content_type": "text",
                    "title": button["title"],
                    "payload": button["payload"],
                }
            )

        await self._send_message(self.sid, message)

    async def send_elements(
            self, recipient_id: Text, elements: Iterable[Dict[Text, Any]], **kwargs: Any
    ) -> None:
        """Sends elements to the output."""

        for element in elements:
            message = {
                "attachment": {
                    "type": "template",
                    "payload": {"template_type": "generic", "elements": element},
                }
            }

            await self._send_message(self.sid, message)

    async def send_custom_json(
            self, recipient_id: Text, json_message: Dict[Text, Any], **kwargs: Any
    ) -> None:
        """Sends custom json to the output"""

        json_message.setdefault("room", self.sid)

        await self.sio.emit(self.bot_message_evt, **json_message)


class RasaAppInput(InputChannel):
    """
    Rasa socket.io input channel
    """

    @classmethod
    def name(cls):
        return "rasa_app"

    @classmethod
    def from_credentials(cls, credentials):
        credentials = credentials or {}
        return cls(
            credentials.get("user_message_evt", "user_uttered"),
            credentials.get("bot_message_evt", "bot_uttered"),
            credentials.get("bot_found_errors_evt", "bot_error_message"),
            credentials.get("namespace"),
            credentials.get("session_persistence", False),
            credentials.get("socketio_path", "/socket.io"),
            credentials.get("languagetool_url", "localhost"),
            credentials.get("languagetool_port", "8082"),
        )

    def __init__(
            self,
            user_message_evt: Text = "user_uttered",
            bot_message_evt: Text = "bot_uttered",
            bot_found_errors_evt: Text = 'bot_error_message',
            namespace: Optional[Text] = None,
            session_persistence: bool = False,
            socketio_path: Optional[Text] = "/socket.io",
            languagetool_url: Text = "localhost",
            languagetool_port: int = 8082,
            nlu_url: Text = "localhost",
            nlu_port: int = 5045,
    ):
        self.bot_message_evt = bot_message_evt
        self.session_persistence = session_persistence
        self.user_message_evt = user_message_evt
        self.bot_found_errors_evt = bot_found_errors_evt
        self.namespace = namespace
        self.socketio_path = socketio_path
        self.languagetool_api = LanguageTool(languagetool_url, languagetool_port)
        self.nlu_api = NLUApi(nlu_url, nlu_port)

    def blueprint(self, on_new_message):
        sio = AsyncServer(async_mode="sanic")
        socketio_webhook = RasaAppBlueprint(
            sio, self.socketio_path, "socketio_webhook", __name__
        )

        @socketio_webhook.route("/", methods=["GET"])
        async def health(request: Request):
            return response.json({"status": "ok"})

        @sio.on("connect", namespace=self.namespace)
        async def connect(sid, environ):
            logger.debug("User {} connected to socketIO endpoint.".format(sid))

        @sio.on("disconnect", namespace=self.namespace)
        async def disconnect(sid):
            logger.debug("User {} disconnected from socketIO endpoint.".format(sid))

        @sio.on("session_request", namespace=self.namespace)
        async def session_request(sid, data):
            if data is None:
                data = {}
            if "session_id" not in data or data["session_id"] is None:
                data["session_id"] = uuid.uuid4().hex
            await sio.emit("session_confirm", data["session_id"], room=sid)
            logger.debug("User {} connected to socketIO endpoint.".format(sid))

        @sio.on("start_conversation", namespace=self.namespace)
        async def start_conversation(sid, data):
            if self.session_persistence:
                if not data.get("session_id"):
                    logger.warning(
                        "A message without a valid sender_id "
                        "was received. This message will be "
                        "ignored. Make sure to set a proper "
                        "session id using the "
                        "`session_request` socketIO event."
                    )
                    return
                sender_id = data["session_id"]
            else:
                sender_id = sid

            output_channel = RasaAppOutput(sio, sid, self.bot_message_evt, [])
            message = UserMessage(
                "Hello!", output_channel, sender_id, input_channel=self.name()
            )
            await on_new_message(message)

        @sio.on(self.user_message_evt, namespace=self.namespace)
        async def handle_message(sid, data):

            if self.session_persistence:
                if not data.get("session_id"):
                    logger.warning(
                        "A message without a valid sender_id "
                        "was received. This message will be "
                        "ignored. Make sure to set a proper "
                        "session id using the "
                        "`session_request` socketIO event."
                    )
                    return
                sender_id = data["session_id"]
            else:
                sender_id = sid

            language_errors = []
            # lt_response = None
            try:
                user_message = data["message"]
                # Extract entities from the message
                response_nlu = self.nlu_api.parse(user_message)
                logger.info("NLU Response " + str(response_nlu))
                logging.debug("response: " + str(response_nlu))
                response_entities = response_nlu["entities"]
                logging.debug("Entities NLU: " + str(response_entities))

                # Check if text contains error
                languagetool_response = self.languagetool_api.check_message(user_message)
                logger.info("LanguageTool Response. " + str(languagetool_response))
                languagetool_response.ignore_entity_errors(response_entities, ["name"])
                language_errors = languagetool_response.get_languagetool_errors()
                logging.debug("Errors found by LanguageTool: " + str(language_errors))
            except (TypeError, ValueError):
                logger.debug("Error occurred using LanguageTool")

            if len(language_errors) > 0:
                # Send found errors to the client
                logger.debug("Errors: " + str(language_errors))
                output_channel = RasaAppOutput(sio, sid, self.bot_found_errors_evt, language_errors)
                await output_channel.send_language_errors_message(sender_id, language_errors)

            output_channel = RasaAppOutput(sio, sid, self.bot_message_evt, language_errors)
            message = UserMessage(
                data["message"], output_channel, sender_id, input_channel=self.name()
            )
            await on_new_message(message)

        return socketio_webhook
