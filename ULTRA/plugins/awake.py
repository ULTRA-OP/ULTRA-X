# made by madboy482 for ULTRA-X
# don't kang lawde

import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from ULTRA import ALIVE_NAME, StartTime, CMD_HELP
# from . import legend
from ULTRAX import BOT, PHOTO, VERSION
from ULTRA.utils import admin_cmd, sudo_cmd
from math import ceil
import json
import random
import re
from telethon import events, errors, custom, __version__
import io
from platform import python_version, uname
from ..data.alive_db import get_img

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"

global ok
ok = bot.uid
edit_time = 5
""" =======================CONSTANTS====================== """
pic1 = "https://telegra.ph/file/56a4edc9a37877693d90b.jpg"
pic2 = "https://telegra.ph/file/41e40f117705809616c78.jpg"
pic3 = "https://telegra.ph/file/0d70a9c518b18edac8a54.jpg"
pic4 = "https://telegra.ph/file/7d4b0aae7bc7d881db9ef.jpg"
""" =======================CONSTANTS====================== """


@bot.on(admin_cmd(pattern=r"awake"))
@bot.on(sudo_cmd(pattern=r"awake", allow_sudo=True))
async def hmm(fuk):
    chat = await fuk.get_chat()
    global ok
    ok = bot.uid
    await fuk.delete()
    tele_version = __version__
    ALIVE_MESSAGE = f"** ~~ UʟᴛʀᴀX ɪs Uᴘ ᴀɴᴅ Rᴜɴɴɪɴɢ Sᴜᴄᴄᴇssғᴜʟʟʏ ~~ **\n\n"
    ALIVE_MESSAGE += f"✘ 𝘼𝙗𝙤𝙪𝙩 𝙈𝙤𝙞 𝙎𝙮𝙨𝙩𝙚𝙢 𝙖𝙣𝙙 𝙋𝙚𝙧𝙛𝙤𝙧𝙢𝙖𝙣𝙘𝙚 ✘\n\n"
    ALIVE_MESSAGE += f"➥ **𝑻𝒆𝒍𝒆𝒕𝒉𝒐𝒏 𝑽𝒆𝒓𝒔𝒊𝒐𝒏 :** `{tele_version}`\n"
    ALIVE_MESSAGE += f"➥ **𝑼𝒍𝒕𝒓𝒂𝑿 𝑽𝒆𝒓𝒔𝒊𝒐𝒏 :** `{VERSION}`\n"
    ALIVE_MESSAGE += f"➥ **𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑮𝒓𝒐𝒖𝒑 :** [𝐔𝐥𝐭𝐫𝐚𝐗 𝐂𝐡𝐚𝐭](https://t.me/ULTRAXCHAT)\n\n"
    ALIVE_MESSAGE += f"➥ **𝑫𝒆𝒑𝒍𝒐𝒚 :** [𝐅𝐫𝐨𝐦 𝐇𝐞𝐫𝐞](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU)\n\n"
    ALIVE_MESSAGE += f"➥ **𝑴𝒐𝒊 𝑩𝒐𝒔𝒔 :** [{DEFAULTUSER}](tg://user?id={ok})\n"
    ultra = await bot.send_file(fuk.chat_id, file=get_img(),caption=ALIVE_MESSAGE)

    await asyncio.sleep(edit_time)
    ultrax = await bot.edit_message(fuk.chat_id, ultra, file=pic2) 

    await asyncio.sleep(edit_time)
    lejhand = await bot.edit_message(fuk.chat_id, ultrax, file=pic3)

    await asyncio.sleep(edit_time)
    lejhandx = await bot.edit_message(fuk.chat_id, lejhand, file=pic1)
    
    await asyncio.sleep(edit_time)
    madboy = await bot.edit_message(fuk.chat_id, lejhandx, file=pic3)
    
    await asyncio.sleep(edit_time)
    madboyx = await bot.edit_message(fuk.chat_id, madboy, file=pic2)
    
    await asyncio.sleep(edit_time)
    proboy = await bot.edit_message(fuk.chat_id, madboyx, file=pic1)
    
    await asyncio.sleep(edit_time)
    proboyx = await bot.edit_message(fuk.chat_id, proboy, file=pic4)
    await asyncio.speep(5)
    LEGENDX = await bot.edit_message(fuk.chat_id, proboyx, file=get_img())


# made by madboy482 for ULTRA-X
# don't kang lawde
