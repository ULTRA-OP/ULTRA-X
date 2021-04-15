# back button click kr madarchod
WARN = ''
import os,re
from telethon import Button, events
from telethon.tl.functions.contacts import BlockRequest as block
from . import id, ID, devs
back = [[Button.inline("Back", data="pm_back")]]
@xbot.on(events.InlineQuery())
async def inline_legend(event):
  piro = event.text
  if event.sender_id == bot.me.id and piro == 'pmsecurity' or event.sender_id==id and piro=='pmpermit':
    LEGENDX = event.builder
    LEGEND = [[Button.inline("Freind", data='frnd_bsdk'),Button.inline("Spam", data='chutia')]]
    LEGEND += [[Button.inline("What is this??",data='noobda')]]
    PROBOYX = LEGENDX.article(title='pmpermit of ULTRA X', text=WARN)
    await event.answer([PROBOYX])
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'chutia')))
async def chutia_aayaa(event):
  global back
  if event.sender_id !=bot.me.id or event.sender_id != id:
     CONFIRM = [[Button.inline("confirm you spammer?", data='confirm_chutia')]]
     CONFIRM += back
     await event.edit("please confirm you are spammer ?", buttons=CONFIRM)
  else:
     No = "NO MASTER YOU ARE NOT SPAMMER")
     await event.answer(No, alert=False)

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'confirm_chutia')))
async def confirmed(event):
  pro=event.sender_id
  global block
  if pro != bot.me.id or pro != ID:
    await event.edit("oh go to hell bsdk\ni blocked you")
    await bot(block(pro))
  else:
     No = "NO MASTER YOU ARE NOT SPAMMER")
     await event.answer(No, alert=False)

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'frnd_bsdk')))
async def Inline_legendx(event):
  piro = event.sender_id
  global back
  if piro != bot.me.id or piro != id:
    await event.edit("OKAY SIR PLEASE WAIT MY MASTER IS COMING SOON", buttons=back)
  else:
    await event.answer("MASTER USE .approve for approve this user")
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'noobda')))
async def noobda (event):
  global back
  Piro = [[Button.url("Support", "https://t.me/UltraXchaT"), Button.url("Channel", "https://t.me/UltraXoT")]]
  Piro += [[Button.url("Repo", "https://github.com/ULTRA-OP/ULTRA-X")]]
  Piro += back
  await event.edit("check-ing this links", buttons=Piro)
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'pm_back')))
async def inline_legend(event):
  LEGENDX = [[Button.inline("Freind", data='frnd_bsdk'),Button.inline("Spam", data='chutia')]]
  LEGENDX += [[Button.inline("What is this??",data='noobda')]]
  await event.edit(buttons=LEGENDX)
