# COPYRIGHT © 2021-2022 BY LEGENDX22
# COPY WITH CREDITS 
import re, os
from var import Var
from ..utils import admin_cmd
from ..data.sudo_db import *

@bot.on(admin_cmd(pattern='rmsudo'))
async def remove_sudo(event):
  if not event.is_reply:
    return await event.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴘʟᴇᴀsᴇ")
  try:
    id = (await event.get_reply_message()).sender_id
    name = (await bot.get_entity(id)).first_name
    op = await is_sudo(id)
    if op:
      await rm_sudo(id)
      await event.edit(f"Tʜᴇ **{name}** ɪs ʀᴇᴍᴏᴠᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ")
    else:
      await event.edit(f"ᴛʜᴇ {name} ɪs ɴᴏᴛ ɪɴ sᴜᴅᴏ 😑😑")
  except Exception as e:
    await event.edit(f"**ERROR** - {str(e)}")

@bot.on(admin_cmd("sudo"))
async def sudos(event):
  if await all_sudo():
    await event.edit("sᴜᴅᴏ ɪs ᴇɴᴇᴀʙʟᴇᴅ ᴛʏᴘᴇ `.listsudo` ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ")
  else:
     await event.edit("sᴜᴅᴏ ɪs ᴏғғ")            
@bot.on(admin_cmd("listsudo"))
async def sudolists(event):
  op = await event.edit('ᴄʜᴇᴄᴋɪɴɢ ᴀʟʟ sᴜᴅᴏs ᴡᴀɪᴛ')
  sudolist = await all_sudo()
  if not sudolist:
    return await event.edit("sᴜᴅᴏ ʟɪsᴛ ɪs ᴇᴍᴘᴛʏ")
  sudoz = "**»sᴜᴅᴏ ʟɪsᴛ«**"
  for sudo in sudolist:
    k = await bot.get_entity(int(sudo))
    pro = f'\n[**ɴᴀᴍᴇ:** {k.first_name} \n**ᴜsᴇʀɴᴀᴍᴇ:** @{k.username or None}]\n'
    sudoz += pro
  await op.edit(sudoz)

@bot.on(admin_cmd(pattern='addsudo'))
async def add_sudo(X):
  #if not X.is_reply:
    #return await event.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴘʟᴇᴀsᴇ")
  try:
    id = (await X.get_reply_message()).sender_id
    name = (await bot.get_entity(id)).first_name
    op = await is_sudo(id)
    if op:
      await X.edit(f"THE {name} IS ALREADY ON SUDO LIST")
      return
    else:
      pass
    await add_sudo(id)
    await X.edit(f"Oᴋᴀʏ **{name}** ɪs ᴀᴅᴅᴇᴅ ᴏɴ sᴜᴅᴏ ᴜsᴇʀs")
  except Exception as e:
    await X.edit(f"**ERROR** - {str(e)}")                              
