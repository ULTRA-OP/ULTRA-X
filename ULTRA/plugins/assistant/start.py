from ULTRA import tbot, bot
from telethon import events, Button

@tbot.on(events.NewMessage(pattern="^/start"))
async def startass(e):
  k = bot.me.id
  if e.is_group:
     return
  if e.sender_id = k:
   await e.reply('Hello Master I am Alive and Awake')
  else:
   buttons=[[
                    Button.url("Deploy Ultra-X", "https://github.com/Ultra-OP/Ultra-X"),
                    Button.url("Visit Support", "t.me/UltraXChat"),
                ]]
   caption = "Hello Im Ultra-X Bot Assistant, Deploy Your Own Ultra-X Bot to Unleash My Full Potential"
   await tbot.send_message(e.chat_id, caption, buttons=buttons)
