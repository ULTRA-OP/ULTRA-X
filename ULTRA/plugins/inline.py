# COPYRIGHT (C) BY 2021 BY ULTRA X
# make by @LEGENDX22
# inline alive
# modify by PROBOYX
# master and assistant button by madboy482

import asyncio
import os
from telethon import __version__
from ULTRAX import BOT, PHOTO, VERSION, MSG
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom
from ULTRA.utils import admin_cmd
from ULTRA import ALIVE_NAME
from ULTRA import bot as ultra, SUDO_USERS as sudos
from telethon import Button, custom
from telethon.tl.types import ChannelParticipantsAdmins
global ok
ok = ultra.uid
from ULTRA.utils import admin_cmd, sudo_cmd
from PIL import Image
import requests
from io import BytesIO
from ..data.alive_db import *
from ..data.sudo_db import *
from ..data.dev_db import check_dev
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"
ALIVE_PHOTTO = PHOTO
TG_BOT_USER_NAME_BF_HER = os.environ.get("ALIVE_PHOTTO", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        MSG = await get_text()
        sudo = await all_sudo()
        if sudo:
          SUDO = True
        else:
          SUDO = False
        if await check_dev() == "True":
          DEV = True
        else:
          DEV = False
        pro_text = f"""
**✘ {BOT} ιѕ ση ƒιяє✘**

┏━━━━━━━━━━━━━━━━━━━━━
**{MSG}**
┗━━━━━━━━━━━━━━━━━━━━━
🔥 ✘ αвσυт му ѕуѕтєм ✘ 🔥

➥ **✘Tᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ✘** : {__version__}

➥ **✘Mʏ ᴍᴀsᴛᴇʀ✘** : [{DEFAULTUSER}](tg://user?id={ok})
➥ **✘Sᴜᴅᴏ✘**  : **{SUDO}**
➥ **✘ɪ ᴀᴍ ᴅᴇᴠ✘**: **{DEV}**"""
        ALIVE_PHOTTO = await get_img()
        result = None
        query = event.text
        me = await bot.get_me()
        x = await xbot.get_me() 
        if query.startswith("alive") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{me.username}"),
                    Button.url("Assɪsᴛᴀɴᴛ", f"https://t.me/{x.username}")
                ]
            ]
            buttons += [[custom.Button.inline("Hᴇʟᴘ", data="open"), custom.Button.inline("Rᴇsᴛᴀʀᴛ", data='restart')]]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO.endswith(("mp4", "gif")):
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="υℓтяα χ",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="υℓтяα χ",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)



from ULTRA import bot 
import os
from . import *
@bot.on(admin_cmd("pmimg"))
@bot.on(sudo_cmd("pmimg"))
async def fuk():
  k = event.text.split(" ", 1)[1]
  await pm_img(k)
  await event.edit("updated successfully")

@bot.on(admin_cmd("pmtext"))
@bot.on(sudo_cmd("pmtext"))
async def fuck():
  k = event.text.split(" ", 1)[1]
  await pm_text(k)
  await event.edit("updated successfully")

@bot.on(admin_cmd('setimg'))
@bot.on(sudo_cmd(pattern='setimg', allow_sudo=True))
async def setimgs(event):
  try:
    text = event.text.split(" ", 1)[1]
    await add_img(text)
    await eor(event, f'The Alive Image is updated now Alive image is {text} type `.alive` or `.awake`', link_preview=False)
  except:
    await eor(event, "please give right link ex: `.setimg <img link>` (without brackets)")

@bot.on(admin_cmd('settext'))
@bot.on(sudo_cmd(pattern='settext', allow_sudo=True))
async def settexts(event):
  try:
    text = event.text.split(" ", 1)[1]
    await add_text(text)
    await eor(event, f'The Alive Text is updated now Alive Text is {text} \ntype `.alive` to see your new text', link_preview=False)
  except:
    await eor(event, "please give right text ex: `.settext <text>")


@bot.on(admin_cmd("alive"))
@bot.on(sudo_cmd(pattern="alive", allow_sudo=True))
async def repo(event):
    if event.fwd_from:
        return
    ULTRAX = Var.TG_BOT_USER_NAME_BF_HER
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(ULTRAX, "alive")
    await response[0].click(event.chat_id)
    await event.delete()
from ULTRA.utils import admin_cmd
@bot.on(admin_cmd(pattern="help"))
@bot.on(sudo_cmd(pattern='help',allow_sudo=True))
async def repo(event):
  try:
    LEGENDX = Var.TG_BOT_USER_NAME_BF_HER
    response = await bot.inline_query(LEGENDX, "Userbot")
    await response[0].click(event.chat_id)
    await event.delete()
  except:
    await eor(event, f'**Error In Helper - Check inline please\nbot username: ({(await xbot.get_me()).username})\nheroku: ({LEGENDX})')
@bot.on(admin_cmd(pattern="restart"))
@bot.on(sudo_cmd(pattern='restart', allow_sudo=True))
async def repo(event):
    if event.fwd_from:
        return
    LEGENDX = Var.TG_BOT_USER_NAME_BF_HER
    response = await bot.inline_query(LEGENDX, "restart")
    await response[0].click(event.chat_id)
    await event.delete()

from ..utils import admin_cmd
@bot.on(admin_cmd(pattern="wspr"))
async def wisper(event):
    if event.fwd_from:
        return
    await event.delete()
    PROBOYX = event.text[5:]
    LEGENDX = Var.TG_BOT_USER_NAME_BF_HER
    response = await bot.inline_query(LEGENDX, "wspr " + PROBOYX)
    await response[0].click(event.chat_id)
    


from telethon import events, Button, custom
import os,re
from ULTRAX import ID
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"restart"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGEND = event.builder
 X = [[custom.Button.inline("⁂⁂ 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 ⁂⁂",data="restart")]] #RESTART
 query = event.text #PROBOYX 
 result = LEGEND.article("LEGEND",text="**Cʟɪᴄᴋ Rᴇsᴛᴀʀᴛ Tᴏ Rᴇsᴛᴀʀᴛ Yᴏᴜʀ Bᴏᴛ**",buttons=X,link_preview=False)
 await event.answer([result]) #LEGENDX

from telethon import Button, custom, events
import os, re, sys, asyncio
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'restart'))) # PROBOYX
async def restart(event):
  if event.sender_id == bot.me.id or event.sender_id == ID or event.sender_id in sudos:
    await event.edit("**Rᴇsᴛᴀʀᴛɪɴɢ Bᴏᴛ\nPʟᴇᴀsᴇ ᴡᴀɪᴛ**")
    await asyncio.sleep(2)
    await event.edit("**Rᴇsᴛᴀʀᴛɪɴɢ ᴛʜᴇ Hᴇʀᴏᴋᴜ Cᴏɴɴᴇᴄᴛɪᴏɴ.....**")
    await asyncio.sleep(1)
    await event.edit("**Rᴇsᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ**\n✅✅")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit ()#OP
  else:
    pro = "Eeh, go and get your own UltraX you noob kiddo"
    await event.answer(pro, alert=True)
