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
  if event.is_reply:
    id = (await event.get_reply_message()).sender_id
    name = (await bot.get_entity(id)).first_name
    sudo = heroku_var["SUDO_USERS"]
    op = re.search(id, str(sudolist))
    if op:
      await event.edit(f"THE {name} IS ALREADY ON SUDO LIST")
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
  if event.is_reply:
    id = (await event.get_reply_message()).sender_id
    name = (await bot.get_entity(id)).first_name
    op = re.search(id, str(sudolist))
    if op:
      i = ""
      amazing = sudolist.copy()
      pro = amazing.remove(id)
      i += str(pro)
      x = i.split("[", "")
      xx = x.split("]", "")
      xxx = xx.split(",", "")
      heroku_var["SUDO_USERS"] = xxx
      await event.edit(f"Tʜᴇ **{name}** ɪs ʀᴇᴍᴏᴠᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ (ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ɪ ᴀᴍ ʀᴇsᴛᴀʀᴛɪɴɢ)")
    else:
      await event.edit(f"ᴛʜᴇ {name} ɪs ɴᴏᴛ ɪɴ sᴜᴅᴏ 😑😑")
    if heroku_var["SUDO_USERS"] == None:
       await event.edit(f"ᴛʜᴇ sᴜᴅᴏ ʟɪsᴛ ɪs ᴇᴍᴘʏᴛʏ 😑😑")
    
