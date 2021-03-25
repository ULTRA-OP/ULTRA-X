# COPYRIGHT (C) 2021-2022 © Ultra X Bot
from ULTRA.utils import admin_cmd
from UltraX import tbot, NAME
from telethon import Button
@borg.on(admin_cmd(pattern="button (.*)"))
async def Buttons(event):
  await event.edit("making your button")
  ULTRAX = Var.TG_BOT_USER_NAME_BF_HER
  pro = event.text[7:]
  pro, boy = pro.split("|")
  if "ULTRAX" == "PROBOYX":
    await xbot.send_message(event.chat_id, "buttons")
  else:
    try:
      async with bot.conversation(ULTRAX) as proboyx:
        await proboyx.send_message("/start")
        await proboyx.get_response()
        await proboyx.send_message("my button 🥺")
        await tbot.send_message(bot.me.id, f"{NAME}", buttons=[[Button.url(f"{pro}", f"{boy}")]])
        pro = await proboyx.get_response()
        await pro.forward_to(event.chat_id)
        await event.delete()
    except:
        await event.edit("example:\n.button b<button name>|<link>\n`.button ULTRAX|https://t.me/ULTRAXOT`\nmake sure your name and link no have Useless spece ", link_preview=False)
