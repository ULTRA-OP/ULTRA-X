import asyncio
import os

from ULTRA import CMD_HELP
from ULTRA.utils import admin_cmd, sudo_cmd


@bot.on(admin_cmd(pattern="repack ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="repack ?(.*)", allow_sudo=True))
async def _(event):
    a = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    b = open(input_str, "w")
    b.write(str(a.message))
    b.close()
    a = await event.reply(f"Packing into {input_str}")
    await asyncio.sleep(2)
    await a.edit(f"Uploading {input_str}")
    await asyncio.sleep(2)
    await event.client.send_file(event.chat_id, input_str)
    await a.delete()
    os.remove(input_str)


CMD_HELP.update(
    {
        "repack": ".repack <filename.extension> <reply to text>\nUse - Pack the text and send as a file."
    }
)
