from ULTRA import tbot, bot
from telethon import events

@tbot.on(events.NewMessage(pattern="^/start"))
async def startass(e):
  k = bot.me.id
  if e.is_group:
     return
  if e.sender_id = k:
   await e.reply('Hello Master I am Alive and Awake')
  else:
   await e.reply('Hello! How can I help Ya')
