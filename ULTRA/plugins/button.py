# jnl
# COPYRIGHT (C) 2021-2022 BY LEGENDX22
# MADE BY LEGENDX22
from telethon import Button, events
from ..utils import admin_cmd
from ..utils import edit_or_reply, eor
from ..utils import sudo_cmd
from .. import CMD_HELP

@borg.on(admin_cmd(pattern="button (.*)"))
@borg.on(sudo_cmd(pattern="button", allow_sudo=True))
async def Buttons(event):
    await eor(event, "`Mᴀᴋɪɴɢ Yᴏᴜʀ Bᴜᴛᴛᴏɴ ᴡᴇɪᴛ ᴍᴀsᴛᴇʀ !!!`")
    ULTRAX = Var.TG_BOT_USER_NAME_BF_HER
    pro = event.text[7:]
    pro, boy = pro.split("|")
    f = open("Button.txt", "w") # by LEGENDX22, PROBOYX
    f.write(f'{pro}\n{boy}')
    f.close()
    LEGENDX = await bot.inline_query(ULTRAX, "BUTTON")
    await LEGENDX[0].click(event.chat_id)
    await event.delete()

@xbot.on(events.InlineQuery(pattern='BUTTON'))
async def file(event):
  f = open("Button.txt")
  ok = f.readlines()[0]
  f.close()
  PROBOYX = open("Button.txt")
  bc = PROBOYX.readlines()[1]
  PROBOYX.close()
  LEGENDX = event.builder
  LEGENDX22 = [[Button.url(f'{ok}', f'{bc}')]]
  PROBOYXOP = LEGENDX.article(title='Button by ULTRA X', text=f'{ok}', buttons=LEGENDX22)
  await event.answer([PROBOYXOP])

CMD_HELP.update
(
  {
    "button": ".button <button name>|<link>\n`.button UltraX|https://t.me/ULTRAXOT`\nmake sure your name and link no have Useless space"
  }
)
