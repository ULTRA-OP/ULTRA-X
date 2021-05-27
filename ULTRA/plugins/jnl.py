# made by madboy482
# UltraX
# kang mat kr lawde

import os
import re
from telethon import events, Button, custom
from ULTRAX import ID
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions

@tgbot.on(events.InlineQuery(pattern=r"jnl"))
async def inline_id_handler(event: events.InlineQuery.Event):
 MADBOY = event.builder
 MB = [[custom.Button.inline("⁂⁂ Cʟɪᴄᴋ Hᴇʀᴇ ⁂⁂",data="jnl")]] 
 query = event.text 
 result = MADBOY.article("MADBOY",text="**Cʟɪᴄᴋ Bᴇʟᴏᴡ**",buttons=MB,link_preview=False)
 await event.answer([result])

from telethon import Button, custom, events
import os, re, sys, asyncio
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'jnl'))) 
async def restart(event):
  await event.edit("**Jᴀᴀ Nᴀ Lᴀᴡᴅᴇ, Aᴘɴᴀ Kᴀᴀᴍ Kᴀʀ**")
  await asyncio.sleep(2)
  await event.edit("**!.! Bʜᴏsᴅɪᴋᴇ, Mᴅᴄ, Mᴀᴄᴄʜᴀʀ ᴋɪ Jʜᴀɴᴛ, Mᴀ ᴋᴀ Bʜᴀʀᴏsᴀ Cʜᴀᴅᴀʀᴍᴏᴅ, Kᴜᴛᴛᴇ ᴋᴇ Mᴜᴛʜ, Bsᴅᴋ !.!**")
  await asyncio.sleep(2)
  await event.edit("**Tᴜ Sᴀʟʟᴀ Aᴠɪ Bʜɪ Yᴀʜᴀɴ Dᴇᴋʜ Rʜᴀ Hᴀɪ, Nɪᴋᴀʟ Nᴀ Cʜᴀᴅᴀʀᴍᴏᴅ**\n\n**JNL**")
  os.execl(sys.executable, sys.executable, *sys.argv)
  
# kang mat kr lawde
# UltraX
# made by madboy482
