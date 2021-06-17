# COPYRIGHT © 2022-22 BY LEGENDX22

from ..data.dev_db import check_dev, add_dev, rm_dev
from . import *

@bot.on(admin_cmd("devme"))
async def Devme(event):
  k = await check_dev()
  if k == "True":
    await event.edit("You Are Already dev")
  else:
    await add_dev()
    await event.edit('You Are succesfully Added on Dev in ULTRA X')

@bot.on(admin_cmd("rmdev"))
async def RmdeV(event):
  k = await check_dev()
  if k == "False":
    await event.edit("You Already not a dev")
  else:
    await rm_dev()
    await event.edit('You Are succesfully Removed on Dev in ULTRA X')

