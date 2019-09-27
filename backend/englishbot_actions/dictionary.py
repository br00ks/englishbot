from typing import Any, Text, List, Dict
import json
import string
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction
from rasa_sdk.forms import FormAction
from englishbot_actions import *


class ActionDictionaryMeaning(Action):
    """ Action that calls Dictionary-class to retrieve the meaning of a word """

    def name(self) -> Text:
        return "action_dictionary_meaning"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        search_term = tracker.get_slot("word")
        results = DictionaryCall.get_meaning_for_word(search_term)

        if results:
            # if term consists of multiple words and no definition is found for compound word
            # send definitions of individual words
            if len(results) > 1:
                dispatcher.utter_message("I couldn't find a definition for the word " + str(
                    search_term) + ", but here's the definition for the individual words.")
                for result in results:
                    result_array = [result]
                    dispatcher.utter_message(json.dumps(result_array))
            else:
                dispatcher.utter_message("That's what I've found: ")
                dispatcher.utter_message(json.dumps(results))
        else:
            dispatcher.utter_message("I am sorry, I don't know the word " + str(search_term))

        return [SlotSet("word", None)]


class DictionaryForm(FormAction):
    """ FormAction used by ActionDictionary in order to ask user for the word """

    def name(self):
        return "dictionary_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["word"]

    def slot_mappings(self):
        # return either word entity if found or whole user input
        return {"word": [self.from_entity(entity="word"), self.from_text()]}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        return [FollowupAction(name='action_dictionary_meaning')]
