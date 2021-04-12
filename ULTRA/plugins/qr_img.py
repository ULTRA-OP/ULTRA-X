import os

os.system("pip install qr-img")

import qr_img

from ULTRA.utils import admin_cmd
from ULTRA import bot

@bot.on(admin_cmd(pattern="qrimg ?(.*)"))
async def _(event):
    tx = event.pattern_match.group(1)
    if not tx:
        return await event.edit("Give Text")
    await event.edit("processing")
    p = await event.client.get_profile_photos(bot.me.id)
    if len(p)>=1:
       file = await bot.download_media(p[0])
    else:
       file= "  "
    out = "dc.png"
    qr_img.qrpic(event, file, tx, out)
    await bot.send_file(event.chat_id, out, force_document=False)
    await event.delete()
    
@bot.on(admin_cmd(pattern="qrmark ?(.*)"))
async def _(event):
    tx = event.pattern_match.group(1)
    r = await event.get_reply_message()
    if not (tx and r and r.media):
        return await event.edit("reply to image and Give Text")
    await event.edit("processing")
    d = await bot.download_media(r.media)
    out = "dc.png"
    qr_img.watermark_qr(event, d, tx, out)
    await bot.send_file(event.chat_id, out, force_document=False)
    await event.delete()
 
    
@bot.on(admin_cmd(pattern="qrdecode$"))
async def _(event):
    r = await event.get_reply_message()
    if not (r and r.media):
        return await event.edit("reply to image and Give Text")
    await event.edit("processing")
    image = await bot.download_media(r.media)
    tx = qr_img.qr_decode(image)
    await event.edit("Decoded Text:\n\n" + tx)
