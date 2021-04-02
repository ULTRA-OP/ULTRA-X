#modify by @LEGENDX22
#credits shivam thanks bruh

from telethon import events
from ULTRA.events import remove_plugin, load_module
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from ULTRA.utils import command, remove_plugin, load_module
from pathlib import Path
from ULTRA import LOAD_PLUG, CMD_HELP
from ULTRA.utils import admin_cmd
import os
@bot.on(admin_cmd(pattern=r"^uninstall (?P<shortname>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path =f"./ULTRA/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await event.edit(f"**Uɴɪɴsᴛᴀʟʟᴇᴅ** `{shortname}` **Sᴜᴄᴄᴇssғᴜʟʟʏ**")
    except OSError as e:
        await event.edit("Error: %s : %s" % (dir_path, e.strerror))

CMD_HELP.update(
    {
        "uninstall": "**Plugin : **`uninstall`\
    \n\n**Syntax : **`uninstall`\
    \n**Function : **use this plugin without . and small later"
    }
)
