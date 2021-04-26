from ..import SUDO_USERS as sudo
from ..utils import admin_cmd
@bot.on(admin_cmd(pattern='rmsudo'))
async def remove(event):
  ok = event.text[8:]
  sudo.discard(ok)
  await event.edit("Done")
