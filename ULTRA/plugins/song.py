# Copyright (C) 2021 By Team UltraX 

# ~ LegendX
# ~ ProBoyX
# ~ MadBoy
# ~ Alain

# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA

# Kang with Credits, else gey
# I knew u will kang and remove credits, duffer!!

# back click kar madharchod 

# Last Warn - Undo the removed part else be ready for DMCA by LegendX
# Mobile me back option he uspe click karde madhachod kang kiya to dekh


import os, re
from ULTRAX import id, ID, devs
from telethon.tl.functions.contacts import BlockRequest as block
from telethon import Button, custom, events, functions

# back button click kr madarchod
from ULTRAX import NAME
ULTRA_USER = NAME

BOT_MSG = os.environ.get("BOT_MSG", None)
if BOT_MSG is None:
  BOT_MAD = f"Hᴇʟʟᴏ sɪʀ ᴍʏsᴇʟғ UʟᴛʀᴀX, ғᴏʀ {ULTRA_USER}'s Pʀᴏᴛᴇᴄᴛɪᴏɴ "
else:
  BOT_MAD = BOT_MSG   

WARN = (
  f'''
**{BOT_MAD}**
__Hᴇʏ ᴛʜᴇʀᴇ!! I'ᴍ__ **υℓтяα χ** __ᴀɴᴅ I'ᴍ ʜᴇʀᴇ ᴛᴏ Pʀᴏᴛᴇᴄᴛ **{ULTRA_USER}**..\nDᴏɴ'ᴛ Uɴᴅᴇʀ Esᴛɪᴍᴀᴛᴇ ᴍᴇ 😈😈__**
__Mʏ Mᴀsᴛᴇʀ **{ULTRA_USER}**  ɪs ʙᴜsʏ ʀɪɢʜᴛ ɴᴏᴡ !!__ \n"
Mʏ Mᴀsᴛᴇʀ ʜᴀs ᴀssɪɢɴᴇᴅ ᴍᴇ ᴛʜᴇ ᴅᴜᴛʏ ᴛᴏ ᴋᴇᴇᴘ ᴀ ᴄʜᴇᴄᴋ ᴏɴ ʜɪs PM, Aɴᴅ ɪ'ʟʟ ᴅᴏ ɪᴛ ғᴀɪᴛʜғᴜʟʟʏ..Sᴏ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅɪsᴛᴜʀʙ ʜɪᴍ..
**Iғ ᴜ Sᴘᴀᴍ, ᴏʀ ᴛʀɪᴇᴅ ᴀɴʏᴛʜɪɴɢ ғᴜɴɴʏ, I'ᴠᴇ ғᴜʟʟ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ Bʟᴏᴄᴋ + Rᴇᴘᴏʀᴛ ʏᴏᴜ ᴀs Sᴘᴀᴍ ɪɴ Tᴇʟᴇɢʀᴀᴍ's sᴇʀᴠᴇʀ...**
**Bᴇᴛᴛᴇʀ ʙᴇ ᴄᴀʀᴇғᴜʟ..**
**Cʜᴏᴏsᴇ ᴀɴʏ Rᴇᴀsᴏɴ & GTFO**
''')

ULTRA_BOT_PIC = os.environ.get("PMPERMIT_PIC", None)
if ULTRA_BOT_PIC is None:
    ULTRA_PIC = "https://telegra.ph/file/91d427a6873d44ca21c78.jpg"
else:
    ULTRA_PIC = ULTRA_BOT_PIC

