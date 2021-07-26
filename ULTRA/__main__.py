import os, sys
try:
  from LEGENDX import id, ID, devs, rd, wt
except:
  os.system("pip install LEGENDX==0.0.21")
  from LEGENDX import id, ID, devs
finally:
  print ("ULTRA X IS STARTING WITH TELETHON") 
from ULTRAX import xbot
from ULTRA import bot, CMD_HELP
from sys import argv
os.system("pip install telethon==1.20")
import sys
import heroku3
import os
from ULTRA import bot
from telethon import events
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from ULTRA.utils import command, remove_plugin, load_module
from var import Var
from pathlib import Path
from ULTRA import LOAD_PLUG
import sys
import asyncio
import traceback
import os
import ULTRA.utils
from telethon.tl.functions.messages import CreateChatRequest as ccr, EditChatPhotoRequest as af
os.system("pip install google_trans_new")
import glob
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient, Button
from var import Var
from ULTRA.utils import load_module, load_pro
from ULTRA import LOAD_PLUG, BOTLOG_CHATID
from pathlib import Path
import asyncio
TOKEN = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
import telethon.utils
from .data.alive_db import get_grp, add_grp
EXTRA_PLUGS = os.environ.get("EXTRA_PLUGS", False)
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.username = bot.me.username or None
    bot.id = bot.me.id
    bot.uid = telethon.utils.get_peer_id(bot.me)
ONLINE_ALERT = os.environ.get("ONLINE_ALERT")
os.system("pip install LEGENDX==0.0.21")
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "UltraXOp",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

import glob


bot.set(heroku_username=Var.TG_BOT_USER_NAME_BF_HER)
path = 'ULTRA/plugins/assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_pro(shortname.replace(".py", ""))


if  EXTRA_PLUGS == True:
    os.system("git clone https://github.com/ULTRA-OP/ULTRA_PLUGS.git ./ULTRA/plugins/")
    path = "ULTRA/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            try:
                load_module(plugin_name.replace(".py", ""))
                if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                    print ('INSTALLING ALL MODULES', plugin_name)
            except:
                pass

else:
  path = 'ULTRA/plugins/*.py'
  files = glob.glob(path)
  for name in files:
      with open(name) as f:
          path1 = Path(f.name)
          shortname = path1.stem
          load_module(shortname.replace(".py", ""))


async def install():
    i =0
    chat = Var.PLUGIN_CHANNEL
    documentss = await bot.get_messages(chat, None , filter=InputMessagesFilterDocument)
    total = int(documentss.total)
    total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await bot.download_media(await bot.get_messages(chat, ids=mxo), "ULTRA/plugins/")
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            print(f'{i} plugin install')
        else:
            print ("Failed")
import ULTRA._core
import os
print("UltraX is Up and Awake! ©️ TeamUltraX 2021")
async def legend():
  pro = await xbot.get_me()
  legend = await bot.get_me()
  LEGENDX = f"""
**Sᴏᴍᴇᴛʜɪɴɢ Hᴀᴘᴘᴇɴᴇᴅ ! Lᴇᴛs Cʜᴇᴄᴋ** 🤔 

`☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎`

**Dɪɴɢ Dᴏɴɢ...** `.\./.\` **Tɪɴɢ Tᴏɴɢ...** `./.\./` **UʟᴛʀᴀX Hᴀs Bᴇᴇɴ Dᴇᴘʟᴏʏᴇᴅ !!**

**Pɪɴɢ Pᴏɴɢ...**

**➥ Mᴀsᴛᴇʀ** `➪` **@{legend.username}**
**➥ Assɪsᴛᴀɴᴛ** `➪` **@{pro.username}**
**➥ Sᴜᴘᴘᴏʀᴛ** `➪` **@UltraXchaT**
**➥ Cʜᴀɴɴᴇʟ** `➪` **@UltraX_SupporT**

**Cʜᴇᴄᴋ ᴍᴏɪ Pɪɴɢ ᴛɪᴍᴇ ʙʏ** `.ping` **[Fᴏʀ UsᴇʀBᴏᴛ] or** `/ping` **[Fᴏʀ Assɪsᴛᴀɴᴛ]**
"""
  if ONLINE_ALERT:
    try:
      PROBOYX = [[Button.inline("Hᴇʀᴏᴋᴜ Vᴀʀs", data='ass_back')]]
      
      await xbot.send_message(bot.me.id, LEGENDX, buttons=PROBOYX)
    except:
       pass
  else:
      print("YOUR BOT DEPLOYED SUCCESSFULLY")

async def danger(username):
  i = 0
  xx = 0
  async for x in bot.iter_dialogs():
    if x.is_group or x.is_channel:
     try:
       await bot.edit_permissions(x.id, username, view_messages=False)
       i += 1
     except:
       xx += 1
  print(f"THE DANGER USER WAS BANNED IN {i-xx}")

async def setgrp():
  bot.set(bot_username=(await xbot.get_me()).username)
  k = await get_grp()
  if k:
    return print ('Private Group already setted')
  print ("Setting groups wait A min")
  mybot = (await xbot.get_me()).username
  r = await bot(ccr(users=[mybot], title='Ultra X Private Group'))
  await add_grp(r.chats[0].id)
  id = r.chats[0].id
  await bot (af(chat_id=id, photo=await bot.upload_file("IMG_20210614_135000_452.jpg"))) 
  await bot.edit_admin(id, mybot, is_admin=True, anonymous=False, title="UltraXbot")
  heroku_conn = heroku3.from_key(Var.HEROKU_API_KEY)
  k = heroku_conn.apps()[Var.HEROKU_APP_NAME]
  vars = {
    "FBAN_GROUP_ID": id,
    "PM_LOGGR_BOT_API_ID" : id,
    "PRIVATE_GROUP_BOT_API_ID": id,
    "G_BAN_LOGGER_GROUP": id,
    "PM_PERMIT_GROUP_ID": id
    }
  k.update_config(vars)
  print ("Successfully Added group")

bot.loop.run_until_complete(setgrp())
#bot.loop.run_until_complete(danger("")) # Temporary
bot.loop.run_until_complete(legend())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
    
else:
    bot.run_until_disconnected()
    
import ULTRA.end
