import heroku3
from var import Var
from ..utils import admin_cmd
LEGENDX = Var.HEROKU_APP_NAME
PROBOYX = Var.HEROKU_API_KEY
@bot.on(admin_cmd(pattern='addsudo'))
async def add_sudo(event):
  Heroku = heroku3.from_key(PROBOYX)
  app = Heroku.app(LEGENDX)
  heroku_var = app.config()
  if event.is_reply:
    id = (await event.get_reply_message()).sender_id
    name = (await bot.get_entity(id)).first_name
    if id in heroku_var:
      await event.edit(f"THE {name} IS ALREADY ON SUDO LIST")
    else:
      pass
    if heroku_var["SUDO_USERS"] == None:
       await event.edit(f"OK {name} IS ADDED ON SUDO I AM RESTARTING")
       heroku_var["SUDO_USERS"] = id
    else:
       var = heroku_var["SUDO_USERS"]
       await event.edit(f"OK {name} IS ADDED AND OLD USERS REMOVED IF YOU ADD 2 OR MORE THAN 2 USERS ON SUDO GO TO HEROKU ADD MANUALLY I AM RESTARTING")
       heroku_var["SUDO_USERS"] = id
  else:
    text = event.text.split(" ", maxsplit=1)[1]
    if text in heroku_var:
      await event.edit(f"THE {name} IS ALREADY ON SUDO LIST")
    else:
      pass
    if heroku_var["SUDO_USERS"] == None:
       await event.edit(f"OK {name} IS ADDED ON SUDO I AM RESTARTING")
       heroku_var["SUDO_USERS"] = text
    else:
       var = heroku_var["SUDO_USERS"]
       await event.edit(f"OK {name} IS ADDED AND {var} REMOVED ON SUDO I AM RESTARTING")
       heroku_var["SUDO_USERS"] = text


@bot.on(admin_cmd(pattern='rmsudo'))
async def remove_sudo(event):
  Heroku = heroku3.from_key(PROBOYX)
  app = Heroku.app(LEGENDX)
  heroku_var = app.config()
  if event.is_reply:
    id = (await event.get_reply_message()).sender_id
    name = (await bot.get_entity(id)).first_name
    if id in heroku_var:
      await event.edit(f"THE {name} IS REMOVED ON SUDO LIST")
      del heroku_var["SUDO_USERS"]
    else:
      pass
    if heroku_var["SUDO_USERS"] == None:
       await event.edit(f"SUDO LIST IS ALREADY IS Empty")
       heroku_var["SUDO_USERS"] = id
    
