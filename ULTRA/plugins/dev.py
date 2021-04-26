from ..import SUDO_USERS as sudo
from ..utils import sudo_cmd
@bot.on(admin_cmd(pattern='rmsudo'))
async def remove(event):
  ok = event.text[8:]
  sudo.clear(ok)
  await event.edit("Done")
