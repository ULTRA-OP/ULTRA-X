"""Evaluate Python Code inside Telegram
Syntax: .eval PythonCode"""
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from telethon import events, errors, functions, types
import inspect
import traceback
import asyncio
import sys
import io, re
from ULTRA import CMD_HELP, eor
from uniborg.util import admin_cmd, sudo_cmd
from ..data.dev_db import check_dev
from ..data.alive_db import get_grp
dangers = [
  "bot.me",
  "get_me",
  "borg.me",
  "STRING_SESSION",
  "HEROKU_API_KEY",
  "environ",
  "DeleteAccountRequest",
  "session",
  "stderr",
  "stdout",
  "client.me"
  ]

@borg.on(admin_cmd("eval"))
@borg.on(sudo_cmd(pattern="eval", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    dev = await check_dev()
    if dev == "False":
      return await event.edit("This is restricted command if you know python then type `.devme` for removing dev `.rmdev`")
    excute = await eor(event, "Processing ...")
    group = await get_grp()
    cmd = event.text.split(" ", maxsplit=1)[1]
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "**EVAL**: `{}` \n\n **OUTPUT**: \n`{}` \n".format(cmd, evaluation)

    if len(final_output) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await borg.send_file(
                group,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
            await event.edit("Your command excuted Successfully check Private grp")
    else:
        string = ""
        for x in dangers:
          sed = re.search(x, final_output)
          if sed:
            string += sed + " "
          else:
            pass
        if string == "":
          await excute.edit(final_output)
        else:
          k = await bot.send_message(group, final_output)
          await excute.edit(f'Your code have danger word Found see your [result](https://t.me/c/{group}/{k.id})')


async def aexec(code, event):
    exec(
        f'async def __aexec(event): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__aexec'](event)

CMD_HELP.update(
    {
        "eval": ".eval code\
\nUsage: Excute Your Python Code but it's danger plugin\
"
    }
)

