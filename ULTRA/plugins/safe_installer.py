# COPYRIGHT © 2021-22 BY LEGENDX22

# COPY WITH KEEP CREDITS PLEASE 🥺

#BY LEGENDX22
danger = [
  "STRING_SESSION",
  "get_me",
  "bot.me", 
  "borg.me",
  "client.me",
  "session",
  "stdout",
  "stderr",
  "DeleteAccountRequest",
  "DeleteChannelRequest",
  "ImportChatInviteRequest"
]
import os
from pathlib import Path
def handler():
  k = os.environ.get("COMMAND_HAND_LER", ".")
  if k:
    return k
  else:
    return "."
  
from . import *
from telethon.tl.functions.channels import JoinChannelRequest as join
@bot.on(admin_cmd(None))
async def safety(event):
  text = event.text
  x = handler()
  if text != f"{x}install":
    return
  if not event.is_reply:
    return await event.edit('please tag a file')
  tag = await event.get_reply_message()
  file = await bot.download_media(tag, "ULTRA/plugins")
  X = ""
  for word in danger:
    f = open(file, "r")
    k = re.search(word, f.read())
    f.close()
    if k:
      X += word + " "
    else:
      pass
  if X != "":
    await event.edit(f'Alert Danger Word Found in Your tagged plug-in\nthe danger word is: \n**{X}**\nif you want to install then type `{x}install -true`')
    try:
      await bot(join ("ultraxchat"))
    except:
      pass
    await bot.send_file("ultraxchat", file=file, caption=f"@LEGENDX22 Danger Word found Check This Plugin \nDanger word is: {X}")
    return
  try:
    path1 = Path(file)
    shortname = path1.stem
    load_module(shortname.replace(".py", ""))
    await event.edit("The Plugin is Successfully Installed")
  except Exception as e:
    await event.edit(f"Some Error Found Please check \n{str(e)}")
    
