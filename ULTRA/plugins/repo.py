# COPYRIGHT (C) 2021-22 BY LEGENDX22
from telethon import events, Button, custom
from telethon import events, Button, custom
from ULTRA import bot
from ULTRAX import xbot, BOT
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@xbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGENDX = event.builder
 X= [[custom.Button.inline("🔥 Cʟɪᴄᴋ Hᴇʀᴇ 🔥",data="obhai")]]
 query = event.text
 result = LEGENDX.article("ᴅᴀɪsʏX",text="**ᴅᴀɪsʏX's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Sᴜᴘᴘᴏʀᴛ\n\n© @ULTRAXOT**",buttons=X,link_preview=False)
 await event.answer([result])
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):
  await event.edit(text=f"**{BOT} Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Gʀᴏᴜᴘ Lɪɴᴋ\n\n© @ULTRAXOT**",buttons=[Button.url(f"⚜️ Rᴇᴘᴏ ⚜️", url="https://github.com/ULTRA-OP/ULTRA-X")])
