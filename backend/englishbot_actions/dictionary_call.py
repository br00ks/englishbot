import logging, requests, json
from nltk.corpus import wordnet
from wiktionaryparser import WiktionaryParser


class DictionaryCall:
    """ Class to retrieve definitions from either Wordnet or Wiktionary """

    def __init__(self, word):
        """
        @param word: search term
        @type word: String
        """
        self.word = word

    def get_meaning_for_word(word):
        """
        @param word: search term
        @type word: String
        @return: results
        @rtype: json
        """
        logging.debug("Search term: " + word)
        results = []
        wordnet_results = get_wordnet_meaning(word)

        # first check if word found by wordnet
        if wordnet_results is not None:
            print(str(wordnet_results))
            results.append(wordnet_results)
            return results

        # second check if wiktionary has definition for the word
        else:
            wiktionary_results = get_wiktionary_meaning(word)

            if wiktionary_results is not None:
                results.append(wiktionary_results)
                return results

            # third if there still no results, check if there's multiple words to search for
            else:
                if len(word.split()) > 1:
                    results = []
                    for word_part in word.split():
                        wordnet_results = get_wordnet_meaning(word_part)
                        if wordnet_results is not None:
                            results.append(wordnet_results)
                    return results

                # if word is found neither in wordnet nor on wiktionary then this word is probably not known
                else:
                    return None


def get_wordnet_meaning(word):
    """
    @param word: word user wants to know the definition of
    @type word: String
    @return: results or None
    @rtype: json-array
    """
    word = word.replace(' ', '_') if word.find(" ") else word

    if wordnet.synsets(word):
        logging.debug("number of synsets: " + str(len(wordnet.synsets(word))))
        results = {}
        definitions = []
        synsets_for_word = wordnet.synsets(word)
        synset_found_for_word = True if str(synsets_for_word).find(str(word)) != -1 else False

        for msg in synsets_for_word:
            counter = 0
            word_name = get_word_for_synset(str(msg))

            if str(word_name) == str(word):
                word_name = word_name if word_name.find('_') is False else word_name.replace('_', ' ')
                definitions.append({
                    'word': word_name,
                    'definition': msg.definition(),
                    "pos": get_pos(msg),
                    'synonyms': msg.lemma_names(),
                    'examples': msg.examples()
                })

            elif synset_found_for_word is False and counter <= 2:
                word_name = word_name if word_name.find('_') is False else word_name.replace('_', ' ')
                definitions.append({
                    'word': word_name,
                    'definition': msg.definition(),
                    "pos": get_pos(msg),
                    'synonyms': msg.lemma_names(),
                    'examples': msg.examples()
                })
                counter += 1

        results['results'] = definitions
        results['msg_type'] = 'dictionary_result'
        logging.debug("Wordnet results: " + json.dumps(results))
        return results
    else:
        return None


def get_wiktionary_meaning(word):
    """
    @param word: word user wants definition for
    @type word: String
    @return: results or None
    @rtype: json-array
    """

    parser = WiktionaryParser()

    # prepare search term for URL
    word = word.replace(' ', '%20') if word.find(" ") else word

    # first: perform open search
    url = 'https://en.wiktionary.org/w/api.php?format=json&utf-8&action=opensearch&search=' + str(word)
    req = json.loads(
        requests.get(url, headers={'Accept': 'application/json'}).text
    )

    # second: get the first result, which is the one that is most important
    if req[3]:
        term_string = str(req[3][0]).split('/')
        wiktionary_term = term_string[len(term_string) - 1]
        fetch_word = parser.fetch(wiktionary_term)

        # third: get the definition(s)
        if fetch_word:
            results = {}
            definitions = []

            for definition in fetch_word[0]['definitions']:
                definitions.append({
                    'word': definition['text'][0],
                    'definition': definition['text'][1],
                    'pos': definition['partOfSpeech'],
                    'related_words': definition['relatedWords'],
                    'examples': definition['examples'],
                    'synonyms': []
                })

            results['results'] = definitions
            results['msg_type'] = 'dictionary_result'

            if results['results']:
                logging.debug("Wiktionary results: " + json.dumps(results))
                return results
            else:
                return None
    else:
        return None


def get_pos(word):
    """
    @param word: word to get POS tag for
    @type word: String
    @return: POS Tag
    @rtype: String
    """
    positions = [pos for pos, char in enumerate(str(word)) if char == "."]
    first_dot = positions[0] + 1
    second_dot = positions[1]
    pos_short = str(word)[first_dot:second_dot]

    switcher = {
        "a": "Adjective",
        "s": "Adjective",
        "r": "Adverb",
        "n": "Noun",
        "v": "Verb"
    }
    return switcher.get(pos_short, "INVALID")


def get_word_for_synset(word):
    """
    @param word: Synset that includes word to search for
    @type word: String
    @return: extracted word
    @rtype: String
    """
    positions = [pos for pos, char in enumerate(str(word)) if char == "."]
    pos_first = str(word).find("'") + 1
    pos_dot = str(word).find(".")
    str_word = str(word)[pos_first:pos_dot]
    return str_word
