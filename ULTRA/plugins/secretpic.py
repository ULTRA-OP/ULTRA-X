# COPYRIGHT (C) 2021-22 BY LEGENDX22
# MADE BY LEGENDX AND MADBOY

# made for ULTRA-X

from . import *
@bot.on(admin_cmd(pattern="secretpic"))
async def oho(event):
  if not event.is_reply:
    return await event.edit('Reply to a self distructing pic !.!.!')
  k = await event.get_reply_message()
  pic = await k.download_media()
  await bot.send_file(event.chat_id, pic, caption=f"""
  OwO!! LoL, Destruction Mode Pic Destroyed!!
  Pic captured By UltraX
  """)
  await event.delete()
  
# made by legendx22 and madboy482

# made for ULTRA-X