back = [[Button.inline("«« Bᴀᴄᴋ", data="pm_back")]]
@xbot.on(events.InlineQuery())
async def inline_legend(event):
  piro = event.text
  if event.sender_id == bot.me.id and piro == 'pmsecurity' or event.sender_id==id and piro=='pmpermit':
    LEGENDX = event.builder
    LEGEND = [[Button.inline("Fʀɪᴇɴᴅ", data='frnd_bsdk'),Button.inline("Sᴘᴀᴍ", data='hmmmmm')]]
    LEGEND += [[Button.inline("Wᴜᴛ's ᴛʜɪs ?",data='noobda')]]
    PROBOYX = LEGENDX.photo(file=ULTRA_PIC, text=WARN, buttons=LEGEND)
    await event.answer([PROBOYX])
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'chutia')))
async def chutia_aayaa(event):
  global back
  if event.sender_id !=bot.me.id or event.sender_id != id:
     CONFIRM = [[Button.inline("Wɪʟʟ ʏᴏᴜ sᴘᴀᴍ?", data='confirm_chutia')]]
     CONFIRM += back
     await event.edit("**Aʀᴇ ʏᴏᴜ sᴘᴀᴍᴍᴇʀ?**", buttons=CONFIRM)
  else:
     No = "**Nᴏ ᴍᴀsᴛᴇʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ sᴘᴀᴍᴍᴇʀ**"
     await event.answer(No, alert=False)

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'confirm_chutia')))
async def confirmed(event):
  pro=event.sender_id
  global block
  if pro != bot.me.id or pro != ID:
    await event.edit("**Oʜᴋ sᴏ ɢᴏ ᴛᴏ ʜᴇʟʟ ᴅᴜᴅᴇ 😁**")
    await bot(block(pro))
  else:
     No = "**Nᴏ ᴍᴀsᴛᴇʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ sᴘᴀᴍᴍᴇʀ**"
     await event.answer(No, alert=False)

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'frnd_bsdk')))
async def Inline_legendx(event):
  piro = event.sender_id
  global back
  if piro != bot.me.id or piro != id:
    await event.edit("**Oᴋɪᴇ ᴡᴇɪᴛ ᴛɪʟʟ ᴍʏ ᴍᴀsᴛᴇʀ ʀᴇᴘʟʏ ʏᴏᴜ, Hᴇ ᴡɪʟʟ ʀᴇᴘʟʏ ʏᴏᴜ sᴏᴏɴ ᴀsᴀᴘ !!**", buttons=back)
  else:
    await event.answer("**Mᴀsᴛᴇʀ, ᴜsᴇ** `.approve` **ᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ʜɪᴍ**")
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'noobda')))
async def noobda (event):
  global back
  Piro = [[Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/UltraXchaT"), Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/UltraXoT")]]
  Piro += [[Button.url("Rᴇᴘᴏ", "https://github.com/ULTRA-OP/ULTRA-X")]]
  Piro += back
  await event.edit("**CʜᴇᴄᴋOᴜᴛ ᴛʜᴇsᴇ ʟɪɴᴋs**", buttons=Piro)
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'pm_back')))
async def inline_legend(event):
  acha = event.sender.first_name
  jnl = bot.me.first_name
  LEGENDX = [[Button.inline("Fʀɪᴇɴᴅ", data='frnd_bsdk'),Button.inline("Sᴘᴀᴍ", data='hmmmmm')]]
  LEGENDX += [[Button.inline("Wᴜᴛ's ᴛʜɪs ?",data='noobda')]]
  await event.edit(f"Hᴇʟʟᴏ **{acha}**, ᴍʏ sᴇʟғ UʟᴛʀᴀX, ʜᴇʀᴇ ᴛᴏ ᴘʀᴏᴛᴇᴄᴛ **{jnl}**!", buttons=LEGENDX)
  
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'nino')))
async def _(event):
  global back
  await event.edit("**Oᴋɪᴇ ᴡᴇɪᴛ ᴛɪʟʟ ᴍʏ ᴍᴀsᴛᴇʀ ʀᴇᴘʟʏ ʏᴏᴜ, Hᴇ ᴡɪʟʟ ʀᴇᴘʟʏ ʏᴏᴜ sᴏᴏɴ ᴀsᴀᴘ !!**", buttons=back)
  
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'hmmmmm')))
async def _(event):
  kk = [[Button.inline("Yᴇs", data='confirm_chutia')]]
  kk += [[Button.inline("Nᴏ", data='nino')]]
  await event.edit("Wɪʟʟ ʏᴏᴜ sᴘᴀᴍ?", buttons=kk)

  

# Copyright (C) 2021 By Team UltraX 

# ~ LegendX
# ~ ProBoyX
# ~ MadBoy
# ~ Alain

# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA

# Kang with Credits, else gey
# I knew u will kang and remove credits, duffer!!

# back click kar madharchod 

# Last Warn - Undo the removed part else be ready for DMCA by LegendX
# Mobile me back option he uspe click karde madhachod kang kiya to dekh
