# pastebin for catuserbot
from ULTRA.utils import admin_cmd, sudo_cmd
import os
from ULTRA import CMD_HELP
import pygments
import requests
from pygments.formatters import ImageFormatter
from pygments.lexers import Python3Lexer
from requests import exceptions, get
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


def progress(current, total):
    logger.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )
from ULTRA.utils import admin_cmd, sudo_cmd

@bot.on(admin_cmd(pattern="neko(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="neko(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "`Pasting to neko bin.....`")
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    if input_str:
        message = input_str
        downloaded_file_name = None
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message,
                Config.TEMP_DIR,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            try:
                for m in m_list:
                    message += m.decode("UTF-8")
            except Exception:
                message = (
                    "**Usage : **`.neko <long text to include/reply to text file>`"
                )
            os.remove(downloaded_file_name)
        else:
            downloaded_file_name = None
            message = previous_message.message
    else:
        downloaded_file_name = None
        message = "**Usage : **`.neko <long text to include/reply to text file>`"
    if downloaded_file_name and downloaded_file_name.endswith(".py"):
        py_file = ".py"
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}{py_file}"
    else:
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
    reply_text = f"**Pasted to Nekobin :** [Neko]({url})\n**Raw url :** [Raw](https://nekobin.com/raw/{key})\n\n**𝑷𝒂𝒔𝒕𝒆𝒅 𝒂𝒏𝒅 𝑼𝒑𝒍𝒐𝒂𝒅𝒆𝒅 𝒕𝒐 𝑵𝒆𝒌𝒐𝑩𝒊𝒏 𝒃𝒚 υℓтяα χ**"
    await catevent.edit(reply_text)

@bot.on(admin_cmd(pattern="pcode(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="pcode(?: |$)(.*)"))
async def code_print(event):
    if event.fwd_from:
        return
    reply_to = await reply_id(event)
    catevent = await edit_or_reply(event, "`Printing the text on blank page...`")
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    text_to_print = ""
    if reply:
        mediatype = media_type(reply)
        if mediatype == "Document":
            d_file_name = await event.client.download_media(reply, "./temp/")
            f = open(d_file_name, "r")
            text_to_print = f.read()
    if text_to_print == "":
        if input_str:
            text_to_print = input_str
        elif event.reply_to_msg_id:
            text_to_print = reply.message
        else:
            await edit_delete(
                catevent,
                "`Either reply to document or reply to text message or give text along with command`",
            )
    pygments.highlight(
        text_to_print,
        Python3Lexer(),
        ImageFormatter(font_name="DejaVu Sans Mono", line_numbers=True),
        "out.png",
    )
    try:
        await event.client.send_file(
            event.chat_id, "out.png", force_document=False, reply_to=reply_to
        )
    except Exception as e:
        await edit_delete(catevent, str(e), parse_mode=parse_pre)
    await catevent.delete()
    os.remove("out.png")
    os.remove(d_file_name)

CMD_HELP.update(
    {
        "neko":
        "\n\n•  **Syntax : **`.neko <text/reply>`\
        \n•  **Function : **__Create a paste or a shortened url using nekobin __`https://nekobin.com`\
        \n\n•  **Syntax : **`.pcode reply/input`\
        \n•  **Function : **__Will paste the entire text on the blank page and will send as image__\
    "
    }
)
        
 
