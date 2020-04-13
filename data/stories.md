## start conversation
* start:
  - action_ask_language
  
## language_selection
*language_selection
  -utter_language_selection

## initializa slot
* init slot
  - action_init_slot

## greet_en
* greet{"language_slot": "en"}
  - utter_greet_en
  
## greet_de
* greet{"language_slot": "de"}
  - utter_greet_de
  
## thank_en
* thank{"language_slot": "en"}
  - utter_noworries_en

## thank_de
* thank{"language_slot": "de"}
  - utter_noworries_de

## bye_en
* bye{"language_slot": "en"}
  - utter_bye_en
  
## bye_de
* bye{"language_slot": "de"}
  - utter_bye_de