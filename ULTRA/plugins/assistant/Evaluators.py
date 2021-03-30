#hmm
import asyncio
import io
import os
import sys
import traceback
from LEGENDX import xbot, devs
from telethon import events
from ULTRA import bot

@xbot.on(events.NewMessage(pattern=("/eval ?(*.)")))
async def _(event):
    pro = await bot.get_me()
    boy = pro.id
    if not event.sender_id in devs:
        if not event.sender_id == boy:
          return
    if event.fwd_from:
        return
    cmd = event.pattern_match.group(1)
    if not cmd:
        return await event.reply("What should i run ?..")
    proevent = await event.reply("Running ...")
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
    final_output = f"**•  Eval : **\n`{cmd}` \n\n**•  Result : **\n`{evaluation}` \n"
    await proevent.edit(
        text=final_output,
        aslink=True,
        linktext=f"**•  Eval : **\n`{cmd}` \n\n**•  Result : **\n",
    )


async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(_format.yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        f"async def __aexec(message, event , reply, client, p, chat): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )


@xbot.on(events.NewMessage(pattern=("/exec ?(*.)")))
async def _(event):
    pro = await bot.get_me()
    boy = pro.id
    if not event.sender_id in devs:
        if not event.sender_id == boy:
          return
    if event.fwd_from:
        return
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not cmd:
        return await event.reply("What should i execute?..")
    proevent = await event.reply("Executing.....")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    curruser = pro.username or "UltraX"
    uid = os.geteuid()
    if uid == 0:
        cresult = f"`{curruser}:~#` `{cmd}`\n`{result}`"
    else:
        cresult = f"`{curruser}:~$` `{cmd}`\n`{result}`"
    await proevent.edit(
        text=cresult,
        aslink=True,
        linktext=f"**•  Exec : **\n`{cmd}` \n\n**•  Result : **\n",
    )
