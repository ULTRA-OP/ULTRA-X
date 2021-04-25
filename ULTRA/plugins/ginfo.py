"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
"""
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ULTRA import CMD_HELP
from ULTRA.utils import admin_cmd
from ULTRAX import MASTER
LEGEND = MASTER
PROBOY = "@tgscanrobot"
# MADE BY LEGENDX22 🔥🔥

@borg.on(admin_cmd("ginfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    LEGENDX = event.pattern_match.group(1)
    if "@" in LEGENDX:
        async with borg.conversation(PROBOY) as conv:
            try:
                
                await event.edit(f"ωαιт ¢нє¢кιηg тнє ∂єтαιℓѕ σƒ тнιѕ ρєяѕση ѕтαятє∂ ву {LEGEND}")
                await conv.send_message("/start")
                await conv.get_response() #made by LEGENDX22
                await conv.send_message(f"{LEGENDX}")
                TEAMX = await conv.get_response()
                TEAMX = TEAMX.message
                if TEAMX.startsawith("This human"):
                  return await event.edit("no details Found")
                await borg.send_message(event.chat_id, TEAMX)
                await event.delete() #made by LEGENDX22
            except YouBlockedUserError:
                await event.edit("Error: @tgscanrobot unblock and retry!")
    elif LEGENDX == "":
        OP = await event.get_reply_message()
        PRO = OP.sender.id 
        async with borg.conversation(PROBOY) as conv:
            try: #made by LEGENDX22 🔥
              #made by LEGENDX22 
                await event.edit(f"тнιѕ υѕєя ∂єтαιℓѕ ¢нє¢кιηg ву {LEGEND}")
                await conv.send_message("/start")
                await conv.get_response() #made by LEGENDX22
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                TEAMX = TEAMX.message
                if TEAMX.startswith("This human"):
                  return await event.edit("no details Found")
                await borg.send_message(event.chat_id, TEAMX)
                await event.delete()
            except YouBlockedUserError: #made by LEGENDX22
                await event.edit("Error: unblock @tgscanrobot and try again!")
    else:
        async with borg.conversation(PROBOY) as conv:
            try: #made by LEGENDX22 🔥
                
                await event.edit(f"тнιѕ υѕєя ∂єтαιℓѕ ¢нє¢кιηg ву {LEGEND}") 
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                TEAMX = TEAMX.message
                if TEAMX.startswith("This human"):
                  return await event.edit("no details found")
                await borg.send_message(event.chat_id, TEAMX)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock  @tgscanrobot `and try again!")
from .. import HELP
HELP(NAME = "ginfo", HELP = ".ginfo <tag or username>", FUCK=True, debug=False, amazing = None)
# try
