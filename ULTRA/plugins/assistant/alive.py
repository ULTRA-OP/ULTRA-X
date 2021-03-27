from ULTRA import tbot
from telethon import events

@tbot.on(events.NewMessage(pattern="/alive"))
async def ok(event):
   await event.reply('Not Done')
