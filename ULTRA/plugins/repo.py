
from telethon import events, Button, custom
from DaisyX import bot
from Assist.DAISYX import xbot

import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@xbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 
 DAISY = event.builder
 X= [[custom.Button.inline("🔥 Cʟɪᴄᴋ Hᴇʀᴇ 🔥",data="obhai")]]
 query = event.text
 
 result = DAISY.article("ᴅᴀɪsʏX",text="**ᴅᴀɪsʏX's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Sᴜᴘᴘᴏʀᴛ\n\n© @DaisyXOT**",buttons=X,link_preview=False)
 await event.answer([result])
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):
  await event.edit(text=f"**ᴅᴀɪsʏX's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Gʀᴏᴜᴘ Lɪɴᴋ\n\n© @DaisyXOT**",buttons=[
                [
                    Button.url(f"⚜️ Rᴇᴘᴏ ⚜️", url="https://github.com/TeamDaisyX/Daisy-X-UB"),
                    Button.url(f"🌚 Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ 🌝", url="https://t.me/DaisySupport_Official")],
                    [Button.url(f"🔰 Dᴇᴘʟᴏʏ 🔰", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeamDaisyX%2FDaisy-X-UB&template=https%3A%2F%2Fgithub.com%2FTeamDaisyX%2FDaisy-X-UB"),
                     Button.url(f"💠 Sᴛʀɪɴɢ 💠", url="https://replit.com/@legendx22/ULTRA-X#main.py"),
                ]
            ]
                   
                  )
