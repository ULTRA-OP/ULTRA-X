# made for ULTRA-X

# ULTRA X

from ..utils import admin_cmd
@bot.on(admin_cmd(pattern='broadcast'))
async def broadcast(event):
  Pro = event.text[10:]
  async for PROBOYX in bot.iter_dialogs():
     fail = []
     succ = []
     chat = PROBOYX.id
     if PROBOYX.is_channel:
       pass
     try:
        await bot.send_message(chat, Pro)
        succ.append(1)
     except:
        fail.append(1)
        pass
  omk = len(succ)
  shit = len(fail)
  await event.edit(f' done = {omk}\n fail = {shit}')
