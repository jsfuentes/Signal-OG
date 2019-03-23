import json 
import requests
from datetime import datetime
import aiohttp
import asyncio
from threading import Thread

from .models import hnToPost

worker_loop = asyncio.new_event_loop()

class HackerNews:
    BASE_URL = "https://hacker-news.firebaseio.com/v0"

    async def getItem(self, session, id):
        async with session.get(f"{self.BASE_URL}/item/{id}.json") as resp:
            item = await resp.json()
            return item

    async def getItems(self, ids):
        items = []
        async with aiohttp.ClientSession() as session:
            for id in ids:
                item = await self.getItem(session, id)
                items.append(item)
        return items
        
    def getTopStories(self, limit): #max 500
        resp = requests.get(f"{self.BASE_URL}/topstories.json")
        ids = json.loads(resp.text)
        if limit > 500:
            limit = 500
        ids = ids[:limit]
        items = worker_loop.run_until_complete(self.getItems(ids))
        items = list(map(hnToPost, items))
        # print("HN", items)
        return items

if __name__ == "__main__":
    hn = HackerNews()
    hn.getTopStories(10)

