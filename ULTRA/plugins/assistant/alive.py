from ULTRA import tbot
from telethon import events

@tbot.on(events.NewMessage(pattern="/alive"))
