"""Execute GNU/Linux commands inside Telegram
Syntax: .exec Code"""
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import time
from uniborg.util import admin_cmd
from .import *
from ..data.dev_db import check_dev
from ..data.alive_db import get_grp
dangers = [
  "env",
  "python"
  ]
import re
@borg.on(admin_cmd(pattern="bash ?(.*)"))
@bot.on(sudo_cmd(pattern="bash", allow_sudo=True))
async def _(event):
    if event.fwd_from or event.via_bot_id:
        return
    if (await check_dev()) == "False":
      return await eor(event, "Sory I can't Excute This Command \nbecause this is devloper command\nif you know shell/bash script\ntype `.devme`")
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    group = await get_grp()
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No Error"
    o = stdout.decode()
    if not o:
        o = "**Tip**: \n`If you want to see the results of your code, I suggest printing them to stdout.`"
    else:
        _o = o.split("\n")
        o = "`\n".join(_o)
    OUTPUT = f"**QUERY:**\n__Command:__\n`{cmd}` \n__PID:__\n`{process.pid}`\n\n**stderr:** \n`{e}`\n**Output:**\n{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                group,
                out_file,
                force_document=True,
                allow_cache=False, 
                caption=cmd,
                reply_to=reply_to_id
            )
            await event.edit('command excuted check private group')
    else:
      string = ""
      for x in dangers:
        k = re.search(x, OUTPUT)
        if k:
          string += x + " "
        else:
          pass
      if string == "":
        await event.edit(OUTPUT)
      else:
        pro = await bot.send_message(group, OUTPUT)
        await event.edit(f'your command have danger word \nsee your [result](https://t.me/c/{group}/{pro.id})')
