## goodbye
* greet.goodbye
  - utter_greet.goodbye
  - utter_end_chat

## story 01
* greet.hello
  - slot{"current_user_name": "Nina"}
  - slot{"current_location": "Paris"}
  - action_greet_user

## story 02
* user.name{"name": "Angela"}
  - utter_user.name_again

## story 02
* user.location{"location" : "Berlin"}
  -  utter_user.location_again
> check_user_moved

## user moved to another location
> check_user_moved
* confirm.yes
  - utter_user.new_location
* user.location{"location" : "London"}
	- action_save_user_location
	- slot{"current_location": "London"}
	- utter_user.location_good
> check_user_likes_location

## user did not move to another location
> check_user_moved
* confirm.no
  - utter_bot_help
* how_does_it_work
  - action_how_to
> user_wants_to_learn

## greet user first time to get to know each other
* greet.hello
    - action_greet_user
    - introduction_form
    - form{"name": "introduction_form"}
    - slot{"requested_slot": "name"}
* form: user.name{"name": "nora"}
    - slot{"name": "nora"}
    - form: introduction_form
    - slot{"name": "Nora"}
    - slot{"current_user_name": "Nora"}
    - slot{"requested_slot": "location"}
* form: user.location{"location": "castrop rauxel"}
    - slot{"location": "castrop rauxel"}
    - form: introduction_form
    - slot{"location": "Castrop rauxel"}
    - slot{"current_location": "Castrop rauxel"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_user.location_good
  > check_user_likes_location

## user likes location
> check_user_likes_location
* confirm.yes OR confirm.yes+user.location.likes
  - utter_user.location_go_there
  - utter_bot_help
  - action_how_to
> user_wants_to_learn

## user does not like location
> check_user_likes_location
* confirm.no OR confirm.no+user.location.not_likes
  - utter_bot_help
  - action_how_to
> user_wants_to_learn
