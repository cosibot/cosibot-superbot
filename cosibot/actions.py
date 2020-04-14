### First take on action language detection to setup a rasa slot 
#   variable in order to switch agents
#
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests

class LangDetectAPI:
    def detect(sentence_list):
        payload = {'sentence': sentence_list}
        r = requests.post('http://158.177.139.34:7610', json = payload) # address and port hardcoded... could be improved later
        return r.json()

class ActionLangDetect(Action):
    def name(self):
        return "action_detect_languages"

    def run(self, dispatcher, tracker, domain):
#        dispatcher.utter_message(text="detecting language")
        lang_detect_api = LangDetectAPI()
        likely_language = restaurant_api.detect([tracker.latest_message.text]) #check the output of the tracker.latest_message
        return [SlotSet("likely_language", likely_language)]

# we need to update the domain to include the action

### To check the language detect service use this commented code below:
#
# sentences = ['Hola', 'me voy a la playa']
# payload = {'sentence': sentences}
# r = requests.post('http://158.177.139.34:7610', json = payload)
# r.json()

