import string
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction


class IntroductionForm(FormAction):
    """FormAction to ask for the user's name and location """

    def name(self):
        return "introduction_form"

    @staticmethod
    def required_slots(tracker):
        return ["name", "location"]

    def slot_mappings(self):
        return {
            "name": [self.from_entity(entity="name"), self.from_text()],
            "location": [self.from_entity(entity="location"), self.from_text()],
        }

    def validate_name(self, value, dispatcher, tracker, domain):
        """Check to see if an user name entity was actually picked up."""

        if any(tracker.get_latest_entity_values("name")):
            # entity was picked up, validate slot
            usr = string.capwords(str(value))
            last_intent = tracker.latest_message['intent'].get('name')

            dispatcher.utter_message("Nice to meet you " + usr)

            if last_intent == 'user.name+bot.name':
                dispatcher.utter_template("utter_bot.name", tracker)
            if last_intent == 'bot.name':
                dispatcher.utter_template("utter_bot.name", tracker)

            dispatcher.utter_template("utter_ask_user_location", tracker)
            return {"current_user_name": usr, "name" : usr}
        else:
            # no entity was picked up, we want to ask again
            dispatcher.utter_template("utter_ask_current_user_name", tracker)
            return {"current_user_name": None, "name": None}

    def validate_location(self, value, dispatcher, tracker, domain):
        """Check to see if an location entity was actually picked up by duckling."""

        if any(tracker.get_latest_entity_values("location")):
            last_intent = tracker.latest_message['intent'].get('name')

            if last_intent == 'user.location+bot.location':
                dispatcher.utter_template("utter_bot.location", tracker)
            if last_intent == 'bot.name':
                dispatcher.utter_template("utter_bot.name", tracker)

            loc = string.capwords(str(value))
            return {"current_location": loc, "location" : loc}
        else:
            # no entity was picked up, we want to ask again
            dispatcher.utter_template("utter_ask_current_location", tracker)
            return {"current_location": None, "location" : None}


    def submit(self, dispatcher, tracker, domain):
        return [SlotSet("word", None)]