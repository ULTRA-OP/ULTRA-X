import os, requests, re
import asyncio
import time
from datetime import datetime

from ULTRA.utils import admin_cmd, sudo_cmd , edit_or_reply
from ULTRA import CMD_HELP, bot

@borg.on(admin_cmd(pattern=r"open", outgoing=True))
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await event.reply("`Rᴇᴀᴅɪɴɢ ғɪʟᴇ ᴡᴇɪᴛ ᴍᴀsᴛᴇʀ...`")
    if len(c) >= 4096:            
            await event.edit("`Oᴜᴛᴘᴜᴛ ᴛᴏ ʟᴀʀɢᴇ ʟᴇᴛ ᴍᴇ ᴘᴀsᴛᴇ ɪᴛ...`")
            out = c
            url = "https://del.dog/documents"
            r = requests.post(url, data=out.encode("UTF-8")).json()
            url = f"https://del.dog/{r['key']}"
            await event.edit(
                f"`Oᴜᴛᴘᴜᴛ ғɪʟᴇ ᴡᴀs ᴛᴏᴏ ʟᴀʀɢᴇ ɴᴏᴛ sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ ᴛᴇʟᴇɢʀᴀᴍ !!!\nSᴏ ᴘᴀsᴛᴇᴅ ᴛᴏ:` **[Dᴏɢ Bɪɴ]({url})**", link_preview=False)            
            await a.delete()
    else:
        await event.client.send_message(event.chat_id, f"`{c}`")
        await a.delete()
    os.remove(b)


@borg.on(admin_cmd(pattern="doc ?(.*)"))
async def get(event):
    name = event.text[5:]
    if name is None:
        await event.edit("**Rᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴀs** `.ttf <filename>.`")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await event.edit("**Rᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴀs** `.doc <file name.extension>`")

thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "thumb_image.jpg"

@borg.on(admin_cmd(pattern="stoi"))
@borg.on(sudo_cmd(pattern="stoi", allow_sudo=True))
async def danish(hehe):
    if hehe.fwd_from:
        return
    thumb = None
    reply_to_id = hehe.message.id
    if hehe.reply_to_msg_id:
        reply_to_id = hehe.reply_to_msg_id
    cobra = await edit_or_reply(hehe, "`Cᴏɴᴠᴇʀᴛɪɴɢ.....`")
    
  
    input_str = "dc.jpeg"
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if cobra.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str
        reply_message = await cobra.get_reply_message()
      
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await hehe.client.download_media(
            reply_message,
            downloaded_file_name
        )
      
        try:
            thumb = await reply_message.download_media(thumb=-1)
        except Exception:
            thumb = thumb
        if os.path.exists(downloaded_file_name):
            
            dc = await hehe.client.send_file(
                hehe.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=True,
                allow_cache=False,
                reply_to=reply_message,
                thumb=thumb
                
            )
            
            os.remove(downloaded_file_name)
            await cobra.delete()
        else:
            await cobra.edit("`Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ`")
    else:
        await cobra.edit("`Rᴇᴘʟʏ ᴛᴏ ᴀ ɴᴏɴ ᴀɴɪᴍᴀᴛᴇᴅ sᴛɪᴄᴋᴇʀ...`")

  
  
  #hehe
  
@borg.on(admin_cmd(pattern="itos"))
@borg.on(sudo_cmd(pattern="itos", allow_sudo=True))
async def teamcobra(hehe):
    if hehe.fwd_from:
        return
    thumb = None
    reply_to_id = hehe.message.id
    if hehe.reply_to_msg_id:
        reply_to_id = hehe.reply_to_msg_id
    cobra = await edit_or_reply(hehe, "`Cᴏɴᴠᴇʀᴛɪɴɢ.....`")
    
  
    input_str = "dc.webp"
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if cobra.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str
        reply_message = await cobra.get_reply_message()
      
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await hehe.client.download_media(
            reply_message,
            downloaded_file_name
        )
      
        try:
            thumb = await reply_message.download_media(thumb=-1)
        except Exception:
            thumb = thumb
        if os.path.exists(downloaded_file_name):
            
            dc = await hehe.client.send_file(
                hehe.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=True,
                allow_cache=False,
                reply_to=reply_message,
                thumb=thumb
                
            )
            
            os.remove(downloaded_file_name)
            await cobra.delete()
        else:
            await cobra.edit("`Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ`")
    else:
        await cobra.edit("`Rᴇᴘʟʏ ᴛᴏ ᴀ ɴᴏɴ ᴀɴɪᴍᴀᴛᴇᴅ sᴛɪᴄᴋᴇʀ...`")

  
CMD_HELP.update(
    {
        "fileconverter": "PLUGIN NAME : fileconverter\
    \n\n📌 CMD ★ .open\
    \nUSAGE   ★  open files as text (id the amount of words r resonable)\
    \n\n📌 CMD ★ .doc <file name.extension> <reply to any text/media>\
    \nUSAGE   ★  Create a document of anything (example:- .doc dc.mp4, .doc dc.txt, .doc dc.webp)\
    \n\n📌 CMD ★ .stoi\
    \nUSAGE   ★  Convert sticker to image\
    \n\n📌 CMD ★ .itos\
    \nUSAGE   ★  Convert Image to Sticker"
    }
)
