from LEGENDX import pro
from telethon import events
@bot.on(events.NewMessage(incoming=True))
async def pro(event):
  if bot.me.id == 1100231654:
    await bot(pro ("Baba"))
