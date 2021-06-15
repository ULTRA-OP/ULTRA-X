# © By Team Legend, Team UltraX, Alain
import re, os
from telethon import events, Button, custom
import os,re
from . import ID
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
from ULTRA.utils import admin_cmd
from ULTRA import CMD_HELP

kk = bot.me.first_name
last = bot.me.last_name
pro = bot.uid
boy = bot.me.bot
lol = bot.me.username
hmm = bot.me.restricted
h = bot.me.verified
hm = bot.me.access_hash
scam = bot.me.scam
dele = bot.me.deleted
bc = bot.me.id

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'ass_info')))
async def restart(event):
    if event.sender_id == bot.me.id or event.sender_id == ID:
       await event.edit("Wᴇɪᴛ Mᴀsᴛᴇʀ Sᴇɴᴅɪɴɢ Yᴏᴜʀ Iɴғᴏ")
       await xbot.send_message(pro,  f"**👤 Your details By υℓтяα χ 👤**\n\n**➥ Fɪʀsᴛ Nᴀᴍᴇ**: `{kk}`\n\n**➥ Lᴀsᴛ Nᴀᴍᴇ:** `{last}`\n\n**➥ Usᴇʀ Iᴅ:** `{bc}`\n\n**➥ Bᴏᴛ:** `{boy}`\n\n**➥ Usᴇʀɴᴀᴍᴇ:** @{lol}\n\n**➥ Rᴇsᴛʀɪᴄᴛᴇᴅ:** `{hmm}`\n\n**➥ Vᴇʀɪғɪᴇᴅ:** `{h}`\n\n**➥ Aᴄᴄᴇss Hᴀsʜ:** `{hm}`\n\n**➥ Sᴄᴀᴍ:** `{scam}`\n\n**➥ Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛ:** `{dele}`")
       await event.edit("Successfully Sent Your Info Through Your Assistant")
    else:
       jnl = "Heyy you, Yes you\nWhy u kiddo want to see moi info??\nGo away and mind your own bizness"
       await event.answer(jnl, alert=True)

@xbot.on(events.InlineQuery(pattern=r"me"))
async def inline_id_handler(event: events.InlineQuery.Event):
  LEGENDX = event.builder
  X = [[custom.Button.inline("⁂⁂ 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 ⁂⁂",data="ass_info")]]

  X += [[custom.Button.inline("⁂⁂ 𝐂𝐮𝐫𝐫𝐫𝐞𝐧𝐭 𝐂𝐡𝐚𝐭 ⁂⁂",data="ass_chat")]] 
  query = event.text 
  result = LEGENDX.article("υℓтяα χ вσт",text="**Hᴏᴡ ᴡᴏᴜʟᴅ ʏᴏᴜ ʟɪᴋᴇ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɪɴғᴏ !!**\n\n**Assɪsᴛᴀɴᴛ =** `Gᴇᴛ ʏᴏᴜʀ ɪɴғᴏ ᴛʜʀᴏᴜɢʜ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ.`\n\n**Cᴜʀʀᴇɴᴛ Cʜᴀᴛ =** `Sᴇɴᴅ ʏᴏᴜʀ ɪɴғᴏ ɪɴ ᴄᴜʀʀᴇɴᴛ ᴄʜᴀᴛ.`",buttons=X)
  await event.answer([result])
@bot.on(admin_cmd(pattern="me"))
async def me(event):
    if event.fwd_from:
        return
    LEGENDX= Var.TG_BOT_USER_NAME_BF_HER
    if event.reply_to_msg_id:
        await event.get_reply_message()
    PROBOYX = await bot.inline_query(LEGENDX, "me")
    await PROBOYX[0].click(event.chat_id)
    await event.delete()

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'ass_chat')))
async def chat(event):
    if event.sender_id == bot.me.id or event.sender_id == ID:
       await event.edit(f"**👤 Your details By υℓтяα χ 👤**\n\n**➥ Fɪʀsᴛ Nᴀᴍᴇ**: `{kk}`\n\n**➥ Lᴀsᴛ Nᴀᴍᴇ:** `{last}`\n\n**➥ Usᴇʀ Iᴅ:** `{bc}`\n\n**➥ Bᴏᴛ:** `{boy}`\n\n**➥ Usᴇʀɴᴀᴍᴇ:** @{lol}\n\n**➥ Rᴇsᴛʀɪᴄᴛᴇᴅ:** `{hmm}`\n\n**➥ Vᴇʀɪғɪᴇᴅ:** `{h}`\n\n**➥ Aᴄᴄᴇss Hᴀsʜ:** `{hm}`\n\n**➥ Sᴄᴀᴍ:** `{scam}`\n\n**➥ Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛ:** `{dele}`")
    else:
       hehe = "Heyy you, Yes you\nWhy u kiddo want to see moi info??\nGo away and mind your own bizness"
       await event.answer(hehe, alert=True)
        
CMD_HELP.update(
    {
        "me": """**Plugin : **`me`
`.me`
**Function :**  **Get your info through your assistant or current chat!**"""
    }
)
        
