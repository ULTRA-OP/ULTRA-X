# Copyright 2021-2022 ULTRA X BOT
#made by @legendx22
import asyncio
import os
try:
  from pyrogram import Client, idle
except:
  os.system("pip install pyrogram>=1.1.13")
  from pyrogram import Client, idle

import asyncio
from userbot.utils import admin_cmd 
from userbot import bot as  υℓтяαχ
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
from telethon import events, custom, Button, TelegramClient
import time
from userbot import botnickname, ALIVE_NAME, bot
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
tbot = TelegramClient("ultra", API_ID, API_HASH).start(bot_token=token)
pbot = Client("ULTRA", api_id=API_ID, api_hash=API_HASH, bot_token=token)
BOT = str(botnickname) if botnickname else "υℓтяα χ вσт"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяαχ вσу"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
Ultra = "[υℓтяαχ](https://t.me/UltraXOT)"
VERSION = "3.1.5"
REPO = "[υℓтяα χ вσт](https://github.com/ULTRA-OP/ULTRA-X)"
PRO = bot.uid
MASTER = f"[{NAME}](tg://user?id={PRO})"
GROUP = "[SUPPORT GROUP](https://t.me/UltraXChat)"
if __name__=="__main__":
  tbot.run_until_disconnected()

if __name__=="__main__":
  pbot.start()
