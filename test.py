    
#Credit To @legendx22 . Keep credit if you are going to edit it. Join @LEGEND_USERBOT_SUPPORT


import random, re
from userbot import CMD_HELP
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="test ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
       
        await event.edit("`Testing LEGEND BOT....`")
        await asyncio.sleep(2)
        await event.edit("`Testing LEGEND BOT..`")
        await asyncio.sleep(2)
        await event.edit("__Testing Successful__")
        await asyncio.sleep(2)
        await event.edit("`Making Output` \n\nPlease wait")
        await asyncio.sleep(2)
        await event.edit("__Output Successful__")
        await asyncio.sleep(3.5)
        await event.edit("Your[LEGEND BOT](https:/t.me/hackerget0) is working Fine...\n       Join @teamishere For Any Help......")

CMD_HELP.update(
    {
        "test": "**Plugin : **`test`\
    \n\n**Syntax : **`.test`\
    \n**Function : **this is only plugin for watching"
    }
)
