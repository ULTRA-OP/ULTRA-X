# ported  by shivam and  LEGENDX22
#own Friday 
# bekar plugin h kaam ni krta kisi ksi ka chalta h bas
# KEEP CREDITS

import os
import re
import urllib
from math import ceil
from re import findall
from youtube_search import YoutubeSearch
from search_engine_parser import GoogleSearch


from urllib.parse import quote
import requests
from telethon import Button, custom, events, functions
from youtubesearchpython import VideosSearch


from pornhub_api import PornhubApi





    
@tgbot.on(events.InlineQuery(pattern=r"ph (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    if event.query.user_id != bot.uid:
        resultm = builder.article(
            title="- NIKAL LAWDE -",
            text=f"You Can't Use This Bot. \nDeploy LEGEND BOTTo Get Your Own BOT Repo Link HERE",
        )
        await event.answer([resultm])
        return
    results = []
    input_str = event.pattern_match.group(1)
    api = PornhubApi()
    data = api.search.search(
    input_str,
    ordering="mostviewed"
    )
    ok = 1
    oik = ""
    for vid in data.videos:
      if ok <= 5:
        lul_m = (f"PORN-HUB SEARCH \nVideo title : {vid.title} \nVideo link : https://www.pornhub.com/view_video.php?viewkey={vid.video_id}")
        results.append(
                await event.builder.article(
                    title=vid.title,
                    text=lul_m,
                    buttons=[
                        Button.switch_inline(
                            "Search Again", query="ph ", same_peer=True
                        )
                    ],
                )
            )
      else:
        pass
    await event.answer(results)
