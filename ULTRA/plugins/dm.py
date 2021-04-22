from telethon import *

from ULTRA import CMD_HELP
from ULTRA.utils import admin_cmd
from ULTRAX import MASTER


# Fixed by LEGDND X
@borg.on(admin_cmd(pattern="dm ?(.*)"))
async def _(dc):

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
        await dc.edit(f"**{MASTER}:** `Mᴇssᴀɢᴇ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴠᴇʀᴇᴅ sɪʀ ✌️✌️`")
    for i in c[1:]:
        msg += i + " " 
    if msg == "":  # hoho
        return
    try:
        await borg.send_message(chat_id, msg)
        await dc.edit(f"**{MASTER}:** `Mᴇssᴀɢᴇ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴠᴇʀᴇᴅ sɪʀ ✌️✌️`")
    except BaseException:  # hmmmmmmmmm🤔🤔
        await dc.edit(".dm (username) (text)")


CMD_HELP.update(
    {
        "dm": ".dm (username) (text)\n or\n .dm (username)(reply to msg)\n it'll forward the replyed msg"
    }
)
