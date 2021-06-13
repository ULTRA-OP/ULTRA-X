import os
from ULTRAX import xbot
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


@xbot.on(events.NewMessage(pattern="/id ?(.*)"))
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
    await xbot.send_message(reply_text)
