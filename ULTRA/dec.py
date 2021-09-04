# COPYRIGHT © 2021 BY LEGENDX22

# made by @LEGENDX22
import inspect, re
from pathlib import Path
import os
def Var(var):
  result = os.environ.get(var, None)
  return result
cmd = os.environ.get('COMMAND_HAND_LER', ".")
from .import CMD_LIST, bot
from .data.sudo_db import all_sudo
from telethon import events
async def eor(event, msg, **ok):
  if event.out:
    await event.edit(msg, **ok)
  else:
    await event.reply(msg, **ok)


def UltraX(**x):
  stack = inspect.stack()
  previous_stack_frame = stack[1]
  file_test = Path(previous_stack_frame.filename)
  file_test = file_test.stem.replace(".py", "")
  admin_only = x.get("admin_only", False)
  group_only = x.get("group_only", False)
  sudo = x.get("allow_sudo", False)
  incoming = x.get("incoming", False)
  outgoing = x.get("outgoing", False)
  pattern = x.get("pattern", False)
  if not incoming and not outgoing:
    x["outgoing"] = True
  if pattern:
    x["pattern"] = re.compile(cmd + x["pattern"])
  if "admin_only" in x:
    del x["admin_only"]
  if "group_only" in x:
    del x["group_only"]
  if "allow_sudo" in x:
    del x["allow_sudo"]
  cmnd = pattern.replace("^", "").replace("(", "").replace(")", "").replace(".", "").replace("*", "").replace("$", "").replace("+", "").replace("?", "").replace("|", "")
  try:
    CMD_LIST[file_test].append(cmnd)
  except BaseException:
    CMD_LIST.update({file_test: [cmnd]})
  def decorator(func):
    test = True
    async def wrapper(event):
      sudos = await all_sudo()
      if not sudos:
        sudos = [12345]
      if sudo:
        if not event.out and event.sender_id in sudos:
          pass
        elif event.sender_id == (await bot.get_me()).id:
          pass
        else:
          return
      else:
        pass
      chat = await event.get_chat()
      if group_only and not event.is_group:
        return await eor(event, "This command for groups sir")
      if admin_only:
        try:
          rights = chat.admin_rights
        except:
          rights = False
        if not rights:
          return await eor(event, "this command for only admins sir")
      try:
        await func(event)
      except Exception as e:
        print (e)
        await event.edit("**Error** - " + str(e))
    bot.add_event_handler(wrapper, events.NewMessage(**x))
    if x.get("outgoing", False) == True and sudo:
      x["outgoing"] = False
      x["incoming"] = True
      bot.add_event_handler(wrapper, events.NewMessage(**x))
    return wrapper
  return decorator
