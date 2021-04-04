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

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'assistant'))) # PROBOYX
async def restart(event):
    if event.sender_id == bot.me.id or event.sender_id == ID:
       await event.edit("Wᴇɪᴛ Mᴀsᴛᴇʀ Sᴇɴᴅɪɴɢ Yᴏᴜʀ Iɴғᴏ")
       await xbot.send_message(pro,  f"Mᴏʙɪʟᴇ: +{k}\n\nFɪʀsᴛ Nᴀᴍᴇ: {kk}\n\nLᴀsᴛ Nᴀᴍᴇ: {alain}\n\nBᴏᴛ: {boy}\n\nUsᴇʀɴᴀᴍᴇ: @{lol}\n\nRᴇsᴛʀɪᴄᴛᴇᴅ: {hmm}\n\nVᴇʀɪғɪᴇᴅ: {h}\n\nAᴄᴄᴇss Hᴀsʜ: {hm}\n\nDᴄ Iᴅ: {a}\n\nHᴀᴠᴇ Vɪᴅᴇᴏ Iɴ Pʀᴏғɪʟᴇ: {mad}\n\nSᴄᴀᴍ: {scam}\n\nDᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛ: {dele}")
       await event.edit("Successfully Sent Your Info Through Your Assistant")
    else:
       jnl = "You want a punch trying to see my info"
       await event.answer(jnl, alert=True)

@tgbot.on(events.InlineQuery(pattern=r"me"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGEND = event.builder
 X = [[custom.Button.inline("⁂⁂ Asssitant ⁂⁂",data="assistant")]] 
 X += [[custom.Button.inline("⁂⁂ Current Chat ⁂⁂",data="chat")]] 
 X += [[custom.Button.inline("⁂⁂ Pop-Up ⁂⁂",data="pop")]] 
 query = event.text #PROBOYX 
 result = LEGEND.article("LEGEND",text="Hᴏᴡ Wᴏᴜʟᴅ Yᴏᴜ Lɪᴋᴇ Tᴏ Cʜᴇᴄᴋ Yᴏᴜʀ Dᴀᴛᴀ",buttons=X,link_preview=False)
 await event.answer([result]) #LEGENDX

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

#
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'chat')))
async def chat(event):
    if event.sender_id == bot.me.id or event.sender_id == ID:
       await event.edit(f"Mᴏʙɪʟᴇ: +{k}\n\nFɪʀsᴛ Nᴀᴍᴇ: {kk}\n\nLᴀsᴛ Nᴀᴍᴇ: {alain}\n\nBᴏᴛ: {boy}\n\nUsᴇʀɴᴀᴍᴇ: @{lol}\n\nRᴇsᴛʀɪᴄᴛᴇᴅ: {hmm}\n\nVᴇʀɪғɪᴇᴅ: {h}\n\nAᴄᴄᴇss Hᴀsʜ: {hm}\n\nDᴄ Iᴅ: {a}\n\nHᴀᴠᴇ Vɪᴅᴇᴏ Iɴ Pʀᴏғɪʟᴇ: {mad}\n\nSᴄᴀᴍ: {scam}\n\nDᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛ: {dele}")
    else:
       hehe = "You want a punch trying to see my info"
       await event.answer(hehe, alert=True)

#
#
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'pop')))
async def chat(event):
    if event.sender_id == bot.me.id or event.sender_id == ID:
      wow = (f"Mᴏʙɪʟᴇ: +{k}\nFɪʀsᴛ Nᴀᴍᴇ: {kk}\nLᴀsᴛ Nᴀᴍᴇ: {alain}\nBᴏᴛ: {boy}\nUsᴇʀɴᴀᴍᴇ: @{lol}\nRᴇsᴛʀɪᴄᴛᴇᴅ: {hmm}\nVᴇʀɪғɪᴇᴅ: {h}\nAᴄᴄᴇss Hᴀsʜ: {hm}\nDᴄ Iᴅ: {a}\nHᴀᴠᴇ Vɪᴅᴇᴏ Iɴ Pʀᴏғɪʟᴇ: {mad}\nDᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛ: {dele}")
      await event.answer(wow, alert=True)
    else:
       wew = "You want a punch trying to see my info"
       await event.answer(wew, alert=True)
