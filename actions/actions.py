"""Provide access to Python's configuration information.  The specific
configuration variables available depend heavily on the platform and
configuration.  The values may be retrieved using
get_config_var(name), and the list of variables is available via
get_config_vars().keys().  Additional convenience functions are also
available.

Written by:   Fred L. Drake, Jr.
Email:        <fdrake@acm.org>
"""
import time
import _imp
import os
import re
import sys
#from .errors import DistutilsPlatformError
from rasa_sdk import Action,Tracker
from rasa_sdk.events import SlotSet
from typing import Any,Text,Dict,List
from automationsimplebot import bot_deploy
from rasa_sdk.executor import CollectingDispatcher
#from weatherbot import CityTemp

from weatherbot import CityTemp
#iIS_PYPY = '__pypy__' in sys.builtin_module_names

# These are needed in a couple of spots, so just compute them once.
#PREFIX = os.path.normpath(sys.prefix)
#EXEC_PREFIX = os.path.normpath(sys.exec_prefix)
#BASE_PREFIX = os.path.normpath(sys.base_prefix)
class ActionCheckRestaurants(Action):
   def name(self) -> Text:
       
       return "action_aaemsg"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
     #  entitiesi = tracker.latest_message['entities']
      # print (entitiesi)
      
      # print(additional_slots)
       botresp = CityTemp("delhi")
     #  botresp = bot_deploy()
   #   botresp="hello mama"
    #    print(botresp)
      # dispatcher.utter_template("utter_aaeresponse",tracker,user_msg=botreisp)
      
       dispatcher.utter_template("utter_showadhaar",tracker,adhaarno=botresp)
 #     time.sleep(120)
       return []

