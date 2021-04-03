# made by LEGENDX22

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd

naam = str(ALIVE_NAME)

bot = "@hexamonbot"

Pokes = ('**Here Are Your HexaPokes**\n➖➖➖➖➖➖➖➖➖➖➖\n')

@borg.on(admin_cmd("mypokes ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/mypokemon")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, Pokes + audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock **@hexamonbot** and retry!")
    elif "@" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/mypokemon " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, Pokes + audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock **@hexamonbot** and try again!")
    elif "" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/mypokemon " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, Pokes + audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock **@hexamonbot** and try again!")
CMD_HELP.update({
    "hexapokes":"type `.mypokes` to get your all hexa pokes"})
