from ULTRA import bot, tbot
from sys import argv
import sys
import os
os.system("pip install google_trans_new")
import glob
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from ULTRA.utils import load_module, load_pro
from ULTRA import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
TOKEN = os.environ.get("TG_BOT_TOKEN", None)
import telethon.utils

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()
try:
    tbot.start(bot_token=TOKEN)
except Exception:
    print("Bot Token Invalid Assistant Stopping!")

import glob


path = 'ULTRA/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_pro(shortname.replace(".py", ""))

path = 'ULTRA/plugins/assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_pro(shortname.replace(".py", ""))



import ULTRA._core

print("UltraX is Up and Awake! ©️ TeamUltraX 2021")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
    tbot.disconnect()
else:
    bot.run_until_disconnected()
    tbot.run_until_disconnected()


