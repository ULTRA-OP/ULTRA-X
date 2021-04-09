# updated by madboy482
# updated by madboy482
# updated by madboy482
from telethon import events, Button, custom
from ULTRA import bot
from ULTRAX import xbot
# updated by madboy482
# updated by madboy482
# updated by madboy482
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@xbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 # updated by madboy482
 # updated by madboy482
 # updated by madboy482
 LEGENDX = event.builder
 X= [[custom.Button.inline("🔥 Cʟɪᴄᴋ Hᴇʀᴇ 🔥",data="obhai")]]
 query = event.text
 # updated by madboy482
 # updated by madboy482
 # updated by madboy482
 result = LEGENDX.article("UʟᴛʀᴀX",text="**UltraX's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Sᴜᴘᴘᴏʀᴛ\n\n© @UltraXOT**",buttons=X,link_preview=False)
 # updated by madboy482
 # updated by madboy482
 # updated by madboy482
 await event.answer([result])
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
# updated by madboy482
# updated by madboy482
# updated by madboy482
async def callback_query_handler(event):
# inline by TEAMLEGEND, TEAMULTRAX
  await event.edit(text=f"**UʟᴛʀᴀX's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Gʀᴏᴜᴘ Lɪɴᴋ\n\n© @UltraXOT**",buttons=[
   # updated by madboy482
   # updated by madboy482
   # updated by madboy482
                [
                    Button.url(f"⚜️ Rᴇᴘᴏ ⚜️", url="https://github.com/ULTRA-OP/ULTRA-X"),
                 # updated by madboy482
                 # updated by madboy482
                 # updated by madboy482
                    Button.url(f"🌚 Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ 🌝", url="https://t.me/ULTRAXCHAT")],
   # updated by madboy482
   # updated by madboy482
   # updated by madboy482
                    [Button.url(f"🔰 Dᴇᴘʟᴏʏ 🔰", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU"),
                ]
            ]
                   # updated by madboy482
                   # updated by madboy482
                   # updated by madboy482
                  )
