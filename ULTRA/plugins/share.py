# COPYRIGHT © 2021-2022 BY LEGENDX22
# COPY WITH CREDITS

from . import *
from telethon import *
def handler():
  k = os.environ.get("COMMAND_HAND_LER", ".")
  return k
@bot.on(admin_cmd(pattern="share"))
#@bot.on(sudo_cmd(pattern='share', allow_sudo=True))
async def amazing (event):
  text = event.text.split(" ", 1)
  #hndlr = handler()
  #if event.text == f'{hndlr}share':
    #return await event.edit("𝐏𝐥𝐞𝐚𝐬𝐞 𝐠𝐢𝐯𝐞 𝐬𝐨𝐦𝐞 𝐓𝐞𝐱𝐭")
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
  pro = [Button.url("𝑪𝒍𝒊𝒄𝒌 𝑯𝒆𝒓𝒆", url=url)]
  piro = LEGENDX.article(title='Super Message', text="𝙎𝙪𝙥𝙚𝙧 𝙈𝙚𝙨𝙨𝙖𝙜𝙚\n\n𝙏𝙖𝙥 𝙤𝙣 𝙩𝙝𝙚 𝘽𝙪𝙩𝙩𝙤𝙣 𝘽𝙚𝙡𝙤𝙬, 𝙖𝙣𝙙 𝙎𝙚𝙡𝙚𝙘𝙩 𝙩𝙝𝙚 𝘾𝙝𝙖𝙩 𝙩𝙤 𝙨𝙚𝙣𝙙 𝙩𝙝𝙚 𝙈𝙚𝙨𝙨𝙖𝙜𝙚", buttons=pro)
  await event.answer([piro])
