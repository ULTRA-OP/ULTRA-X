

Betichod = "RoseLoverX"
from telethon import events, Button, custom
from ULTRA import bot, tbot
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 DEVIL = event.builder
 X= [[custom.Button.inline("🔥 CLICK ME 🔥",data="obhai")]]
 query = event.text
 result = DEVIL.article("DEVIL",text="REPO AND SUPPORT",buttons=X,link_preview=False)
 await event.answer([result])
@tbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):

# inline by LEGENDX22 and PROBOYX 🔥 and Betichod
  await event.edit(text=f"ULTRA-X Repo and Group link",buttons=[[Button.url(f"ULTRA-X REPO", url="https://github.com/ULTRA-OP/ULTRA-X"), Button.url(f"ULTRA-X SUPPORT", url="https://t.me/ULTRAXCHAT")]])
