#COPYRIGHT 2021-22 BY LEGENDX22, PROBOYX
""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
             DONT DARE TO KANG WITHOUT CREDITS
"""
# IF YOU KANG THEN KEEP CREDITS PLEASE 🥺
from telethon import events, Button
import re, os
from ULTRAX import id
from ULTRAX import xbot
@xbot.on(events.InlineQuery(pattern='wspr'))
async def inline_proboy(event):
  PROBOYX = event.text[5:]
  PROBOYX, GODBOYX = PROBOYX.split('@')
  os.system("rm -rf wspr.txt")
  f = open("wspr.txt", "a")
  f.write(PROBOYX + "\n" + GODBOYX)
  f.close()
  LEGENDX = event.builder
  MADBOI = [[Button.inline("SEE MSG", data='secret')]]
  MADBOI += [[Button.switch_inline("REPLY", query="wspr", same_peer=True)]]
  ALAIN = LEGENDX.article(title=f"FOR @{GODBOYX}", text=f"THIS IS SECRET MESSAGE FOR @{GODBOYX}", buttons=MADBOI)
  await event.answer([ALAIN])

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'secret')))
async def wspr(event):
  try:
    f = open("wspr.txt")
    LEGENDX = f.readlines()[0]
    f.close()
    pro = open("wspr.txt")
    PROBOYX = pro.readlines()[1].lower()
    pro.close()
    bot = await xbot.get_me()
    sender = f"{event.sender.username}".lower()
    me = f"{borg.me.username}".lower()
    if sender == PROBOYX or sender == me or event.sender_id == id:
       await event.answer(LEGENDX, alert=True)
    else:
       await event.answer("HEY DON'T SEE MY MSG", alert=False)
  except:
    await event.answer(f"use @{bot.username} wspr msg <@ sender username>", alert=True)
