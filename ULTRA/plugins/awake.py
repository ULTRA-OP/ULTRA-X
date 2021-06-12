
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from ULTRA import ALIVE_NAME, StartTime, CMD_HELP
#from . import legend
from ULTRAX import BOT, PHOTO, VERSION
from ULTRA.utils import admin_cmd, sudo_cmd
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname
from ..data.alive_db import add_img, get_img
from telethon import __version__
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"

        
#make by LEGEND X bht mehnat lag gayi yrr but banhi gaya 😅 
#so credits ke sath kang krna, nhi to tum jante ho apna bhai DMCA hai 🙂😁
#modify by madboy482
@borg.on(admin_cmd(pattern=r"awake"))
@bot.on(sudo_cmd(pattern=r"awake", allow_sudo=True))
async def amireallyalive(awake):
  tag = borg.uid
  PHOTO = await get_img()
  ALIVE_MESSAGE = f'''
        {BOT} ɪs ᴏɴʟɪɴᴇ

         Sʏsᴛᴇᴍ sᴛᴀᴛᴜs
(*❛‿❛)→ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ »»» `{__version__}`
ᕙ( ͡◉ ͜ ʖ ͡◉)ᕗ ʙᴏᴛ ᴠᴇʀsɪᴏɴ »»» `{VERSION}`\n\n
(｡•̀ᴗ-)✧ ᴍʏ ʙᴏss »»» [{DEFAULTUSER}](tg://user?id={tag})
(◠‿◕) sᴜᴘᴘᴏʀᴛ »»» [SUPPORT](https://t.me/ULTRAXCHAT)
｡◕‿◕｡ [ᴅᴇᴘʟᴏʏ](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FULTRA-OP%2HEROKU) ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ [{BOT}](http://github.com/ULTRA-OP/ULTRA-X) '''

  await awake.delete() 
  await borg.send_file(awake.chat_id, PHOTO,caption=ALIVE_MESSAGE)
CMD_HELP.update(
    {
        "awake": "Plugin : awake\
    \n\nSyntax : .awake\
    \nFunction : you can set here costom alive pic .setimg (Telegraph link)"
    }
)
