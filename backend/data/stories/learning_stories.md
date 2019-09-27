## user wants to learn
* learning.intent_general
  - utter_user.wants_to_learn_english
> user_wants_to_learn

## user wants to learn new vocabulary
> user_wants_to_learn
* learning.teach_vocabulary
  - utter_ask_vocabulary_topic
> check_quizmode_start

## user wants to start vocabulary quiz
> check_quizmode_start
* confirm.yes
  - utter_lets_start_vocabulary_quiz
  - action_ask_question
  - slot{"vocabulary_counter": 0}
  - vocabulary_quiz_form
  - form{"name": "vocabulary_quiz_form"}
  - slot{"vocabulary_counter": 1}
  - slot{"vocabulary_quiz_exit": "exit"}
  - form{"name": null}
  - utter_continue_chatting
> check_continue_chatting

## user wants to continue chatting
> check_continue_chatting
* confirm.yes
    - utter_confirmation.yes
    - action_start_random_conversation
  > start_random_conversation

## user wants to continue chatting
> check_continue_chatting
* confirm.no OR out_of_scope
  - utter_end_chat

## user does not want to start vocabulary quiz
> check_quizmode_start
* confirm.no OR out_of_scope
  - utter_continue_chatting
* confirm.yes
  - utter_confirmation.yes
  - action_start_random_conversation
  > start_random_conversation

## user does not want to start vocabulary quiz
> check_quizmode_start
* confirm.no OR out_of_scope
  - utter_continue_chatting
* confirm.no
  - utter_confirmation.no
  - utter_end_chat

## start quiz mode
* learning.teach_vocabulary
  - utter_ask_vocabulary_topic
> check_quizmode_start

## get meaning for word 1
> user_wants_to_learn
* word.meaning{"word": "syllabus"}
  - slot{"word": "syllabus"}
  - action_dictionary_meaning
  - slot{"word": null}

## get meaning for word 2
> user_wants_to_learn
* word.meaning{"word": null}
  - utter_tell_me_word
  - dictionary_form
  - action_listen
  - form{"name": "dictionary_form"}
  - slot{"requested_slot": "word"}
  - form{"name": null}
  - slot{"word": null}

## get meaning for word 3
> user_wants_to_learn
* word.meaning
  - utter_tell_me_word
  - dictionary_form
  - action_listen
  - form{"name": "dictionary_form"}
  - slot{"requested_slot": "word"}
  - form{"name": null}
  - slot{"word": null}

## get meaning for word 1
* word.meaning{"word": "boredom"}
  - slot{"word": "boredom"}
  - action_dictionary_meaning
  - slot{"word": null}


## get meaning for word 2
* word.meaning{"word": null}
  - utter_tell_me_word
  - dictionary_form
  - action_listen
  - form{"name": "dictionary_form"}
  - slot{"requested_slot": "word"}
  - form{"name": null}
  - slot{"word": null}

## get meaning for word 3
* word.meaning
  - utter_tell_me_word
  - dictionary_form
  - action_listen
  - form{"name": "dictionary_form"}
  - slot{"requested_slot": "word"}
  - form{"name": null}
  - slot{"word": null}