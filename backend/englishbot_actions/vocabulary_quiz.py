from typing import Any, Text, Dict, List, Optional
import logging, requests, json, string, os, string
import random as rand
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction
from rasa_sdk.forms import FormAction
from englishbot_actions import *


class VocabularyQuizForm(FormAction):
    """ Starts vocabulary quiz """

    def name(self):
        return "vocabulary_quiz_form"

    @staticmethod
    def required_slots(tracker):
        return ["vocabulary_quiz_exit"]

    def slot_mappings(self):
        return {
            "vocabulary_quiz_exit": [
                self.from_intent(intent="learning.exit", value="exit"),
                self.from_text(not_intent="learning.exit"),
            ]
        }

    def validate_vocabulary_quiz_exit(self, value, dispatcher, tracker, domain):
        """ Check to see if user wants to exit the quiz, otherwise ask next question. """

        last_intent = tracker.latest_message['intent'].get('name')
        last_intent_conf = tracker.latest_message['intent'].get('confidence')

        # user wants to exit quiz
        if last_intent == 'learning.exit':
            return {"vocabulary_quiz_exit": "exit"}

        # user wants to know the meaning of a word
        elif last_intent == 'word.meaning' and last_intent_conf > 0.80:
            get_meaning(tracker, dispatcher)
            return {"vocabulary_quiz_exit": None}

        # users wants to get a hint
        elif last_intent == 'learning.hint' or last_intent == 'ask_whatspossible' or last_intent == 'how_does_it_work' \
                and last_intent_conf > 0.80:
            get_hint(tracker, dispatcher)
            return {"vocabulary_quiz_exit": None}

        # user has given an answer
        else:
            latest_message = tracker.latest_message.get('text')
            correct_answers_slot = tracker.get_slot('vocabulary_correct_answer')
            counter = tracker.get_slot('vocabulary_counter') or 0

            logging.debug("user input : " + str(latest_message) + ", correct is: " + str(correct_answers_slot))

            correct = False
            latest_message = str(latest_message).lower()
            correct_answers = correct_answers_slot.split(", ")
            users_answer = ""
            for answer in correct_answers:
                # -1 means that substring was not found
                if latest_message.find(answer) != -1:
                    users_answer = answer
                    correct = True

            if correct:
                dispatcher.utter_template("utter_vocabulary_quiz_correct", tracker)
                if len(correct_answers) > 1:
                    possibilities = correct_answers_slot.replace(users_answer + ", ", "")
                    dispatcher.utter_message("You can also say: " + str(possibilities))
                counter = counter + 1
            else:
                dispatcher.utter_template("utter_vocabulary_quiz_not_correct", tracker)
                dispatcher.utter_template("utter_vocabulary_quiz_correct_answer", tracker)

            # next question
            question = get_random_question(tracker)
            correct_answers = ", ".join(str(x) for x in question[1])
            dispatcher.utter_message(question[0])

            return {"word": None, "vocabulary_quiz_exit": None, "vocabulary_user_answer": latest_message,
                    'vocabulary_correct_answer': correct_answers, 'vocabulary_counter': counter}

    def submit(self, dispatcher, tracker, domain):
        correct_answers = tracker.get_slot('vocabulary_counter')

        if correct_answers == 0:
            dispatcher.utter_template("utter_user.learning_exit_no_correct", tracker)
        elif correct_answers == 1:
            dispatcher.utter_template("utter_user.learning_exit_one_correct", tracker)
        else:
            dispatcher.utter_template("utter_user.learning_exit", tracker)

        return [SlotSet('vocabulary_quiz_exit', None), SlotSet('vocabulary_user_answer', None),
                SlotSet('vocabulary_correct_answer', None), SlotSet('vocabulary_counter', None)]


class AskQuestion(Action):
    """ Action that returns next quiz question """

    def name(self):
        return 'action_ask_question'

    def run(self, dispatcher, tracker, domain):
        # get random question
        question = get_random_question(tracker)
        # turn list into string
        correct_answers = ", ".join(str(x) for x in question[1])
        # send random question to user
        dispatcher.utter_message(question[0])
        return [SlotSet('vocabulary_correct_answer', correct_answers), SlotSet('vocabulary_counter', 0)]


def get_random_question(tracker):
    """ Get a random question from university.json """

    # currently only university.json available. Intended to have more vocabulary modules.
    with open(os.path.join(os.path.dirname(__file__), 'vocabulary/university.json'), "r") as f:
        data = json.load(f)
        max_len = len(data)
        random_question_index = rand.randint(0, max_len - 1)

    # get random question from random vocabulary file
    list_of_questions = data[random_question_index]["questions"]

    if len(list_of_questions) > 1:
        max_questions = len(list_of_questions)
        rand_index = rand.randint(0, max_questions - 1)
        question = list_of_questions[rand_index]

    elif len(list_of_questions) == 1:
        question = list_of_questions[0]

    else:
        question = create_question(data[random_question_index]["definition"])

    return [question, data[random_question_index]["words"]]


def create_question(definition):
    """ Create a random question for vocabulary withouth predefined questions """
    questions = ["What is the term for ",
                 "How do you call ",
                 "What's ",
                 "What's the word for ",
                 "What's the term for ",
                 "What is the word for ",
                 "What is ",
                 "Do you know the word for "]

    rand_index = rand.randint(0, len(questions) - 1)
    return questions[rand_index] + definition + "?"


def get_hint(tracker, dispatcher):
    """ Method that sends hint for current question """
    dispatcher.utter_message("Ok, here's my hint for you 💡")
    slot_answers = tracker.get_slot('vocabulary_correct_answer')
    total_answers = slot_answers.split(", ")
    answer_str = total_answers[0][0].upper()
    word_parts = 1
    for letter in total_answers[0][1:]:
        if letter == " ":
            answer_str += "   "
            word_parts += 1
        else:
            answer_str += " _ "
    word_parts_str = str(word_parts) + " word" if word_parts <= 1 else str(word_parts) + " words"
    dispatcher.utter_message("The word we're looking for consists of " + str(
        word_parts_str) + " and starts with the following letter: ")
    dispatcher.utter_message(str(answer_str))
    return


def get_meaning(tracker, dispatcher):
    """ Method to get meaning of a word while in vocabulary quiz """
    search_term = tracker.get_slot("word")

    if search_term is not None:
        results = DictionaryCall.get_meaning_for_word(search_term)
        results_len = len(results)
        if results_len > 1:
            dispatcher.utter_message("I couldn't find a definition for the word " + str(
                search_term) + ", but here's the definition for the individual words.")
            for result in results:
                dispatcher.utter_message(json.dumps(result))
        elif results_len == 1:
            dispatcher.utter_message("That's what I've found: ")
            dispatcher.utter_message(json.dumps(results))
        else:
            dispatcher.utter_message("I am sorry, I don't know the word " + str(search_term))
    else:
        dispatcher.utter_message(
            "I am sorry, I didn't understand which word you want me to tell you. Could you try to rephrase?")
    return
