
## interactive_story_1
* greet.hello
    - action_greet_user
    - introduction_form

## interactive_story_2
* greet.hello
    - action_greet_user
    - introduction_form
    - form{"name": "introduction_form"}
    - slot{"requested_slot": "name"}
* form: user.name{"name": "Anna Lisa"}
    - slot{"name": "Anna Lisa"}
    - form: introduction_form
    - slot{"name": "Anna Lisa"}
    - slot{"current_user_name": "Anna Lisa"}
    - slot{"requested_slot": "location"}
* form: user.location{"location": "malaga"}
    - slot{"location": "malaga"}
    - form: introduction_form
    - slot{"location": "Malaga"}
    - slot{"current_location": "Malaga"}
    - slot{"word": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_user.location_good
* confirm.yes+user.location.likes
    - utter_user.location_go_there
    - utter_bot_help
    - action_how_to
* bot.name
    - utter_bot.name
* nice_to_meet_you
    - utter_nice_to_meet_you_too
* out_of_scope
    - utter_cannot_help
    - utter_explain_whatspossible
* word.meaning{"word": "foundation"}
    - slot{"word": "foundation"}
    - action_dictionary_meaning
    - slot{"word": null}
* appraisal.thanks
    - utter_appraisal.welcome
* ask_whatspossible
    - utter_explain_whatspossible
* learning.teach_vocabulary
    - utter_ask_vocabulary_topic
* confirm.yes
    - utter_lets_start_vocabulary_quiz
    - action_ask_question
    - slot{"vocabulary_correct_answer": "careers service, career service"}
    - slot{"vocabulary_counter": 0}
    - vocabulary_quiz_form
    - form{"name": "vocabulary_quiz_form"}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: out_of_scope
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": null}
    - slot{"word": null}
    - slot{"vocabulary_user_answer": "let me say career service"}
    - slot{"vocabulary_correct_answer": "office hours"}
    - slot{"vocabulary_counter": 1}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: learning.hint
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": null}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: out_of_scope
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": null}
    - slot{"word": null}
    - slot{"vocabulary_user_answer": "oh office hours right?"}
    - slot{"vocabulary_correct_answer": "fellow student"}
    - slot{"vocabulary_counter": 2}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: learning.exit
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": "exit"}
    - slot{"vocabulary_quiz_exit": null}
    - slot{"vocabulary_user_answer": null}
    - slot{"vocabulary_correct_answer": null}
    - slot{"vocabulary_counter": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_continue_chatting
* confirm.yes
    - utter_confirmation.yes
    - action_start_random_conversation
    - slot{"chat_topic": "studying"}
* confirm.no
    - utter_user.profession
* out_of_scope
    - utter_show_interest
    - action_end_random_conversation
    - slot{"chat_topic": null}
    - action_bot_questions
    - slot{"word": null}
* confirm.yes
    - utter_confirmation.yes_questions
* bot.age
    - utter_bot.age
* user.age
    - utter_user.age
* bot.real
    - utter_bot.real
* confirm.yes
    - utter_confirmation.yes
* word.meaning{"word": "colander"}
    - slot{"word": "colander"}
    - action_dictionary_meaning
    - slot{"word": null}
* greet.goodbye
    - utter_greet.goodbye
    - utter_end_chat

## interactive_story_3
* greet.hello
    - action_greet_user
    - introduction_form
    - form{"name": "introduction_form"}
    - slot{"requested_slot": "name"}
* form: user.name+bot.name{"name": "Norman"}
    - slot{"name": "Norman"}
    - form: introduction_form
    - slot{"name": "Norman"}
    - slot{"current_user_name": "Norman"}
    - slot{"requested_slot": "location"}
* form: user.location{"location": "trondheim"}
    - slot{"location": "trondheim"}
    - form: introduction_form
    - slot{"location": "Trondheim"}
    - slot{"current_location": "Trondheim"}
    - slot{"word": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_user.location_good
* confirm.yes
    - utter_user.location_go_there
    - utter_bot_help
    - action_how_to
* bot.age
    - utter_bot.age
* user.age
    - utter_user.age
* out_of_scope
    - utter_cannot_help
    - utter_explain_whatspossible
* word.meaning
    - utter_tell_me_word
    - dictionary_form
    - form{"name": "dictionary_form"}
    - slot{"requested_slot": "word"}
* form: word.meaning{"word": "gondola"}
    - slot{"word": "gondola"}
    - form: dictionary_form
    - slot{"word": "gondola"}
    - form: followup{"name": "action_dictionary_meaning"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_dictionary_meaning
    - slot{"word": null}
* appraisal.thanks
    - utter_appraisal.welcome
* user.wants_to_chat
    - action_start_random_conversation
    - slot{"chat_topic": "studying"}
* confirm.yes
    - utter_user.studying.ask_subject
* user.degree_program{"degree_program": "biomedicine"}
    - action_user_degree_program
    - slot{"user_degree_program": "Biomedicine"}
    - action_react_to_degree_program
* user.degree_program.semester
    - utter_user.plans_after_studies
* confirm.no+user.location.not_likes{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_end_random_conversation
    - slot{"chat_topic": null}
    - action_bot_questions
    - slot{"word": null}
* greet.goodbye
    - utter_greet.goodbye
    - utter_end_chat


## interactive_story_4
* greet.hello
    - action_greet_user
    - introduction_form
    - form{"name": "introduction_form"}
    - slot{"requested_slot": "name"}
* form: user.name+bot.name{"name": "Tiffany"}
    - slot{"name": "Tiffany"}
    - form: introduction_form
    - slot{"name": "Tiffany"}
    - slot{"current_user_name": "Tiffany"}
    - slot{"requested_slot": "location"}
* form: user.location{"location": "Salzburg"}
    - slot{"location": "Salzburg"}
    - form: introduction_form
    - slot{"location": "Salzburg"}
    - slot{"current_location": "Salzburg"}
    - slot{"word": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_user.location_good
* confirm.no
    - utter_bot_help
    - action_how_to
* what_time_is_it
  - action_tell_time
* bot.age
    - utter_bot.age
* user.age
    - utter_user.age
* out_of_scope
    - utter_cannot_help
    - utter_explain_whatspossible
* bot.joke
  - action_joke
* bot.bad_joke
  - utter_bad_joke
* confirm.no
  - utter_user_what_now
* word.meaning
    - utter_tell_me_word
    - dictionary_form
    - form{"name": "dictionary_form"}
    - slot{"requested_slot": "word"}
* form: word.meaning{"word": "gondola"}
    - slot{"word": "gondola"}
    - form: dictionary_form
    - slot{"word": "gondola"}
    - form: followup{"name": "action_dictionary_meaning"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_dictionary_meaning
    - slot{"word": null}
* appraisal.thanks
    - utter_appraisal.welcome
* bot.languages
  - utter_bot.languages
* user.wants_to_chat
    - action_start_random_conversation
    - slot{"chat_topic": "studying"}
* confirm.yes
    - utter_user.studying.ask_subject
* user.degree_program{"degree_program": "biomedicine"}
    - action_user_degree_program
    - slot{"user_degree_program": "Biomedicine"}
    - action_react_to_degree_program
* user.degree_program.semester
    - utter_user.plans_after_studies
* confirm.no+user.location.not_likes{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_end_random_conversation
    - slot{"chat_topic": null}
    - action_bot_questions
    - slot{"word": null}
* greet.goodbye
    - utter_greet.goodbye
    - utter_end_chat

## interactive_story_5
* greet.hello
    - action_greet_user
    - introduction_form
    - form{"name": "introduction_form"}
    - slot{"requested_slot": "name"}
* form: user.name+bot.name{"name": "Karin"}
    - slot{"name": "Karin"}
    - form: introduction_form
    - slot{"name": "Karin"}
    - slot{"current_user_name": "Karin"}
    - slot{"requested_slot": "location"}
* form: user.location{"location": "Hamburg"}
    - slot{"location": "Hamburg"}
    - form: introduction_form
    - slot{"location": "Hamburg"}
    - slot{"current_location": "Hamburg"}
    - slot{"word": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_user.location_good
* confirm.yes
    - utter_user.location_go_there
    - utter_bot_help
    - action_how_to
* bot.hobbies
  - utter_bot.hobbies
  - utter_bot.and_you
* user.hobbies
  - utter_show_interest
* bot.joke
  - action_joke
* emotions.ha_ha
  - utter_emotions.ha_ha
  - utter_user_what_now
* learning.teach_vocabulary
    - utter_ask_vocabulary_topic
* confirm.yes
    - utter_lets_start_vocabulary_quiz
    - action_ask_question
    - slot{"vocabulary_correct_answer": "red butter"}
    - slot{"vocabulary_counter": 0}
    - vocabulary_quiz_form
    - form{"name": "vocabulary_quiz_form"}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: out_of_scope
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": null}
    - slot{"word": null}
    - slot{"vocabulary_user_answer": "let me say schedule"}
    - slot{"vocabulary_correct_answer": "office hours"}
    - slot{"vocabulary_counter": 0}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: learning.hint
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": null}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: out_of_scope
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": null}
    - slot{"word": null}
    - slot{"vocabulary_user_answer": "oh maybe you mean books?"}
    - slot{"vocabulary_correct_answer": "fellow student"}
    - slot{"vocabulary_counter": 0}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: learning.exit
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": "exit"}
    - slot{"vocabulary_quiz_exit": null}
    - slot{"vocabulary_user_answer": null}
    - slot{"vocabulary_correct_answer": null}
    - slot{"vocabulary_counter": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_continue_chatting
* confirm.yes
    - utter_confirmation.yes
    - action_start_random_conversation
    - slot{"chat_topic": "studying"}
* user.degree_program
    - action_user_degree_program
    - action_react_to_degree_program
* user.degree_program.semester
    - utter_user.plans_after_studies
* out_of_scope
    - action_end_random_conversation
    - slot{"chat_topic": null }
    - slot{"word": null}
    - action_bot_questions
* bot.gender
  - utter_bot.gender
* bot.location
  - utter_bot.location
* bot.real
  - utter_bot.real
* bot.be_clever
  - utter_bot.be_clever
* greet.goodbye
    - utter_greet.goodbye
    - utter_end_chat


## interactive_story_6
* greet.hello
    - action_greet_user
    - introduction_form
    - form{"name": "introduction_form"}
    - slot{"requested_slot": "name"}
* form: user.name+bot.name{"name": "Annabelle"}
    - slot{"name": "Annabelle"}
    - form: introduction_form
    - slot{"name": "Annabelle"}
    - slot{"current_user_name": "Annabelle"}
    - slot{"requested_slot": "location"}
* form: user.location{"location": "Paris"}
    - slot{"location": "Paris"}
    - form: introduction_form
    - slot{"location": "Paris"}
    - slot{"current_location": "Paris"}
    - slot{"word": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_user.location_good
* confirm.yes
    - utter_user.location_go_there
    - utter_bot_help
    - action_how_to
* bot.name
  - utter_bot.name 
* bot.languages
  - utter_bot.languages
* greet.how_are_you
  - utter_bot.mood.good
  - utter_greet.ask_how_are_you
* user_mood.good
  - utter_user.mood.happy
* bot.hobbies
  - utter_bot.hobbies
  - utter_bot.and_you
* user.hobbies
  - utter_show_interest
* bot.be_clever
  - utter_bot.be_clever
* greet.goodbye
    - utter_greet.goodbye
    - utter_end_chat

## interactive_story_7
* greet.hello
    - action_greet_user
    - introduction_form
    - form{"name": "introduction_form"}
    - slot{"requested_slot": "name"}
* form: user.name{"name": "Chris"}
    - slot{"name": "Chris"}
    - form: introduction_form
    - slot{"name": "Chris"}
    - slot{"current_user_name": "Chris"}
    - slot{"requested_slot": "location"}
* form: user.location{"location": "Gibraltar"}
    - slot{"location": "Gibraltar"}
    - form: introduction_form
    - slot{"location": "Gibraltar"}
    - slot{"current_location": "Gibraltar"}
    - slot{"word": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_user.location_good
* confirm.no
    - utter_bot_help
    - action_how_to
* bot.name
    - utter_bot.name
* nice_to_meet_you
    - utter_nice_to_meet_you_too
* out_of_scope
    - utter_cannot_help
    - utter_explain_whatspossible
* bot.stupid
  - utter_bot.stupid
* word.meaning{"word": "keyboard"}
    - slot{"word": "keyboard"}
    - action_dictionary_meaning
    - slot{"word": null}
* appraisal.thanks
    - utter_appraisal.welcome
* word.meaning{"word": "display"}
    - slot{"word": "display"}
    - action_dictionary_meaning
    - slot{"word": null}
* word.meaning{"word": "orange tree"}
    - slot{"word": "orange tree"}
    - action_dictionary_meaning
    - slot{"word": null}
* appraisal.thanks
  - utter_appraisal.welcome
* bot.knows_a_lot
  - utter_bot.thanks_for_compliment
* what_time_is_it
  - action_tell_time
* bot.joke
  - action_joke
* emotions.ha_ha 
  - utter_emotions.ha_ha
  - utter_user_what_now
* greet.how_are_you
  - utter_bot.mood.good
  - utter_greet.ask_how_are_you
* user_mood.bad
  - utter_user.mood.unhappy
* confirm.no 
  - utter_continue_chatting
* confirm.no 
  - utter_confirmation.no
  - utter_end_chat
* bot.gender
  - utter_bot.gender
* greet.goodbye
    - utter_greet.goodbye
    - utter_end_chat

## interactive_story_8
* greet.hello
    - action_greet_user
    - introduction_form
    - form{"name": "introduction_form"}
    - slot{"requested_slot": "name"}
* form: user.name{"name": "Bernd"}
    - slot{"name": "Bernd"}
    - form: introduction_form
    - slot{"name": "Bernd"}
    - slot{"current_user_name": "Bernd"}
    - slot{"requested_slot": "location"}
* form: user.location{"location": "Bielefeld"}
    - slot{"location": "Bielefeld"}
    - form: introduction_form
    - slot{"location": "Bielefeld"}
    - slot{"current_location": "Bielefeld"}
    - slot{"word": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_user.location_good
* confirm.no
    - utter_bot_help
    - action_how_to
* ask_whatspossible
    - utter_explain_whatspossible
* learning.teach_vocabulary
    - utter_ask_vocabulary_topic
* confirm.yes
    - utter_lets_start_vocabulary_quiz
    - action_ask_question
    - slot{"vocabulary_correct_answer": "schedule"}
    - slot{"vocabulary_counter": 0}
    - vocabulary_quiz_form
    - form{"name": "vocabulary_quiz_form"}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: out_of_scope
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": null}
    - slot{"word": null}
    - slot{"vocabulary_user_answer": "that's a hard one. i only know the german word."}
    - slot{"vocabulary_correct_answer": "professor"}
    - slot{"vocabulary_counter": 1}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: learning.hint
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": null}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: learning.hint
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": null}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: out_of_scope
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": null}
    - slot{"word": null}
    - slot{"vocabulary_user_answer": "tell me the answer?"}
    - slot{"vocabulary_correct_answer": "lecture"}
    - slot{"vocabulary_counter": 2}
    - slot{"requested_slot": "vocabulary_quiz_exit"}
* form: learning.exit
    - form: vocabulary_quiz_form
    - slot{"vocabulary_quiz_exit": "exit"}
    - slot{"vocabulary_quiz_exit": null}
    - slot{"vocabulary_user_answer": null}
    - slot{"vocabulary_correct_answer": null}
    - slot{"vocabulary_counter": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_continue_chatting
* confirm.yes
    - utter_confirmation.yes
    - action_start_random_conversation
    - slot{"chat_topic": "studying"}
* confirm.no
    - utter_user.profession
* out_of_scope
    - utter_show_interest
    - action_end_random_conversation
    - slot{"chat_topic": null}
    - action_bot_questions
    - slot{"word": null}
* confirm.yes
    - utter_confirmation.yes_questions
* bot.name
    - utter_bot.name
* nice_to_meet_you
    - utter_nice_to_meet_you_too
* out_of_scope
    - utter_cannot_help
    - utter_explain_whatspossible
* bot.stupid
  - utter_bot.stupid
* word.meaning{"word": "keyboard"}
    - slot{"word": "keyboard"}
    - action_dictionary_meaning
    - slot{"word": null}
* appraisal.thanks
    - utter_appraisal.welcome
* word.meaning{"word": "display"}
    - slot{"word": "display"}
    - action_dictionary_meaning
    - slot{"word": null}
* word.meaning{"word": "orange tree"}
    - slot{"word": "orange tree"}
    - action_dictionary_meaning
    - slot{"word": null}
* appraisal.thanks
  - utter_appraisal.welcome
* bot.knows_a_lot
  - utter_bot.thanks_for_compliment
* what_time_is_it
  - action_tell_time
* bot.joke
  - action_joke
* emotions.ha_ha 
  - utter_emotions.ha_ha
  - utter_user_what_now
* greet.how_are_you
  - utter_bot.mood.good
  - utter_greet.ask_how_are_you
* user_mood.bad
  - utter_user.mood.unhappy
* confirm.no 
  - utter_continue_chatting
* confirm.no 
  - utter_confirmation.no
  - utter_end_chat
* bot.gender
  - utter_bot.gender
* greet.goodbye
    - utter_greet.goodbye
    - utter_end_chat

## user age
* user.age
  - utter_user.age

## user impressed
* bot.knows_a_lot
  - utter_bot.thanks_for_compliment

## bot location
* bot.location
  - utter_bot.location

## bot gender
* bot.gender
  - utter_bot.gender

## bot.real
* bot.real
  - utter_bot.real
