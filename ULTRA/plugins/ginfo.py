"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))


                  made by @LEGENDX22
                  credits TEAMLEGEND
                  idea by @Alain_Champion 
 ((((((((((((((((((((((((( @LEGENDX22 AND @PROBOYX)))))))))))))))))))))))))))
"""
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.utils import admin_cmd
from userbot.legend import MASTER
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
                
                await event.edit(f"THIS USER DETAILS CHECKING BY {LEGEND}")
                await conv.send_message("/start")
                await conv.get_response() #made by LEGENDX22
                await conv.send_message(f"{LEGENDX}")
                TEAMX = await conv.get_response()
                await borg.send_message(event.chat_id, TEAMX.text)
                await event.delete() #made by LEGENDX22
            except YouBlockedUserError:
                await event.edit("Error: @tgscanrobot unblock and retry!")
    elif LEGENDX == "":
        OP = await event.get_reply_message()
        PRO = OP.sender.id 
        async with borg.conversation(PROBOY) as conv:
            try: #made by LEGENDX22 🔥
              #made by LEGENDX22 
                await event.edit(f"THIS USER DETAILS CHECKING BY {LEGEND}")
                await conv.send_message("/start")
                await conv.get_response() #made by LEGENDX22
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                await borg.send_message(event.chat_id, TEAMX.text)
                await event.delete()
            except YouBlockedUserError: #made by LEGENDX22
                await event.edit("Error: unblock @tgscanrobot and try again!")
    else:
        async with borg.conversation(PROBOY) as conv:
            try: #made by LEGENDX22 🔥
                
                await event.edit(f"THIS USER DETAILS CHECKING BY {LEGEND}") 
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                await borg.send_message(event.chat_id, TEAMX.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock  @tgscanrobot `and try again!")
CMD_HELP.update({
    "ginfo ":"type .ginfo <@username> or tag a user type .ginfo 🔥"})
