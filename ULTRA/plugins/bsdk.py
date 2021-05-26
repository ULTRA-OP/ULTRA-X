from telethon import events
from ULTRAX import *
import asyncio

from ULTRA import CMD_HELP
from ULTRA.utils import admin_cmd

@borg.on(admin_cmd("bsdk"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "gulli":
    await event.edit("gulli")
    animation_chars = [
            "**OK**",
            "**SUNN MADERCHOD**",
            "`TERI MAA KA BHOSDA`",
            "`BEHEN K LUND`",
            "**TERI MAA KA DUD**",
            "`MERA LAWDA LELE TU AGAR CHAIYE TOH`",
            "`GAANDU`",
            "**CHUTIYA**",
            "`TERI MAA KI CHUT PE JCB CHADHAA DUNGA`",
            "**SAMJHAA LAWDE**",
            "**YA DU TERE GAAND ME TAPAA TAP😂**",
            "`TERI BEHEN MERA ROZ LETI HAI`",
            "`TERI GF K SAATH MMS BANAA CHUKA HU🙈🤣🤣`",
            "`TU CHUTIYA TERA KHANDAAN CHUTIYA`",
            "**Yeahhhhhh**",
            "`AUR KITNA BOLU BEY MANN BHAR GAYA MERA🤣`",
            "**Ab nikal ja jaake chkko k saath hilaa**",
            "`😂😂😂🤣🤣`"
        ]

    for i in animation_ttl:
         
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

from ULTRAX import kangers
from telethon import events
@bot.on(events.NewMessage(incoming=True))
async def hehe (event):
  if event.is_private:
      return
  if event.sender_id in kangers:
    for kanger in kangers:
      try:
         await bot.edit_permissions(event.chat_id,kanger,view_messages=False)
      except:
         pass
  else:
    pass


from telethon import events,Button
from telethon.tl.types import InputWebDocument
from ULTRAX import MASTER, xbot
from ULTRA import ALIVE_NAME

from ULTRA import bot as ultra
global ok
madboi = ultra.uid

acha = ".Resources/IMG_20210413_155725_416.jpg"
omk = acha
omk = "https://telegra.ph/file/79f0a1b254b4511181afa.jpg"
k = bot.me.first_name

@xbot.on(events.InlineQuery())
async def inline (event):
  if event.query.user_id != bot.me.id or event.query.user_id ==bot.me.id and event.text == '' or event.query.user_id ==id and event.text == '':
     Buttonss = [[Button.url("Rᴇᴘᴏsɪᴛᴏʀʏ","https://github.com/ULTRA-OP/ULTRA-X"),Button.url("Dᴇᴘʟᴏʏ","https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU")]]
     fuck = f"**UʟᴛʀᴀX - Usᴇʀʙᴏᴛ**\n**➖➖➖➖➖➖➖➖➖➖**\n**Oᴡɴᴇʀ: [{MASTER}](tg://user?id={madboi})**\n**Cʜᴀɴɴᴇʟ: @UltraX_Support**\n**Sᴜᴘᴘᴏʀᴛ: @UltraXChat**\n**➖➖➖➖➖➖➖➖➖➖**"
     op = event.builder
     omg = op.article(title='UʟᴛʀᴀX Usᴇʀʙᴏᴛ', text=fuck, thumb=InputWebDocument(omk, 0, "image/jpeg", []), url="t.me/UltraXOT", description="© TᴇᴀᴍUʟᴛʀᴀX | Usᴇʀʙᴏᴛ | UʟᴛʀᴀX", buttons=Buttonss)
     await event.answer([omg], switch_pm=f'👤 Assɪsᴛᴀɴᴛ ᴏғ : {k}', switch_pm_param='start')
  else:
    pass

CMD_HELP.update({
    "bsdk":"**Abuse Plug Do** `.bsdk`"})
