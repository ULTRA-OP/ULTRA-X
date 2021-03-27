from ULTRA import tbot
from telethon import events
from ULTRA import StartTime
from ULTRA.events import get_readable_time
import time
import datetime

@tbot.on(events.NewMessage(pattern="/ping"))
async def ok(event):
    start_time = datetime.datetime.now()
    message = await event.reply("Pinging_")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "PONG !\n"
        "<b>Time Taken:</b> <code>{}</code>\n"
        "<b>Service uptime:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )
