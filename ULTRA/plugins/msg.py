

from userbot import bot as borg



import os
import re
import urllib
from math import ceil

import requests
from telethon import Button, custom, events, functions
from youtubesearchpython import SearchVideos




@tgbot.on(events.InlineQuery(pattern=r"tor (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder

    inp = event.pattern_match.group(1)
    if event.query.user_id == bot.uid:
        sn = urllib.parse.quote_plus(inp)
        results = []
        sl = "https://api.sumanjay.cf/torrent/?query=" + sn
        try:
            op = requests.get(url=sl, timeout=10).json()
        except:
            pass
        ed = len(op)
        if  ed == 0:
            resultm = builder.article(
                title="No Result",
                description="Try Again With correct Spelling",
                text="**No Matching Found**",
                buttons=[
                    [
                        Button.switch_inline(
                            "Search Again", query="torrent ", same_peer=True
                        )
                    ],
                ],
            )
            await event.answer([resultm])
            return
        if  ed > 30:
            for i in range(30):
                ds = op[i]["age"]
                ops = op[i]["leecher"]
                ssk = op[i]["magnet"]
                okk = op[i]["name"]
                sizes = op[i]["size"]
                type = op[i]["type"]
                seeders = op[i]["seeder"]
                ok = f"**Title :** `{okk}` \n**Size :** `{sizes}` \n**Type :** `{type}` \n**Seeder :** `{seeders}` \n**Leecher :** `{ops}` \n**Magnet :** `{ssk}` "
                me = f"Size : {sizes} Type : {type} Age : {ds}"
                results.append(
                    await event.builder.article(
                        title=okk,
                        description=me,
                        text=ok,
                        buttons=Button.switch_inline(
                            "Search Again", query="tor ", same_peer=True
                        ),
                    )
                )
        else:
            for dz in op:
                siz = dz["size"]
                typ = dz["type"]
                seede = dz["seeder"]
                ag = dz["age"]
                leech = dz["leecher"]
                mag = dz["magnet"]
                nam = dz["name"]            
                all = f"**Title :** `{nam}` \n**Size :** `{siz}` \n**Type :** `{typ}` \n**Seeder :** `{seede}` \n**Leecher :** `{leech}` \n**Magnet :** `{mag}` "
                mi = f"Size : {siz} Type : {typ} Age : {ag}"
                results.append(
                    await event.builder.article(
                        title=nam,
                        description=mi,
                        text=all,
                        buttons=[
                            Button.switch_inline(
                                "Search Again", query="tor ", same_peer=True
                            )
                        ],
                    )
                )
        await event.answer(results)
    if not event.query.user_id == bot.uid:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/legendx22/LEGEND-BOT ",buttons=[[Button.switch_inline("Search Again", query="tor ", same_peer=True)],], )
        await event.answer([resultm])
        return

@tgbot.on(events.InlineQuery(pattern=r"yt (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput,shivam = event.pattern_match.group(1).split(";")
    urllib.parse.quote_plus(testinput)

    if event.query.user_id == bot.uid:
        results = []
        search = SearchVideos(f"{testinput}", offset=1, mode="dict", max_results=int(shivam))
        mi = search.result()
        moi = mi["search_result"]
        if search == None:
            resultm = builder.article(
                title="No Results.",
                description="Try Again With correct Spelling",
                text="**No Matching Found**",
                buttons=[
                    [Button.switch_inline("Search Again", query="yt ", same_peer=True)],
                ],
            )
            await event.answer([resultm])
            return
        for mio in moi:
            mo = mio["link"]
            thum = mio["title"]
            fridayz = mio["id"]
            thums = mio["channel"]
            td = mio["duration"]
            tw = mio["views"]
            kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
            okayz = f"**Title :** `{thum}` \n**Link :** {mo} \n**Channel :** `{thums}` \n**Views :** `{tw}` \n**Duration :** `{td}`"
            hmmkek = f"Channel : {thums} \nDuration : {td} \nViews : {tw}"
            results.append(
                await event.builder.article(
                    title=thum,
                    description=hmmkek,
                    text=okayz,
                    buttons=Button.switch_inline(
                        "Search Again", query="yt ", same_peer=True
                    ),
                )
            )
        await event.answer(results)

    if not event.query.user_id == bot.uid:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/legendx22/LEGEND-BOT  ",buttons=[[Button.switch_inline("Search Again", query="yt ", same_peer=True)],], )
        await event.answer([resultm])
        return

#

#
