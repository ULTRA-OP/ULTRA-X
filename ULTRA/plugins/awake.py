
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
  ALIVE_MESSAGE = f"**(☞ ಠ_ಠ)☞ {BOT} IS UP AND RUNNING SUCCESSFULLY (☞ ಠ_ಠ)☞**"
  ALIVE_MESSAGE += "\n\n"
  ALIVE_MESSAGE += "**(☞^o^) ☞ 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂 (☞^o^) ☞**\n\n"
  ALIVE_MESSAGE += "(*❛‿❛)→ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 : `{__version__}`\n\n"
  ALIVE_MESSAGE += f"ᕙ( ͡◉ ͜ ʖ ͡◉)ᕗ 𝚄𝙻𝚃𝚁𝙰 𝚇 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 : `{VERSION}`\n\n"
  ALIVE_MESSAGE += f"(｡•̀ᴗ-)✧ 𝙼𝚈 𝙱𝙾𝚂𝚂 : [{DEFAULTUSER}](tg://user?id={tag})\n\n"
  ALIVE_MESSAGE += "(◠‿◕) 𝙶𝚁𝙾𝚄𝙿 : [SUPPORT](https://t.me/ULTRAXOT)\n\n"
  ALIVE_MESSAGE += f"｡◕‿◕｡ [𝙳𝙴𝙿𝙻𝙾𝚈](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FULTRA-OP%2HEROKU) 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙾𝙿 [{BOT}](http://github.com/ULTRA-OP/ULTRA-X) ✧\n"   
  await awake.delete() 
  await borg.send_file(awake.chat_id, PHOTO,caption=ALIVE_MESSAGE)
CMD_HELP.update(
    {
        "awake": "Plugin : awake\
    \n\nSyntax : .awake\
    \nFunction : you can set here costom alive pic .setimg (Telegraph link)"
    }
)
