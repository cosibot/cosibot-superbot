# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action #, Tracker
# from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
from rasa_core.events import SlotSet

class AskLanguage(Action):

     def name(self):
         return "action_ask_language"

     def run(self, dispatcher, tracker, domain):

         dispatcher.utter_message(text="Hello, which language would you like to use? English/Englisch or/oder German/Deutsch")

         return [UserUtteranceReverted()]

class SetSlotValue(Action):
     def name(self):
         return "action_init_slot"

     def run(self, dispatcher,tracker,domain):

         slot_value = tracker.get_slot("language_slot")
         entity_value = tracker.get_latest_entity_values("language")

         if slot_value is None and entity_value is not None:
             return [SlotSet("language_slot", entity_value)]
         else:
             return [SlotSet("language_slot", "en")]
        
