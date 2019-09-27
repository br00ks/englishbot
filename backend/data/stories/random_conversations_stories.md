## user wants to chat
* user.wants_to_chat
    - action_start_random_conversation
    > start_random_conversation

## studying story happy path
> start_random_conversation
* confirm.yes OR user.is_student
    - utter_user.studying.ask_subject
* user.degree_program
    - action_user_degree_program
    - action_react_to_degree_program
* user.degree_program.semester OR out_of_scope
    - utter_user.plans_after_studies
> plans_after_studies

## user.is_student
* user.is_student
    - utter_user.studying.ask_subject
* user.degree_program
    - action_user_degree_program
    - action_react_to_degree_program
* user.degree_program.semester OR out_of_scope
    - utter_user.plans_after_studies
> plans_after_studies

## user studies
* user.degree_program
    - action_user_degree_program
    - action_react_to_degree_program
* user.degree_program.semester OR out_of_scope
    - utter_user.plans_after_studies
> plans_after_studies

## studying story happy path
> start_random_conversation
* confirm.yes{"degree_program": "Mathematics"}
    - action_user_degree_program
    - action_react_to_degree_program
* user.degree_program.semester OR out_of_scope
    - utter_user.plans_after_studies
> plans_after_studies

## studying story SAD path
> start_random_conversation
* confirm.no
    - utter_user.profession
* user.profession
    - utter_show_interest
    - action_end_random_conversation
    - slot{"chat_topic": null }
    - slot{"word": null}
    - action_bot_questions
    > bot_questions

## studying story SAD path
> start_random_conversation
* confirm.no
    - utter_user.profession
* user.profession
    - utter_show_interest
    - action_end_random_conversation
    - slot{"chat_topic": null }
    - slot{"word": null}
    - action_bot_questions

## plans after studies yes
> plans_after_studies
* confirm.yes
    - action_end_random_conversation
    - slot{"chat_topic": null }
    - slot{"word": null}
    - action_bot_questions

## plans after studies no
> plans_after_studies
* confirm.no OR out_of_scope
    - action_end_random_conversation
    - slot{"chat_topic": null }
    - slot{"word": null}
    - action_bot_questions
> bot_questions

## plans after studies no
> plans_after_studies
* confirm.no OR out_of_scope
    - action_end_random_conversation
    - slot{"chat_topic": null }
    - slot{"word": null}
    - action_bot_questions
* bot.name
  - utter_bot.name
* bot.age
  - utter_bot.age
  
## bot questions no
> bot_questions
* confirm.no OR out_of_scope
    - utter_end_chat

## bot questions yes
> bot_questions
* confirm.yes
    - utter_confirmation.yes_questions
