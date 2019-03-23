import requests
import json 
from dateutil.parser import parse
from datetime import datetime

last_logged_in_utc = 1552268737
# resp = requests.get(f"{BASE_URL}/maxitem.json")
# curItem = resp.text
# 
# #hackernews can be deleted or null
# while True:
#     if resp.text == "null":
#         item = json.loads(resp.text)
#         print(item)
#         if item['time'] <= last_logged_in_utc:
#             break
#         elif item['type'] == "story" and not item.get('deleted', False):
#             print(item['title'], item['score'])
#     curItem = str(int(curItem) - 1)
#     # print(curItem)

class HackerNews:
    BASE_URL = "https://hacker-news.firebaseio.com/v0"
    
    def getItem(self, id):
        resp = requests.get(f"{self.BASE_URL}/item/{id}.json")
        return json.loads(resp.text)
    
    def getTopStories(self):
        resp = requests.get(f"{self.BASE_URL}/topstories.json")
        ids = json.loads(resp.text)
        print(len(ids))
        dates = []
        for id in ids: 
            x = self.getItem(id)
            dates.append(datetime.utcfromtimestamp(x['time']))
        print(min(dates))
        
hn = HackerNews()
hn.getTopStories()
