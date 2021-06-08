# COPYRIGHT © 2021-2022 BY LEGENDX22
# COPY WITH CREDITS
from . import *
from telethon import *
def handler():
  k = os.environ.get("COMMAND_HAND_LER", ".")
  return k
@bot.on(admin_cmd("share"))
@bot.on(sudo_cmd(pattern='share'))
async def amazing (event):
  text = event.text.split(" ", 1)
  hndlr = handler()
  if event.text == f'{hndlr}share':
    return await event.edit("Please Give some text")
  pro = text[1].replace(" ", "%20")
  inline = await bot.inline_query((await xbot.get_me()).username, f'share|{pro}')
  print ("share plug-in fired")
  await inline[0].click(event.chat_id)
  await event.delete()

@xbot.on(events.InlineQuery(pattern='share'))
async def share_inline(event):
  text = event.text.split("|")
  url = f'http://t.me/share/url?url={text[1]}'
  LEGENDX = event.builder
  pro = [Button.url("TAP ME", url=url)]
  piro = LEGENDX.article(title='Shared Message', text="Super Message tap on Button", buttons=pro)
  await event.answer([piro])
