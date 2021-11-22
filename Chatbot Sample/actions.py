# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import urllib.request
client_id = "DjKlYQQjgTZzkH02btlM" # 애플리케이션 등록시 발급 받은 값
client_secret = "eE4XOrJz2c" # 애플리케이션 등록시 발급 받은 값

class ActionBookSearch(Action):

    def name(self) -> Text:
        return "action_book_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Book Search!\n")
        
        target = tracker.get_slot('info')
        encTarget = urllib.parse.quote(target)
        url = "https://openapi.naver.com/v1/search/book?query=" + encTarget +"&display=3&sort=count"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        result = ""
        if(rescode==200):
            book_info_json = response.read().decode('utf-8')
            import json
            book_info_py = json.loads(book_info_json)
            i = 1
            for item in book_info_py["items"]:
                result += str(i) + "  "
                result += item["title"] + "\n"
                i +=1
            result += "================="
        else:
            result += "Error Code:" + rescode
        dispatcher.utter_message(result)
        return []

    
class ActionContentSearch(Action):

    def name(self) -> Text:
        return "action_content_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Content Search!\n")
        
        target = tracker.get_slot('info')
        encTarget = urllib.parse.quote(target)
        url = "https://openapi.naver.com/v1/search/book?query=" + encTarget +"&display=3&sort=count"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        result = ""
        if(rescode==200):
            book = tracker.get_slot('book')
            book_info_json = response.read().decode('utf-8')
            import json
            book_info_py = json.loads(book_info_json)
            i = 1
            result += book_info_py["items"][int(book[0])-1]["title"] + "\n내용 : "
            result += book_info_py["items"][int(book[0])-1]["description"]
            result += "\n================="
        else:
            result += "Error Code:" + rescode
            
        
        dispatcher.utter_message(result)
        return []

    
class ActionPriceSearch(Action):

    def name(self) -> Text:
        return "action_price_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Price Search!\n")
        
        target = tracker.get_slot('info')
        encTarget = urllib.parse.quote(target)
        url = "https://openapi.naver.com/v1/search/book?query=" + encTarget +"&display=3&sort=count"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        result = ""
        if(rescode==200):
            book = tracker.get_slot('book')
            book_info_json = response.read().decode('utf-8')
            import json
            book_info_py = json.loads(book_info_json)
            i = 1
            result += book_info_py["items"][int(book[0])-1]["title"] + "\n가격 : "
            result += book_info_py["items"][int(book[0])-1]["price"]
            result += "원\n================="
        else:
            result += "Error Code:" + rescode
            
        
        dispatcher.utter_message(result)
        return []
