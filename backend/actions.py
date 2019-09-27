from datetime import datetime
from rasa_sdk.events import UserUtteranceReverted
from englishbot_actions import *


class BotQuestions(Action):
    """ Action that sets slot word to None when bot asks user to ask questions """

    def name(self):
        return 'action_bot_questions'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_bot.questions", tracker)
        return [SlotSet("word", None)]


class TellTime(Action):
    """ Action to tell the current time """

    def name(self):
        return 'action_tell_time'

    def run(self, dispatcher, tracker, domain):
        time = datetime.now().time()
        time = time.strftime("%I:%M %p")
        dispatcher.utter_message("It's ⌚ " + str(time))
        return [UserUtteranceReverted()]


class ReactToDegreeProgram(Action):
    """ Action to react to degree program """

    def name(self):
        return 'action_react_to_degree_program'

    def run(self, dispatcher, tracker, domain):
        # degree_program = tracker.get_slot('user_degree_program')
        # if str(degree_program) is not str(None):
        #     dispatcher.utter_template("utter_user.interesting_degree_program", tracker)
        # else:
        dispatcher.utter_template("utter_user.interesting", tracker)
        return []


class ExplainHowTo(Action):
    """ Action to give examples if user need help to execute a function """

    def name(self):
        return 'action_how_to'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("To get the meaning of a word ask like this: \n"
                                 "💬 What does the word ____ mean? \n\n"
                                 "To learn new vocabulary, ask like this: \n"
                                 "💬 Teach me some vocabulary \n\n"
                                 "And if you want to chat, just type \n💬 Let's chat")
        return []


class UserDegreeProgram(Action):
    """ Action that sets extracted degree program from user input """

    def name(self):
        return 'action_user_degree_program'

    def run(self, dispatcher, tracker, domain):
        degree_program = next(tracker.get_latest_entity_values("degree_program"), None)
        degree_program = (str(degree_program)).capitalize()
        print("degree_program: " + str(degree_program))
        return [SlotSet('user_degree_program', degree_program)]


class GreetUser(Action):
    """ Action to greet user depending on user_name slot """

    def name(self):
        return 'action_greet_user'

    def run(self, dispatcher, tracker, domain):
        user_name_slot = tracker.get_slot('current_user_name')

        # if user_name slot has already been set, Bot knows user
        # and should greet by name and ask how user is
        if user_name_slot is not None:
            dispatcher.utter_template("utter_greet.hello.name", tracker)
            dispatcher.utter_template("utter_greet.ask_how_are_you", tracker)
            return [UserUtteranceReverted()]

        # else ask for name
        else:
            dispatcher.utter_template("utter_greet.hello", tracker)
            dispatcher.utter_template("utter_ask_for_name", tracker)
            return


class SaveUserLocation(Action):
    """ Action to set current_location slot to extracted location """

    def name(self):
        return 'action_save_user_location'

    def run(self, dispatcher, tracker, domain):
        loc = next(tracker.get_latest_entity_values("location"), None)
        loc = (str(loc)).capitalize()
        print("User location: " + str(loc))
        return [SlotSet('current_location', loc)]


class ActionJoke(Action):
    """ Action that retrieves a random joke from joke API """

    def name(self):
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # get random joke from joke api
        request = json.loads(
            requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'application/json'}).text
        )
        joke = request['joke']
        dispatcher.utter_template("utter_joke", tracker)
        dispatcher.utter_message("Here's one: " + str(joke))
        return []