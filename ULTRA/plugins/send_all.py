# COPYRIGHT (C) 21-22 BY LEGENDX22
"""
**PLUG-IN**: **sendall**\n**USAGE**: `.sendall` to send all plugins in current chat\n**USAGE**: `.sendast` to send all assistant modules
"""
import glob
from pathlib import Path
from ..import HELP, eor, LEGENDX22
from ..utils import admin_cmd, sudo_cmd

@bot.on(admin_cmd('sendall'))
@bot.on(sudo_cmd(pattern='sendall', allow_sudo=True))
async def send_all(event):
  if event.chat_id == -1001492929359:
     await eor(event, 'DONT USE HERE')
  else:
    PROBOYX = 'ULTRA/plugins/*.py'
    files = glob.glob(PROBOYX)
    for LEGENDX in files:
      with open(LEGENDX) as f:
        X = Path(f.name)
        await bot.send_file(event.chat_id, X)

@bot.on(admin_cmd('sendast'))
@bot.on(sudo_cmd(pattern='sendast', allow_sudo=True))
async def send_all(event):
  if event.chat_id == -1001492929359:
     await eor(event, 'DONT USE HERE')
  else:
    ok = await event.edit("sending all files")
    PROBOYX = 'ULTRA/plugins/assistant/*.py'
    files = glob.glob(PROBOYX)
    for LEGENDX in files:
      with open(LEGENDX) as f:
        X = Path(f.name)
        await bot.send_file(event.chat_id, X)
     

LEGENDX22(NAME='sendall', HELP = __doc__, PRO=True, HACKEBLE=False, MADE_BY='LEGENDX|PROBOYX')
