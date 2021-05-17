# made by madboy
# kang mat kr lawde
# UltraX

from telethon import events, Button, custom
from ULTRA import bot
from ULTRAX import xbot
from ULTRA import CMD_HELP

BOT_USERNAME = Var.TG_BOT_USER_NAME_BF_HER

# made by madboy
# kang mat kr lawde
# UltraX

import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
MadBoy = bot.me.first_name
@xbot.on(events.InlineQuery(pattern=r"myself"))
async def inline_id_handler(event: events.InlineQuery.Event):
  MADBOY = event.builder
  MADB= [[custom.Button.inline("🔥 Hᴇʀᴇ 🔥",data="mb")]]
  query = event.text
  result = MADBOY.article("υℓтяα χ",text=f"**υℓтяα χ**",buttons=MADB,link_preview=False)
  await event.answer([result])
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"mb")))
async def callback_query_handler(event):
  await event.edit(text=f"**{MadBoy}**",buttons=[[Button.url(f"⚜️ Cʟɪᴄᴋ Hᴇʀᴇ ⚜️", url="tg://settings")]],
                  )
# made by madboy
# kang mat kr lawde
# UltraX

CMD_HELP.update
(
  {
    "myself": f"**Plugin : **`myself`\
    \n\n**Your info button, but will re-direct to the profile of one who is clicking the button**\
    \n•  **Syntax-1 : **`.myself`\
    \n•  **Syntax-2 : **`@{BOT_USERNAME} myself`\
    "
  }
)
# made by madboy
# kang mat kr lawde
# UltraX
