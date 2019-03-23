import json 
import requests
from datetime import datetime
import aiohttp
import asyncio

class HackerNews:
    BASE_URL = "https://hacker-news.firebaseio.com/v0"

    async def getItem(self, session, id):
        async with session.get(f"{self.BASE_URL}/item/{id}.json") as resp:
            rawItem = await resp.text()
            return rawItem

    async def getItems(self, ids):
        items = []
        async with aiohttp.ClientSession() as session:
            for id in ids:
                rawItem = await self.getItem(session, id)
                item = json.loads(rawItem)
                print(item)
                items.append(item)
        return items
        
    def getTopStories(self):
        resp = requests.get(f"{self.BASE_URL}/topstories.json")
        ids = json.loads(resp.text)
        ids = ids[:100]
        print(len(ids))
        dates = []
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.getItems(ids))
# 
hn = HackerNews()
hn.getTopStories()

