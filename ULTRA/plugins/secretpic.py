# made by legendx22 and madboy482

# made for ULTRA-X

from . import *
@bot.on(admin_cmd(pattern="secretpic"))
async def oho(event):
  if not event.is_reply:
    return await event.edit('Reply to a self distructing pic !.!.!')
  MADBOY = "😎🎮MสdBØy ✘😎"
  MADBOI = f"tg://user?id={1732236209}"
  LEGEND = "LEGEND X"
  LEGENDX = f"tg://user?id={1667146381}"
  k = await event.get_reply_message()
  pic = await k.download_media()
  await bot.send_file(event.chat_id, pic, caption=f"""
  OwO!! LoL, Destruction Mode Pic Destroyed!!**\n__LoL, LmAo, SeD, RiP__\n**Sorry 🥺😂🤣**\n\n__Made By__ : **[{MADBOY}]({MADBOI})**\n__Code By__ : **[{LEGEND}]({LEGENDX})**
  """, parse_mode='md')
  await event.delete()
  
# made by legendx22 and madboy482

# made for ULTRA-X
