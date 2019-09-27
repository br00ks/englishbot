## user asks whats possible
* ask_whatspossible
  - utter_explain_whatspossible

## user asks for something out of scope
* out_of_scope
  - utter_cannot_help
  - utter_explain_whatspossible

## ask name
* bot.age
  - utter_bot.age
* user.age
  - utter_user.age

## user age
* user.age
  - utter_user.age

## ask name
* bot.age
  - utter_bot.age
* out_of_scope
  - utter_confirmation.no

## appraisal thanks
* appraisal.thanks
  - utter_appraisal.welcome

## user impressed, thinks that bot is clever
* bot.knows_a_lot
  - utter_bot.thanks_for_compliment

## nice to meet you
* nice_to_meet_you
  - utter_nice_to_meet_you_too

## bot location
* bot.location
  - utter_bot.location

## bot gender
* bot.gender
  - utter_bot.gender

## bot.real
* bot.real
  - utter_bot.real

## bot name
* bot.name
  - utter_bot.name

## bot.languages
* bot.languages
  - utter_bot.languages

## user_mood.good+greet.how_are_you
* user_mood.good+greet.how_are_you
  - utter_user.mood.happy
  - utter_bot.mood.good

## confirm.yes
* confirm.yes
  - utter_confirmation.yes

## greet.how_are_you
* greet.how_are_you
  - utter_bot.mood.good
  - utter_greet.ask_how_are_you
* user_mood.good
  - utter_user.mood.happy

## greet.how_are_you
* greet.how_are_you
  - utter_bot.mood.good
  - utter_greet.ask_how_are_you
* user_mood.bad
  - utter_user.mood.unhappy
> check_quizmode_start

## user mood bad
* user_mood.bad
  - utter_user.mood.unhappy
> check_quizmode_start

## user mood good
* user_mood.good
  - utter_user.mood.happy

## bot.hobbies
* bot.hobbies
  - utter_bot.hobbies
  - utter_bot.and_you
* user.hobbies
  - utter_show_interest

## bot joke
* bot.joke
  - action_joke
  > bad_joke

## bot joke
* bot.joke
  - action_joke
  > good_joke

## good joke
> good_joke
* emotions.ha_ha 
  - utter_emotions.ha_ha
  - utter_user_what_now

## bad joke
> bad_joke
* bot.bad_joke OR out_of_scope
  - utter_bad_joke
* confirm.yes
  - action_joke

## bad joke
> bad_joke
* bot.bad_joke 
  - utter_bad_joke
* confirm.no
  - utter_user_what_now

## emotions
* emotions.ha_ha
  - utter_emotions.ha_ha
  - utter_user_what_now

## how_does_it_work
* how_does_it_work
  - action_how_to

## tell time
* what_time_is_it
  - action_tell_time

## bot stupid
* bot.stupid
  - utter_bot.stupid

## bot be clever
* bot.be_clever
  - utter_bot.be_clever
