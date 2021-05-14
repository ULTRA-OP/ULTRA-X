# COPYRIGHT (C) BY 2021 BY ULTRA X
# made by madboy482
# kang mat kr lawde

import asyncio
import os
import re
import sys
from ULTRAX import ID
import requests
from telethon import events, Button, custom, functions, errors
from ULTRA.utils import admin_cmd, sudo_cmd

@tgbot.on(events.InlineQuery(pattern=r"redeploy"))
async def inline_id_handler(event: events.InlineQuery.Event):
 MADBOY = event.builder
 MB = [[custom.Button.inline("⁂⁂ 𝑹𝒆𝒅𝒆𝒑𝒍𝒐𝒚 ⁂⁂",data="redeploy")]] #REDEPLOY
 query = event.text # MADBOY482
 result = MADBOY.article("MADBOY",text="**Cʟɪᴄᴋ RᴇDᴇᴘʟᴏʏ Tᴏ RᴇDᴇᴘʟᴏʏ Yᴏᴜʀ Bᴏᴛ**",buttons=MB,link_preview=False)
 await event.answer([result]) # MADBOY482

from telethon import Button, custom, events
import os, re, sys, asyncio
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'redeploy'))) # MADBOY482
async def restart(event):
  if event.sender_id == bot.me.id or event.sender_id == ID:
    await event.edit("**Pʟᴇᴀsᴇ Wᴀɪᴛ**")
    await asyncio.sleep(2)
    await event.edit("**RᴇDᴇᴘʟᴏʏɪɴɢ Tʜᴇ Hᴇʀᴏᴋᴜ Cᴏɴɴᴇᴄᴛɪᴏɴ.....**")
    await asyncio.sleep(1)
    await event.edit("**RᴇDᴇᴘʟᴏʏᴇᴅ Yᴏᴜʀ Bᴏᴛ Sᴜᴄᴄᴇssғᴜʟʟʏ**\n✅✅")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit () # MADBOY482
  else:
    mad = "Eeh, go and get your own UltraX you noob kiddo"
    await event.answer(mad, alert=True)
