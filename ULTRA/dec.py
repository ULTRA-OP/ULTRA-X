# decorator made by @LEGENDX22
from telethon import events
import os
def Var(var):
  result = os.environ.get(var, None)
  return result
cmd = os.environ.get('COMMAND_HAND_LER', ".")

from .data.sudo_db import all_sudo
def UltraX(**x):
  admin_only = x.get("admin_only", False)
  group_only = x.get("only_group", False)
  sudo = x.get("allow_sudo", False)
  incoming = x.get("incoming", False)
  outgoing = x.get("outgoing", False)
  x["pattern"] = cmd + x["pattern"]
  if "admin_only" in x: # delete that coz variables already get the values
    del x["admin_only"]
  if "group_only" in x:
    del x["group_only"]
  if "allow_sudo" in x:
    del x["allow_sudo"]
  def decorator(func):
    test = True
    async def wrapper(event):
      sudos = await all_sudo()
      if sudo:
        if not event.out and not event.sender_id in sudos:
          return
      else:
        pass
      chat = await event.get_chat()
      if group_only and not event.is_group:
        return await event.edit("This command for groups sir")
      if admin_only:
        try:
          rights = chat.admin_rights
        except:
          rights = False
        if not rights:
          return await event.edit("this command for only admins sir")
      await bot.send_message("LEGENDX22", "helo")
      await func(event)
    bot.add_event_handler(wrapper, events.NewMessage(**x))
    return wrapper
  return decorator
