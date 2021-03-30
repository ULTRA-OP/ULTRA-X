
from telethon import events, Button, custom
from ULTRA import bot
from ULTRAX import xbot
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@xbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGENDX = event.builder
 X= [[custom.Button.inline("🔥 CLICK ME 🔥",data="obhai")]]
 query = event.text
 result = LEGENDX.article("ULTRA X",text="REPO AND SUPPORT",buttons=X,link_preview=False)
 await event.answer([result])
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):
# inline by TEAMLEGEND, TEAMULTRAx
  await event.edit(text=f"ULTRA-X Repo and Group link",buttons=[[Button.url(f"ULTRA-X REPO", url="https://github.com/ULTRA-OP/ULTRA-X"), Button.url(f"ULTRA-X SUPPORT", url="https://t.me/ULTRAXCHAT")]])
