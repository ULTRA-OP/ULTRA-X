# Copyright (C) 2021 By Team UltraX 

# ~ LegendX
# ~ ProBoyX
# ~ Alain
# ~ MadBoy
# ~ RoseLoverX

# modify by madboy482

# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA

# Kang with Credits, else gey
# I knew u will kang and remove credits, duffer!!

# back click kar madharchod 

# Last Warn - Undo the removed part else be ready for DMCA by LegendX
# Mobile me back option he uspe click karde madhachod kang kiya to dekh

# Pls kang mat krna pyar se bol rha hu, nhi to DMCA hai

# code starting...
import re, os
from telethon import events, Button, custom
import os,re
from ULTRAX import ID
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
from ULTRA.utils import admin_cmd

k = bot.me.phone
kk = bot.me.first_name
alain = bot.me.last_name
pro = bot.uid
boy = bot.me.bot
lol = bot.me.username
hmm = bot.me.restricted
h = bot.me.verified
hm = bot.me.access_hash
a = bot.me.photo.dc_id
mad = bot.me.photo.has_video
scam = bot.me.scam
dele = bot.me.deleted

X = [[custom.Button.inline("⁂⁂ Assistant ⁂⁂",data="assistant")]]
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA

# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'assistant'))) # PROBOYX
async def restart(event):
    if event.sender_id == bot.me.id or event.sender_id == ID:
       await event.edit("Wᴇɪᴛ Mᴀsᴛᴇʀ Sᴇɴᴅɪɴɢ Yᴏᴜʀ Iɴғᴏ")
       await xbot.send_message(pro,  f"**➥ Mᴏʙɪʟᴇ:** +{k}\n\n**➥ Fɪʀsᴛ Nᴀᴍᴇ:** {kk}\n\n**➥ Lᴀsᴛ Nᴀᴍᴇ:** {alain}\n\n**➥ Bᴏᴛ:** {boy}\n\n**➥ Usᴇʀɴᴀᴍᴇ:** @{lol}\n\n**➥ Rᴇsᴛʀɪᴄᴛᴇᴅ:** {hmm}\n\n**➥ Vᴇʀɪғɪᴇᴅ:** {h}\n\n**➥ Aᴄᴄᴇss Hᴀsʜ:** {hm}\n\n**➥ Dᴄ Iᴅ:** {a}\n\n**➥ Hᴀᴠᴇ Vɪᴅᴇᴏ Iɴ Pʀᴏғɪʟᴇ:** {mad}\n\n**➥ Sᴄᴀᴍ:** {scam}\n\n**➥ Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛ:** {dele}")
       await event.edit("Successfully Sent Your Info Through Your Assistant")
    else:
       jnl = "Heyy you, Yes you\nWhy tf u want to see moi info??\nGo away and moind your own bizness"
       await event.answer(jnl, alert=True)
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
@tgbot.on(events.InlineQuery(pattern=r"me"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGEND = event.builder
 X = [[custom.Button.inline("⁂⁂ Asssitant ⁂⁂",data="assistant")]] 
 X += [[custom.Button.inline("⁂⁂ Current Chat ⁂⁂",data="chat")]] 
 query = event.text #PROBOYX 
 result = LEGEND.article("LEGEND",text="Hᴏᴡ Wᴏᴜʟᴅ Yᴏᴜ Lɪᴋᴇ Tᴏ Cʜᴇᴄᴋ Yᴏᴜʀ Dᴀᴛᴀ",buttons=X,link_preview=False)
 await event.answer([result]) #LEGENDX
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA

# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
@bot.on(admin_cmd(pattern="me"))
async def me(event):
    if event.fwd_from:
        return
    LEGENDX = Var.TG_BOT_USER_NAME_BF_HER
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(LEGENDX, "me")
    await response[0].click(event.chat_id)
    await event.delete()
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA

# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'chat')))
async def chat(event):
    if event.sender_id == bot.me.id or event.sender_id == ID:
       await event.edit(f"**➥ Mᴏʙɪʟᴇ:** +{k}\n\n**➥ Fɪʀsᴛ Nᴀᴍᴇ:** {kk}\n\n**➥ Lᴀsᴛ Nᴀᴍᴇ:** {alain}\n\n**➥ Bᴏᴛ:** {boy}\n\n**➥ Usᴇʀɴᴀᴍᴇ:** @{lol}\n\n**➥ Rᴇsᴛʀɪᴄᴛᴇᴅ:** {hmm}\n\n**➥ Vᴇʀɪғɪᴇᴅ:** {h}\n\n**➥ Aᴄᴄᴇss Hᴀsʜ:** {hm}\n\n**➥ Dᴄ Iᴅ:** {a}\n\n**➥ Hᴀᴠᴇ Vɪᴅᴇᴏ Iɴ Pʀᴏғɪʟᴇ:** {mad}\n\n**➥ Sᴄᴀᴍ:** {scam}\n\n**➥ Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛ:** {dele}")
    else:
       hehe = "Heyy you, Yes you\nWhy tf u want to see moi info??\nGo away and moind your own bizness"
       await event.answer(hehe, alert=True)
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA

# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
