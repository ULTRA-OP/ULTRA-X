from telethon import Button, custom, events
import os, re, sys, asyncio
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'restart')))
async def restart(event):
  if event.sender_id == bot.me.id:
    await event.edit("restarting your bot please wait")
    await asyncio.sleep(2)
    await event.edit("restarted your bot succesfully")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit ()
  else:
    pro = "ρℓєαѕє ∂єρℓσу уσυ σωη υℓтяα χ υѕєявσт"
    await event.answer(pro, alert=True)
