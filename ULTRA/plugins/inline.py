# COPYRIGHT (C) BY 2021 BY ULTRA X

from telethon import events, Button, custom
import os,re
from ULTRAX import ID
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"restart"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGEND = event.builder
 X = [[custom.Button.inline("⁂⁂ 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 ⁂⁂",data="restart")]] #RESTART
 query = event.text #PROBOYX 
 result = LEGEND.article("LEGEND",text="**Cʟɪᴄᴋ Rᴇsᴛᴀʀᴛ Tᴏ Rᴇsᴛᴀʀᴛ Yᴏᴜʀ Bᴏᴛ**",buttons=X,link_preview=False)
 await event.answer([result]) #LEGENDX

from telethon import Button, custom, events
import os, re, sys, asyncio
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'restart'))) # PROBOYX
async def restart(event):
  if event.sender_id == bot.me.id or event.sender_id == ID:
    await event.edit("**Yᴀ ᴡᴀɪᴛ....Yᴏᴜʀ ʙᴏᴛ ɪs ʙᴇɪɴɢ ʀᴇsᴛᴀʀᴛᴇᴅ...\nPʟᴇᴀsᴇ ᴡᴀɪᴛ**")
    await asyncio.sleep(2)
    await event.edit("**Rᴇsᴛᴀʀᴛɪɴɢ ᴛʜᴇ Hᴇʀᴏᴋᴜ Cᴏɴɴᴇᴄᴛɪᴏɴ.....**")
    await asyncio.sleep(2)
    await event.edit("**Yᴀʏ!! Rᴇsᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ**\n✅✅")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit ()#OP
  else:
    pro = "ρℓєαѕє ∂єρℓσу уσυ σωη υℓтяα χ υѕєявσт"
    await event.answer(pro, alert=True)
