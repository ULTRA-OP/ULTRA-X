# MADE BY LEGENDX22 AND PROBOYX
#CREDITS TELEBOT
# KEEP CREDITS PLEASE 🥺
import asyncio
from userbot.legend import NAME
from userbot import CMD_HELP
from userbot.utils import admin_cmd, sudo_cmd
# By (@proboy22), and (@LEGENDX22)
from userbot import bot
PRO = NAME
@bot.on(admin_cmd("devilfban ?(.*)"))
@bot.on(sudo_cmd("devilfban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"**𝚂𝚝𝚊𝚛𝚝𝚒𝚗𝚐 𝙳𝚎𝚟𝚒𝚕𝙵𝚋𝚊𝚗 𝙱𝚢 {PRO}**...")
    fedList = []
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await bot.download_media(
                previous_message, "fedlist"
            )
            await asyncio.sleep(6)
            file = open(downloaded_file_name, "r")
            lines = file.readlines()
            for line in lines:
                try:
                    fedList.append(line[:36])
                except BaseException:
                    pass
            arg = event.text.split(" ", maxsplit=2)
            if len(arg) > 2:
                FBAN = arg[1]
                REASON = arg[2]
            else:
                FBAN = arg[1]
                REASON = " #DEVILFBANNED 🔥 "
        else:
            FBAN = previous_message.sender_id
            REASON = event.text.split(" ", maxsplit=1)[1]
            if REASON.strip() == "":
                REASON = " #DEVILFBANNED 🔥"
    else:
        arg = event.text.split(" ", maxsplit=2)
        if len(arg) > 2:
            FBAN = arg[1]
            REASON = arg[2]
        else:
            FBAN = arg[1]
            REASON = " #DEVILFBANNED 🔥 "
    try:
        int(FBAN)
        if int(FBAN) == 1513257955 or int(FBAN) == 1037581197:
            await event.edit("BHAAG BETICHOD APNE BAAP KO FBAN DEGA")
            return
    except BaseException:
        if FBAN == "@lucifermorningstarbackup" or FBAN == "@luciifeermorningstar":
            await event.edit("NIKAL LAWDE TUJHE HI SUPER FBAN KRRAHAHU.")
            return
    if Config.FBAN_GROUP_ID:
        chat = Config.FBAN_GROUP_ID
    else:
        chat = await event.get_chat()
    if not len(fedList):
        for a in range(3):
            async with bot.conversation("@MissRose_bot") as bot_conv:
                await bot_conv.send_message("/start")
                await bot_conv.send_message("/myfeds")
                await asyncio.sleep(3)
                response = await bot_conv.get_response()
                await asyncio.sleep(3)
                if "make a file" in response.text:
                    await asyncio.sleep(6)
                    await response.click(0)
                    await asyncio.sleep(6)
                    fedfile = await bot_conv.get_response()
                    await asyncio.sleep(3)
                    if fedfile.media:
                        downloaded_file_name = await bot.download_media(
                            fedfile, "fedlist"
                        )
                        await asyncio.sleep(6)
                        file = open(downloaded_file_name, "r")
                        lines = file.readlines()
                        for line in lines:
                            try:
                                fedList.append(line[:36])
                            except BaseException:
                                pass
                    else:
                        return
                if len(fedList) == 0:
                    await event.edit(f"𝚠𝚊𝚒𝚝 𝙼𝙰𝚂𝚃𝙴𝚁 𝙸 𝙰𝙼 𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 {PRO} 𝙰𝙻𝙻 𝙵𝙴𝙳𝚂 𝙶𝙸𝚅𝙴 𝙼𝙴 𝚃𝙸𝙼𝙴 ({a+1}/3)...")
                else:
                    break
        else:
            await event.edit(f"Error")
        if "You can only use fed commands once every 5 minutes" in response.text:
            await event.edit("Try again after 5 mins.")
            return
        In = False
        tempFedId = ""
        for x in response.text:
            if x == "`":
                if In:
                    In = False
                    fedList.append(tempFedId)
                    tempFedId = ""
                else:
                    In = True

            elif In:
                tempFedId += x
        if len(fedList) == 0:
            await event.edit("Something went wrong.")
            return
    await event.edit(f"𝙳𝚎𝚟𝚒𝚕𝚏𝚋𝚊𝚗𝚗𝚒𝚗𝚐 IN {len(fedList)} BY {PRO} 🔥.")
    try:
        await bot.send_message(chat, f"/start")
    except BaseException:
        await event.edit("FBAN_GROUP_ID is incorrect.")
        return
    await asyncio.sleep(3)
    if Config.EXCLUDE_FED:
        excludeFed = Config.EXCLUDE_FED.split("|")
        for n in range(len(excludeFed)):
            excludeFed[n] = excludeFed[n].strip()
    exCount = 0
    for fed in fedList:
        if Config.EXCLUDE_FED and fed in excludeFed:
            await bot.send_message(chat, f"{fed} Excluded.")
            exCount += 1
            continue
        await bot.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(3)
        await bot.send_message(chat, f"/fban {FBAN} {REASON}")
        await asyncio.sleep(3)
    await event.edit(
        f"SuperFBan Completed. Affected {len(fedList) - exCount} feds.\n#DEVIL BOT"
    )


# By @HeisenbergTheDanger, @its_xditya
# MODIFIED BY PROBOYX 


@bot.on(admin_cmd("devilunfban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"**STARTING 𝙳𝙴𝚅𝙸𝙻 UNFBANNING BY {PRO}**...")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        FBAN = previous_message.sender_id
    else:
        FBAN = event.pattern_match.group(1)

    if Config.FBAN_GROUP_ID:
        chat = Config.FBAN_GROUP_ID
    else:
        chat = await event.get_chat()
    fedList = []
    for a in range(3):
        async with bot.conversation("@MissRose_bot") as bot_conv:
            await bot_conv.send_message("/start")
            await bot_conv.send_message("/myfeds")
            response = await bot_conv.get_response()
            if "make a file" in response.text:
                await asyncio.sleep(3)
                await response.click(0)
                fedfile = await bot_conv.get_response()
                if fedfile.media:
                    downloaded_file_name = await bot.download_media(
                        fedfile, "fedlist"
                    )
                    file = open(downloaded_file_name, "r")
                    lines = file.readlines()
                    for line in lines:
                        fedList.append(line[: line.index(":")])
                else:
                    return
                if len(fedList) == 0:
                    await event.edit(f"FINDING {PRO} ALL FEDS GIVE ME SOME TIME({a+1}/3)...")
                else:
                    break
    else:
        await event.edit(f"Error")
    if "You can only use fed commands once every 5 minutes" in response.text:
        await event.edit("Try again after 5 mins.")
        return
    In = False
    tempFedId = ""
    for x in response.text:
        if x == "`":
            if In:
                In = False
                fedList.append(tempFedId)
                tempFedId = ""
            else:
                In = True

        elif In:
            tempFedId += x

    await event.edit(f"UNFBANNING IN {len(fedList)} FEDS BY {PRO}.")
    try:
        await bot.send_message(chat, f"/start")
    except BaseException:
        await event.edit("FBAN_GROUP_ID is incorrect.")
        return
    await asyncio.sleep(5)
    for fed in fedList:
        await bot.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(5)
        await bot.send_message(chat, f"/unfban {FBAN}")
        await asyncio.sleep(5)
    await event.edit(f"𝙳𝚎𝚟𝚒𝚕UnFBan Completed. Affected {len(fedList)} Feds by {PRO}.\n#DEVILBOT")


# By TEAMLEGEND
# OWNED BY TELEBOT

CMD_HELP.update(
    {
        "superban": ".superfban <username/userid> <reason>\
        \n**Usage**: Mass-Ban in all feds you are admin in.\
        \nSet `EXCLUDE_FED fedid1|fedid2` in heroku vars to exclude those feds.\
        \nSet var `FBAN_GROUP_ID` to the group with rose, where you want FBan to take place.\
        \n\nGet help - @lucifeermorningstar OR @deviluserbot."
    }
)
