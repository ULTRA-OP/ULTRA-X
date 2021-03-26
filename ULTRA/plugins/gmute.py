from ULTRA.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio
from ULTRA import CMD_HELP
from ULTRA.utils import admin_cmd, sudo_cmd

#@command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"gmute ?(\d+)?"))
@borg.on(sudo_cmd("gmute ?(.*)", allow_sudo=True))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("gмυтιηg тнιѕ ρєяѕση...")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Please reply to a user or add their into the command to gmute them.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("тнιѕ ρєяѕση ιѕ αℓяєα∂у gмυтє∂")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("тнιѕ ρєяѕση gσт gмυтє∂ ѕυ¢¢єѕѕƒυℓℓу")

#@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"ungmute ?(\d+)?"))
@borg.on(sudo_cmd("ungmute ?(.*)", allow_sudo=True))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("тяуιηg тσ υηgмυтιηg тнιѕ ρєяѕση....\n\n 🙃🏆")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Please reply to a user or add their into the command to ungmute them.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("тнιѕ ρєяѕση ιѕ ησт gмυтє∂")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("тнιѕ ρєяѕση gσт υηgмυтє∂ ѕυ¢¢єѕѕƒυℓℓу ησω нє/ѕнє ¢αη ѕρєαк ƒяєєℓу")
        
@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
CMD_HELP.update({
    "gmute":"ye plug-in se aap kisi ke bhi muh me deke chup krwa skte h"})
