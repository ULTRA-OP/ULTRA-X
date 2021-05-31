from telethon import *

from ULTRA import CMD_HELP
from ULTRA.utils import admin_cmd
from ULTRA import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"

# Fixed by LEGDND X
@borg.on(admin_cmd(pattern="dm ?(.*)"))
async def _(dc):
    ultrax = bot.uid
    USERNAME = f"tg://user?id={ultrax}"
    
    d = dc.pattern_match.group(1)

    c = d.split(" ")

    chat_id = c[0]
    try:
        chat_id = int(chat_id)

    except BaseException:

        pass

    msg = ""
    masg = await dc.get_reply_message()  # ghanta😒😒
    if dc.reply_to_msg_id:
        await borg.send_message(chat_id, masg)
        await dc.edit(f"✅✅\n\n**[{DEFAULTUSER}]({USERNAME})** : 𝒀𝒐𝒖𝒓 𝒎𝒆𝒔𝒔𝒂𝒈𝒆 𝒘𝒂𝒔 𝒔𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚 𝒅𝒆𝒍𝒊𝒗𝒆𝒓𝒆𝒅\n\n✅✅")
    for i in c[1:]:
        msg += i + " " 
    if msg == "":  # hoho
        return
    try:
        await borg.send_message(chat_id, msg)
        await dc.edit(f"✅✅\n\n**[{DEFAULTUSER}]({USERNAME})** : 𝒀𝒐𝒖𝒓 𝒎𝒆𝒔𝒔𝒂𝒈𝒆 𝒘𝒂𝒔 𝒔𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚 𝒅𝒆𝒍𝒊𝒗𝒆𝒓𝒆𝒅\n\n✅✅")
    except BaseException:  # hmmmmmmmmm🤔🤔
        await dc.edit("__.dm <@username> <text>__")


CMD_HELP.update
(
  {
    "dm": "**Plugin :** `dm`\
    \n\n**Syntax : **`.dm <username> <text>`\
    \n**Usage : ** Sends the <text> msg to the given <username>\
    \n\n**Syntax : **`.dm <username> (reply to a msg)`\
    \n**Usage : ** Forwards the (replied msg) to the given <username>"
  }
)
