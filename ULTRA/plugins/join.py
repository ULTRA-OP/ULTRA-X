# made by madboy482
# made for ULTRA-X
# kang mat kr lawde

# UltraX

from telethon.tl.functions.channels import JoinChannelRequest as join
from ..utils import admin_cmd
from ULTRA import CMD_HELP
from ULTRA import ALIVE_NAME as MadBoy

MADBOY_USER = str(MadBoy) if MadBoy else "υℓтяα χ"

@bot.on(admin_cmd(pattern="join"))
async def join_krenge(MADBOY):
  madboy = bot.uid
  MADBOY_USERNAME = f"tg://user?id={madboy}"
  chat = MADBOY.text.split(" ", maxsplit=1)[1]
  try:
    await bot(join(chat))
    await MADBOY.edit(f"**[{MADBOY_USER}]({MADBOY_USERNAME})** :\n𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚 𝑱𝒐𝒊𝒏𝒆𝒅 𝒕𝒉𝒆 𝒈𝒊𝒗𝒆𝒏 𝑪𝒉𝒂𝒕")
  except:
    await MADBOY.edit(f"**[{MADBOY_USER}]({MADBOY_USERNAME})** :\n𝑺𝒐𝒎𝒆𝒕𝒉𝒊𝒏𝒈 𝑾𝒆𝒏𝒕 𝑾𝒓𝒐𝒏𝒈, 𝒘𝒉𝒊𝒍𝒆 𝑱𝒐𝒊𝒏𝒊𝒏𝒈 𝒕𝒉𝒆 𝒈𝒊𝒗𝒆𝒏 𝑪𝒉𝒂𝒕")
    
    
CMD_HELP.update
(
  {
    "join": "**Plugin :** `join`\
    \n\n**Syntax : **`.join @<GroupUsername>` / `.join` https://t.me/<GroupLink>\
    \n**Usage : ** Joins the group with just an username or a group link without manually doing it."
  }
)

# UltraX

# kang mat kr lawde
# made for ULTRA-X
# made by madboy482
