import io
import json
import math
import os
import re
import time
import sys

from telethon import Button, custom, events, functions, version

from ULTRA import CMD_LIST
from ULTRA import ALIVE_NAME
from ULTRAX import PHOTO
from ULTRA.utils import admin_cmd, sudo_cmd
from platform import uname

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"


#@command(pattern="^.help ?(.*)")

@borg.on(admin_cmd(pattern=r"ihelp ?(.*)", outgoing=True))
@borg.on(sudo_cmd(pattern=r"ihelp ?(.*)", outgoing=True, allow_sudo=True))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/" , "#", "-", "_", "@"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":

            string = ""

            for i in CMD_LIST:

                string += "â¡ï¸" + i + "\n"

                for iter_list in CMD_LIST[i]:

                    string += "    " + str(iter_list) + ""

                    string += "\n"

                string += "\n"

            if len(string) > 69:

                with io.BytesIO(str.encode(string)) as out_file:

                    out_file.name = "cmd.txt"

                    await bot.send_file(

                        event.chat_id,

                        out_file,

                        force_document=True,

                        allow_cache=False,

                        caption="¢σммαη∂ѕ ιη υℓтяα χ вσт",

                        reply_to=reply_to_id

                    )

                    await event.delete()

            else:

                await event.edit(string)

        elif input_str:

            if input_str in CMD_LIST:

                string = "Cᴏᴍᴍᴀɴᴅ ғᴏᴜɴᴅ ɪɴ {}:\n".format(input_str)

                for i in CMD_LIST[input_str]:

                    string += "  " + i

                    string += "\n"

                await event.edit(string)

            else:

                await event.edit(input_str + " ɪs ɴᴏᴛ ᴀ ᴠᴀʟɪᴅ Pʟᴜɢɪɴ")

        else:

            help_string = f""" υℓтяα χ вσт Hᴇʟᴘ ᴘʀᴏᴠɪᴅᴇᴅ ʙʏ тєαм υℓтяα χ\n

Dᴏ `.help` PLUGIN_NAME ғᴏʀ ᴄᴏᴍᴍᴀɴᴅs, ɪғ ɪɴ ᴄᴀsᴇ Pᴏᴘ-Uᴘ ᴅᴏᴇsɴ'ᴛ ᴀᴘᴘᴇᴀʀ."""

            results = await bot.inline_query(  # pylint:disable=E0602

                tgbotusername,

                help_string

            )

            await results[0].click(

                event.chat_id,

                reply_to=event.reply_to_msg_id,

                hide_via=True

            )

            await event.delete()

            

@borg.on(admin_cmd(pattern="legend"))  # pylint:disable=E0602

async def _(event):

    if event.fwd_from:

        return

    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602

    await event.edit(result.stringify())





@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602

async def _(event):

    if event.fwd_from:

        return

    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602

    result = result.stringify()

    logger.info(result)  # pylint:disable=E0602

    await event.edit("тєℓєтнση  вαѕє∂ υѕєявσт ρσωєяє∂ ву υℓтяα χ вσт")





@borg.on(admin_cmd(pattern="syntax (.*)"))

async def _(event):

    if event.fwd_from:

        return

    plugin_name = event.pattern_match.group(1)



    if plugin_name in CMD_LIST:

        help_string = CMD_LIST[plugin_name].doc

        unload_string = f"Usᴇ `.unload` {plugin_name} ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴛʜɪs Pʟᴜɢɪɴ.\n           Â© υℓтяα χ"

        

        if help_string:

            plugin_syntax = f"Sʏɴᴛᴀx ғᴏʀ ᴘʟᴜɢɪɴ {plugin_name}:\n\n{help_string}\n{unload_string}"

        else:

            plugin_syntax = f"Nᴏ DOCSTRING ʜᴀs ʙᴇᴇɴ sᴇᴛᴜᴘ ғᴏʀ {plugin_name} Pʟᴜɢɪɴ."

    else:



        plugin_syntax = "Eɴᴛᴇʀ ᴠᴀʟɪᴅ Pʟᴜɢɪɴ ɴᴀᴍᴇ.\nDᴏ `.plinfo` ᴏʀ `.help` ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴠᴀʟɪᴅ Pʟᴜɢɪɴ ɴᴀᴍᴇs."



    await event.edit(plugin_syntax)
