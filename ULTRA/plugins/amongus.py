# thanks to @Skastickers for stickers....
# Among us.....
# credits to UltraX
# madboy482


import asyncio

from ULTRA.utils import admin_cmd, edit_or_reply, sudo_cmd
from ULTRA import ALIVE_NAME, CMD_HELP

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"
LEGEND_USER = "LEGEND X"
MADBOY_USER = "««¿»» ««¿»»"
MASTER_USER = "𝕄𝔸𝕊𝕋𝔼ℝ 🇮🇳 𝕊ℍ𝔸𝔻𝕆𝕎"

@bot.on(admin_cmd(pattern="imp(|n) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="imp(|n) (.*)", allow_sudo=True))
async def _(event):
    ultrax = bot.uid
    USERNAME = f"tg://user?id={ultrax}"
    LEGEND_USERNAME = f"tg://user?id={1667146381}"
    MADBOY_USERNAME = f"tg://user?id={1732236209}"
    MASTER_USERNAME = f"tg://user?id={1630403501}"
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    text1 = await edit_or_reply(event, "𝑯𝒎𝒎... 𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝑺𝒐𝒎𝒆𝒕𝒉𝒊𝒏𝒈 𝒊𝒔 𝒘𝒓𝒐𝒏𝒈 𝒉𝒆𝒓𝒆 🤔🧐❗❗")
    await asyncio.sleep(2)
    await text1.delete()
    stcr1 = await event.client.send_file(
        event.chat_id, "CAADAQADRwADnjOcH98isYD5RJTwAg"
    )
    text2 = await event.reply(
        f"**[{DEFAULTUSER}]({USERNAME})** :\n𝑰❜𝒍𝒍 𝒉𝒂𝒗𝒆 𝒕𝒐 𝒄𝒂𝒍𝒍 𝒅𝒊𝒔𝒄𝒖𝒔𝒔𝒊𝒐𝒏 😯"
    )
    await asyncio.sleep(3)
    await stcr1.delete()
    await text2.delete()
    stcr2 = await event.client.send_file(
        event.chat_id, "CAADAQADRgADnjOcH9odHIXtfgmvAg"
    )
    text3 = await event.reply(
        f"**[{DEFAULTUSER}]({USERNAME})** :\n𝑾𝒆 𝒉𝒂𝒗𝒆 𝒕𝒐 𝒆𝒋𝒆𝒄𝒕 𝒕𝒉𝒆 𝒊𝒎𝒑𝒐𝒔𝒕𝒆𝒓 𝒐𝒓 𝒘𝒆❜𝒍𝒍 𝒍𝒐𝒔𝒆 😥"
    )
    await asyncio.sleep(3)
    await stcr2.delete()
    await text3.delete()
    stcr3 = await event.client.send_file(
        event.chat_id, "CAADAQADOwADnjOcH77v3Ap51R7gAg"
    )
    text4 = await event.reply(f"**[{MASTER_USER}]({MASTER_USERNAME})** :\n𝙒𝙝𝙚𝙧𝙚 ❓❓❓❓ 🤨 ")
    await asyncio.sleep(3)
    await text4.edit(f"**[{MADBOY_USER}]({MADBOY_USERNAME})** :\n𝙒𝙝𝙤 ❓❓❓ 🧐 ")
    await asyncio.sleep(3)
    await text4.edit(f"**[{LEGEND_USER}]({LEGEND_USERNAME})** :\n𝙆𝙤𝙣 𝙝𝙖𝙞 𝘽𝘾 ❓❓ 🖕🤔 ")
    await asyncio.sleep(3)
    await text4.edit(
        f"**[{DEFAULTUSER}]({USERNAME})** :\n𝙄𝙩𝙨 {name}, 𝙄 𝙨𝙖𝙬 {name} 𝙪𝙨𝙞𝙣𝙜 𝙩𝙝𝙚 𝙫𝙚𝙣𝙩...🤨🤨"
    )
    await asyncio.sleep(3)
    await text4.edit(f"**Others** :\n𝙊𝙠𝙖𝙮.. 😲 𝙑𝙤𝙩𝙚 {name} ")
    await asyncio.sleep(2)
    await stcr3.delete()
    await text4.delete()
    stcr4 = await event.client.send_file(
        event.chat_id, "CAADAQADLwADnjOcH-wxu-ehy6NRAg"
    )
    okevent = await event.reply(f"{name} 𝒘𝒂𝒔 𝒆𝒋𝒆𝒄𝒕𝒆𝒅.......🤐")
    await asyncio.sleep(2)
    await okevent.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await okevent.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await okevent.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await okevent.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await okevent.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await okevent.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await okevent.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await asyncio.sleep(0.5)
    await okevent.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await asyncio.sleep(0.5)
    await okevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await asyncio.sleep(0.5)
    await okevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await asyncio.sleep(0.2)
    await stcr4.delete()
    if cmd == "":
        await okevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ{name} 𝒘𝒂𝒔 𝒂𝒏 𝑰𝒎𝒑𝒐𝒔𝒕𝒆𝒓.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 𝑰𝒎𝒑𝒐𝒔𝒕𝒐𝒓 𝒓𝒆𝒎𝒂𝒊𝒏𝒔    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        await asyncio.sleep(4)
        await okevent.delete()
        await event.client.send_file(event.chat_id, "CAADAQADLQADnjOcH39IqwyR6Q_0Ag")
    elif cmd == "n":
        await okevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ{name} 𝒘𝒂𝒔𝒏❜𝒕 𝒂𝒏 𝑰𝒎𝒑𝒐𝒔𝒕𝒆𝒓.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 𝑰𝒎𝒑𝒐𝒔𝒕𝒐𝒓 𝒓𝒆𝒎𝒂𝒊𝒏𝒔    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        await asyncio.sleep(4)
        await okevent.delete()
        await event.client.send_file(event.chat_id, "CAADAQADQAADnjOcH-WOkB8DEctJAg")


@bot.on(admin_cmd(pattern="timp(|n) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="timp(|n) (.*)", allow_sudo=True))
async def _(event):
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    okevent = await edit_or_reply(event, f"{name} 𝒘𝒂𝒔 𝒆𝒋𝒆𝒄𝒕𝒆𝒅.......")
    await asyncio.sleep(2)
    await okevent.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await okevent.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await okevent.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await okevent.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await okevent.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await okevent.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await okevent.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await asyncio.sleep(0.8)
    await okevent.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await asyncio.sleep(0.8)
    await okevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await asyncio.sleep(0.8)
    await okevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await asyncio.sleep(0.2)
    if cmd == "":
        await okevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} 𝒘𝒂𝒔 𝒂𝒏 𝑰𝒎𝒑𝒐𝒔𝒕𝒆𝒓.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 𝑰𝒎𝒑𝒐𝒔𝒕𝒐𝒓 𝒓𝒆𝒎𝒂𝒊𝒏𝒔    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
    elif cmd == "n":
        await okevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} 𝒘𝒂𝒔𝒏❜𝒕 𝒂𝒏 𝑰𝒎𝒑𝒐𝒔𝒕𝒆𝒓.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 𝑰𝒎𝒑𝒐𝒔𝒕𝒐𝒓 𝒓𝒆𝒎𝒂𝒊𝒏𝒔    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )


CMD_HELP.update(
    {
        "imposter": "**Plugin :** `imposter__`\
\n\n**Syntax : **`.imp` / `.impn` <text>\
\n**Usage : ** Find imposter with stickers.\
\n\n**Syntax : **`.timp` / `.timpn` <text>\
\n**Usage : ** Find imposter only text."
    }
)

# thanks to @Skastickers for stickers....
# Among us.....
# credits to UltraX
# madboy482
