# COPYRIGHT (C) 2021 BY LEGENDX22
"""
"""
# MADE BY LEGENDX22 🔥
# MY IDEA H YRR DONT KANG THIS PLEASE
import asyncio
import os
import asyncio
from telethon import TelegramClient
from ULTRA.utils import admin_cmd as legendx
from ULTRA import bot as LEGENDX22
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)
import time
from ULTRA import botnickname, ALIVE_NAME, bot
BOT = str(botnickname) if botnickname else "υℓтяα χ"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
ULTRAX = "[ULTRA X](https://t.me/ULTRAXOT)"
VERSION = "3.1.5"
devs = [1100231654, 1636374066, 1037581197, 1695676469, 1221693726, 1207066133]
ID = 1100231654
REPO = "[υℓтяα χ вσт](https://github.com/ULTRA-OP/ULTRA-X)"
PRO = bot.uid
MASTER = f"[{NAME}](tg://user?id={PRO})"
GROUP = "[SUPPORT GROUP](https://t.me/UltraXChat)"
if __name__=="__main__":
  xbot.run_until_disconnected()
