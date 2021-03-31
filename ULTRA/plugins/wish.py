# made by @Alain_Champion and TEAMLEGEND
# Credites :- @LEGENDX22 , @PROBOYX
# if you kang this please keep credits

# SPECIES THANKS TEAMLEGEND

import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import CMD_HELP
from userbot import bot
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
import io
from platform import python_version, uname
@bot.on(admin_cmd(pattern="wish ?(.*)"))
async def LEGENDBOT(event):
    LEGENDX = event.pattern_match.group(1)
    PROBOY = random.randint(0, 100)
    if LEGENDX:
        reslt = f'''🦋 Yᴏᴜʀ ᴡɪsʜ ʜᴀs ʙᴇᴇɴ ᴄᴀsᴛᴇᴅ 🦋\n\n\n☘️ 𝐘𝐨𝐮𝐫 𝐖𝐢𝐬𝐡 ➪ **`{LEGENDX}`** ✨
              \n\n🔥𝙲𝙷𝙰𝙽𝙲𝙴 𝙾𝙵 𝚂𝚄𝙲𝙲𝙴𝚂𝚂 : **{PROBOY}%**'''
    else:
        if event.is_reply:
            reslt = f"🦋 Yᴏᴜʀ ᴡɪsʜ ʜᴀs ʙᴇᴇɴ ᴄᴀsᴛᴇᴅ 🦋\
                 \n\n🔥𝙲𝙷𝙰𝙽𝙲𝙴 𝙾𝙵 𝚂𝚄𝙲𝙲𝙴𝚂𝚂 : {PROBOY}%"
        else:
            result = f"🦋 Yᴏᴜʀ ᴡɪsʜ ʜᴀs ʙᴇᴇɴ ᴄᴀsᴛᴇᴅ 🦋\
                  \n\n🔥𝙲𝙷𝙰𝙽𝙲𝙴 𝙾𝙵 𝚂𝚄𝙲𝙲𝙴𝚂𝚂 : {PROBOY}%"
    await edit_or_reply(event, reslt)

CMD_HELP.update(
    {
        "wish": "**Plugin : **`wish`\
    \n\n**Syntax : **`.wish <your wish>`\
    \n**Function : **wish plug-in like .wish i am pro"
    }
)

