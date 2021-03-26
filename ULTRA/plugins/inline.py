# COPYRIGHT (C) BY 2021 BY ULTRA X

from telethon import events, Button, custom
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"restart"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGEND = event.builder
 X= [[custom.Button.inline("🔥 RESTART 🔥",data="restart")]]
 query = event.text
 result = LEGEND.article("LEGEND",text="REPO AND SUPPORT",buttons=X,link_preview=False)
 await event.answer([result])

from telethon import Button, custom, events
import os, re, sys, asyncio
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'restart')))
async def restart(event):
  if event.sender_id == bot.me.id:
    await event.edit("restarting your bot please wait")
    await asyncio.sleep(2)
    await event.edit("restarting......")
    await asyncio.sleep(2)
    await event.edit("restarted your bot succesfully")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit ()
  else:
    pro = "ρℓєαѕє ∂єρℓσу уσυ σωη υℓтяα χ υѕєявσт"
    await event.answer(pro, alert=True)
