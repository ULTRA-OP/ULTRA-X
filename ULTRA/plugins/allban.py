# originally created by legendx22

# team LEGEND
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from ULTRA.utils import admin_cmd
from ULTRA import bot, CMD_HELP


@bot.on(admin_cmd(pattern=r"allban", outgoing=True))
async def testing(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("𝗬𝗢𝗨 𝗗𝗜𝗗𝗡𝗧 𝗛𝗔𝗩𝗘 𝗦𝗨𝗙𝗙𝗜𝗖𝗜𝗘𝗡𝗧 𝗥𝗜𝗚𝗛𝗧𝗦")
        return
    await event.edit("Doing Nothing 🙃🙂")# Kang with Credits
# for ULTRA X
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
        except Exception as e:
            pass
    await event.edit("Nothing Happend here🙃🙂")

CMD_HELP.update(
    {
        "allban": "**Plugin : **`allban`\
    \n\n**Syntax : **`.allban`\
    \n**Function : **ban all members in 1 cmnd"
    }
)
