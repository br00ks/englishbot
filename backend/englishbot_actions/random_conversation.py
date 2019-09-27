from typing import Text, List
import random as rand
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
import englishbot_actions


class EndRandomConversation(Action):
    """ Action to end conversation about a random topic """
    def name(self):
        return 'action_end_random_conversation'

    def run(self, dispatcher, tracker, domain):
        return [SlotSet('chat_topic', None)]


class StartRandomConversation(Action):
    """ Action to start conversation about a random topic """
    def name(self):
        return 'action_start_random_conversation'

    def run(self, dispatcher, tracker, domain):
        topics = self.conversation_topics()
        max_len = len(topics)
        random_topic = topics[rand.randint(0, max_len - 1)]
        dispatcher.utter_message("Let's get to know each other a bit better 😉")

        # intended to have more topics to talk about, but stories have to be written first
        if str(random_topic) == "studying":
            dispatcher.utter_template("utter_user.studying", tracker)
            return [SlotSet("chat_topic", str(random_topic))]

    @staticmethod
    def conversation_topics() -> List[Text]:
        # prototype can only talk about studying currently
        return [
            "studying",
        ]
