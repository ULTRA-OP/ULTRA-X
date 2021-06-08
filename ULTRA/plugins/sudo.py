# COPYRIGHT © 2021-2022 BY LEGENDX22
# COPY WITH CREDITS 
import heroku3
import re, os
from var import Var
from ..utils import admin_cmd
LEGENDX = Var.HEROKU_APP_NAME
PROBOYX = Var.HEROKU_API_KEY
sudolist = os.environ.get("SUDO_USERS", None)
@bot.on(admin_cmd(pattern='addsudo'))
async def add_sudo(event):
  Heroku = heroku3.from_key(PROBOYX)
  app = Heroku.app(LEGENDX)
  heroku_var = app.config()
  if not event.is_reply:
    return await event.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴘʟᴇᴀsᴇ")                              
  if event.is_reply:
    id = (await event.get_reply_message()).sender_id
    name = (await bot.get_entity(id)).first_name
    sudo = heroku_var["SUDO_USERS"]
    op = re.search(str(id), str(sudolist))
    if op:
      await event.edit(f"THE {name} IS ALREADY ON SUDO LIST")
      return
    else:
      pass
    if not sudolist:
       await event.edit(f"Oᴋᴀʏ **{name}** ɪs Aᴅᴅᴇᴅ Oɴ sᴜᴅᴏ ʟɪsᴛ (ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ɪ ᴀᴍ ʀᴇsᴛᴀʀᴛɪɴɢ)")
       heroku_var["SUDO_USERS"] = id
    else:
       sudousers = f'{sudolist} {id}'
       await event.edit(f"Oᴋᴀʏ **{name}** ɪs ᴀᴅᴅᴇᴅ ᴏɴ sᴜᴅᴏ ᴜsᴇʀs (ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ɪ ᴀᴍ ʀᴇsᴛᴀʀᴛɪɴɢ)")
       heroku_var["SUDO_USERS"] = sudousers
  else:
    await event.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴘʟᴇᴀsᴇ")                              



@bot.on(admin_cmd(pattern='rmsudo'))
async def remove_sudo(event):
  Heroku = heroku3.from_key(PROBOYX)
  app = Heroku.app(LEGENDX)
  heroku_var = app.config()
  if not event.is_reply:
    return await event.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴘʟᴇᴀsᴇ")
  if event.is_reply:
    id = (await event.get_reply_message()).sender_id
    name = (await bot.get_entity(id)).first_name
    op = re.search(str(id), str(sudolist))
    if op:
      i = ""
      amazing = sudolist.split(" ")
      amazing.remove(str(id))
      i += str(amazing)
      x = i.replace("[", "")
      xx = x.replace("]", "")
      xxx = xx.replace(",", "")
      done = xxx.replace("'", "")
      heroku_var["SUDO_USERS"] = done
      await event.edit(f"Tʜᴇ **{name}** ɪs ʀᴇᴍᴏᴠᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ (ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ɪ ᴀᴍ ʀᴇsᴛᴀʀᴛɪɴɢ)")
    else:
      await event.edit(f"ᴛʜᴇ {name} ɪs ɴᴏᴛ ɪɴ sᴜᴅᴏ 😑😑")
    if heroku_var["SUDO_USERS"] == None:
       await event.edit(f"ᴛʜᴇ sᴜᴅᴏ ʟɪsᴛ ɪs ᴇᴍᴘʏᴛʏ 😑😑")
@bot.on(admin_cmd("sudo"))
async def sudos(event):
  if sudolist:
    await event.edit("sᴜᴅᴏ ɪs ᴇɴᴇᴀʙʟᴇᴅ ᴛʏᴘᴇ `.listsudo` ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ")
  else:
     await event.edit("sᴜᴅᴏ ɪs ᴏғғ")            
@bot.on(admin_cmd("listsudo"))
async def sudolists(event):
  op = await event.edit('ᴄʜᴇᴄᴋɪɴɢ ᴀʟʟ sᴜᴅᴏs ᴡᴀɪᴛ')
  Heroku = heroku3.from_key(PROBOYX)
  app = Heroku.app(LEGENDX)
  heroku_var = app.config()
  if not sudolist:
    return await event.edit("sᴜᴅᴏ ʟɪsᴛ ɪs ᴇᴍᴘᴛʏ")
  sudos = sudolist.split(" ")
  sudoz = "**»sᴜᴅᴏ ʟɪsᴛ«**"
  for sudo in sudos:
    k = await bot.get_entity(int(sudo))
    pro = f'\n[**ɴᴀᴍᴇ:** {k.first_name} \n**ᴜsᴇʀɴᴀᴍᴇ:** @{k.username or None}]\n'
    sudoz += pro
  await op.edit(sudoz)
