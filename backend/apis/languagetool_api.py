import requests
import re
import os


def load_spelling_ignore_file():
    """ Loads file where words are defined that should be ignored - thus not be corrected - by LanguageTool """

    file_path = os.path.join(os.path.dirname(__file__), "spelling_ignore.txt")
    spelling_ignore_list_file = open(file_path)
    spelling_ignore_list = [line.rstrip() for line in spelling_ignore_list_file]
    spelling_ignore_list_file.close()

    return spelling_ignore_list


# List of words that should not be corrected by LanguageTool
spelling_ignore_list = load_spelling_ignore_file()


class LanguageTool:
    """ class to communicate with LanguageTool Server """

    def __init__(self, server_url, server_port, api_version="v2"):
        self.api_url = "http://{}:{}/{}".format(server_url, server_port, api_version)
        # use american english
        self.language = "en-US"

        # Ignore the following rules
        self.disabled_rules = [
            "EN_QUOTES",
            "UPPERCASE_SENTENCE_START",
            "PUNCTUATION_PARAGRAPH_END",
            "I_LOWERCASE",
        ]

    def check_message(self, input_text):
        """
        Calls the check endpoint, which is responsible for detecting errors in a given text.
        Response is wrapped in a custom response object.
        """
        url = self.api_url + "/check"

        request_parameters = {
            "text": input_text,
            "language": self.language,
            "disabledRules": ",".join(self.disabled_rules)
        }

        response = requests.post(url, data=request_parameters)

        if response.status_code != 200:
            raise ValueError(response.text)

        # print parameters
        print(request_parameters)
        print(response.json())

        return LanguageToolResponse(input_text, response.json())


class LanguageError:
    """ Class for error detection using LanguageTool """

    def __init__(self, match):
        text_containing_error = match["context"]["text"]
        self.start_pos = match["offset"]
        self.end_pos = self.start_pos + match["length"]
        self.error = text_containing_error[self.start_pos:self.end_pos]
        self.suggestion = self.extract_suggestion(match)
        self.category = self.extract_category(match)
        self.message = self.extract_message(match)

    def extract_suggestion(self, match):
        # consider only replacement value with highest rank, 
        # which means first suggestion result
        suggestion = None
        if (len(match["replacements"]) >= 1):
            suggestion = match["replacements"][0]["value"]
        return suggestion

    def extract_message(self, match):
        word_with_error = match['context']['text'][self.start_pos:self.end_pos]
        print("word with error: " + str(word_with_error))
        message = match['message']
        if (self.category == 'COLLOCATIONS') is True or (self.category == 'NONSTANDARD_PHRASES') is True:
            return match['message']
        else:
            if not 'Did you mean' in message:
                message += "\nDid you mean '" + self.suggestion + "'?"
                return message
        return match['message']

    def extract_category(self, match):
        return match['rule']['category']['id']


class LanguageToolResponse:
    """ Response wrapper for response vom LanguageTool Service """

    def __init__(self, input_text, response):
        self.input_text = input_text
        self.response = response
        self.errors = self.create_errors(response)

    def ignore_entity_errors(self, nlu_entities, entity_types):
        """ Removes errors from the list, if it is an entity of a specific type."""

        def is_entity(err):
            for entity in nlu_entities:
                if entity["start"] <= err.start_pos and entity["end"] >= err.end_pos:
                    if entity["entity"] in entity_types:
                        return True
            return False

        self.errors = list(filter(lambda err: not is_entity(err), self.errors))

    def get_languagetool_errors(self):
        """ Returns a serializable dictionary """
        return list(map(lambda e: e.__dict__, self.errors))

    def create_errors(self, response):
        """ Create list of errors, if found by LanguageTool"""
        list_of_errors = []
        for match in response["matches"]:
            error = LanguageError(match)

            if error != None:
                list_of_errors.append(error)

        return list_of_errors
