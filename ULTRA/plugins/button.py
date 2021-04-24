# COPYRIGHT (C) 2021-2022 © Ultra X Bot
from ULTRA.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from ULTRAX import xbot, NAME
from telethon import Button
@borg.on(admin_cmd(pattern="button (.*)"))
@borg.on(sudo_cmd(pattern="button", allow_sudo=True))
async def Buttons(event):
  await eor(event, "`Mᴀᴋɪɴɢ Yᴏᴜʀ Bᴜᴛᴛᴏɴ ᴡᴇɪᴛ ᴍᴀsᴛᴇʀ !!!`")
  ULTRAX = Var.TG_BOT_USER_NAME_BF_HER
  pro = event.text[7:]
  pro, boy = pro.split("|")
  if "LEGENDX" == "PROBOYX":
    await xbot.send_message(event.chat_id, "buttons")
  else:
    try:
      async with bot.conversation(ULTRAX) as proboyx:
        await proboyx.send_message("/start")
        await proboyx.get_response()
        await proboyx.send_message("my button 🥺")
        await xbot.send_message(bot.me.id, f"{pro}", buttons=[[Button.url(f"{pro}", f"{boy}")]])
        pro = await proboyx.get_response()
        await pro.forward_to(event.chat_id)
        await event.delete()
    except:
        await event.edit("example:\n.button <button name>|<link>\n`.button ULTRAX|https://t.me/ULTRAXOT`\nmake sure your name and link no have Useless spece ",link_preview=False)

from .. import CMD_HELP
CMD_HELP.update({"button": "example:\n.button <button name>|<link>\n`.button ULTRAX|https://t.me/ULTRAXOT`\nmake sure your name and link no have Useless spece"})
