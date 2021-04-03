import asyncio
import time
from datetime import datetime

from .. import ALIVE_NAME, StartTime, CMD_HELP
from ..utils import admin_cmd, sudo_cmd, edit_or_reply

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND USER"
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
    
uptime = get_readable_time((time.time() - StartTime))


@borg.on(admin_cmd(pattern="loda$"))
@borg.on(sudo_cmd(pattern="loda$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    ghanta = borg.uid
    event = await edit_or_reply(event, "__**(★ Lessun!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"__**✦҈͜͡➳ Lessun!__**\n★ immunity {ms}\n★ __**Mere**__ **Master ka loda {uptime}  se khada h aur mere {DEFAULTUSER} ke pass abhi bht immunity h kisi ko bhi chod skte h check krna h kya abhi bhi khada h {uptime} hogaye  ** [{DEFAULTUSER}](tg://user?id={ghanta})"
    )


CMD_HELP.update(
    {
        "loda": "**Plugin : **`loda`\
    \n\n**Syntax : **`.loda`\
    \n**Function : **funny Plugin made by @LEGENDX22"
    }
)
