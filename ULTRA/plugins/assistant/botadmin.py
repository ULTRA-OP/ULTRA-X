from ULTRAX import xbot, devs as DEVS

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
)
from telethon import events
from telethon.tl import functions
from telethon.tl import types
PP_TOO_SMOL = "`The image is too small`"
PP_ERROR = "`Failure while processing the image`"
NO_ADMIN = "`I am not an admin nub nibba!`"
NO_PERM = (
    "`I don't have sufficient permissions! This is so sed. Pls Promote Me!`"
)
NO_SQL = "`Running on Non-SQL mode!`"

CHAT_PP_CHANGED = "`Chat Picture Changed`"
CHAT_PP_ERROR = (
    "`Some issue with updating the pic,`"
    "`maybe coz I'm not an admin,`"
    "`or don't have enough rights.`"
)
INVALID_MEDIA = "`Invalid Extension`"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await xbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


async def can_promote_users(message):
    result = await xbot(
        functions.channels.GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(p, types.ChannelParticipantCreator) or (
        isinstance(p, types.ChannelParticipantAdmin) and p.admin_rights.ban_users
    )


async def can_ban_users(message):
    result = await xbot(
        functions.channels.GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(p, types.ChannelParticipantCreator) or (
        isinstance(p, types.ChannelParticipantAdmin) and p.admin_rights.ban_users
    )




async def can_pin_msg(message):
    result = await xbot(
        functions.channels.GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(p, types.ChannelParticipantCreator) or (
        isinstance(p, types.ChannelParticipantAdmin) and p.admin_rights.pin_messages
    )



async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.reply("`Pass the user's username, id or reply!`")
            return
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return user_obj, extra

async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj


@xbot.on(events.NewMessage(pattern="/ban ?(.*)"))
async def ban(event):
    if not event.is_group:
        return
    if event.is_group:
        if not await can_ban_users(message=event):
            return
    user, reason = await get_user_from_event(event)
    
    banned = await xbot.get_permissions(event.chat_id, user)
    pro = user
    fname = pro.first_name
    if banned.is_admin:
        await event.reply("Oh, Yeah? Lets Start Banning Admins.")
        return
    if user:
        pass
    else:
        return
    if user.id in DEVS:
     await event.reply("Sorry I Can't Act Against My Devs")
     return
    try:
        await xbot(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        await event.reply("I Could't Ban That User Probably Due To Less Permissions.")
        return
    if reason:
        await event.reply(f"Banned {fname} For \nReason: {reason}")
    else:
        await event.reply(f"Banned {fname} !")

@xbot.on(events.NewMessage(pattern="/unban ?(.*)"))
async def unban(event):
    if not event.is_group:
        return
    if event.is_group:
        if not await can_ban_users(message=event):
            return
    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return
    try:
        await xbot(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
        await event.reply("`Unbanned Successfully. Granting another chance.🚶`")
    except BadRequestError:
        await event.reply("I Could't UnBan That User Probably Due To Less Permissions.")
        return


@xbot.on(events.NewMessage(pattern="/promote ?(.*)"))
async def promote(event):
    if event.is_group:
          if not await can_promote_users(message=event):
            return
    else:
        return
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=False,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    user, rank = await get_user_from_event(event)
    kekme = await serena.get_permissions(event.chat_id, user)
    if kekme.is_admin:
        await event.reply("Oh, Yeah? Promote A Admin?")
        return
    if not rank:
        rank = "Admin"
    if user:
        pass
    else:
        return
    try:
        await xbot(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
        await event.reply("Promoted Successfully! Now give Party")
    except BadRequestError:
        await event.reply(
            "I Could't Promote That User Probably Due To Less Permissions."
        )
        return


@xbot.on(events.NewMessage(pattern="/demote ?(.*)"))
async def demote(event):
    if event.is_group:
          if not await can_promote_users(message=event):
            return
    else:
        return
    rank = "Admin"
    user = await get_user_from_event(event)
    
    user = user[0]
    if user:
        pass
    else:
        return
    if user.id in DEVS:
     await event.reply("Sorry I Can't Act Against My Devs")
     return

    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, newrights, rank))
    except BadRequestError:
        await event.reply(
            "I Could't Demote That User Probably Due To Less Permissions."
        )
        return
    await event.reply("Demoted This User Sucessfully.")


@xbot.on(events.NewMessage(pattern=None))
async def pin(event):
    msg = str(event.text)
    if not msg == "/pin":
     return
    if event.is_group:
        if not await can_pin_msg(message=event):
            return
    else:
        return
    to_pin = event.reply_to_msg_id
    if not to_pin:
        await event.reply("`Reply to a message to pin it.`")
        return
    options = None
    is_silent = True
    if options.lower() == "loud":
        is_silent = False
    try:
        await xbot(UpdatePinnedMessageRequest(event.to_id, to_pin, is_silent))
    except BadRequestError:
        await event.reply(
            "I Could't Pin That Message Probably Due To Less Permissions."
        )
        return
    await event.reply("Pinned This Message Sucessfully.")
    await get_user_sender_id(event.sender_id, event)

@xbot.on(events.NewMessage(pattern="/permapin ?(.*)"))
async def pin(event):
    if event.is_group:
        if not await can_pin_msg(message=event):
            return
    else:
        return
    previous_message = await msg.get_reply_message()
    k = await xbot.send_message(
            msg.chat_id,
            previous_message
          )
    to_pin = k.id
    if not to_pin:
        await event.reply("`Reply to a message to pin it.`")
        return
    options = event.pattern_match.group(1)
    is_silent = True
    if options.lower() == "loud":
        is_silent = False
    try:
        await xbot(UpdatePinnedMessageRequest(event.to_id, to_pin, is_silent))
    except BadRequestError:
        await event.reply(
            "I Could't Pin That Message Probably Due To Less Permissions."
        )
        return
    await event.reply("Pinned This Message Sucessfully.")
    await get_user_sender_id(event.sender_id, event)


@xbot.on(events.NewMessage(pattern="/unpin"))
async def pin(msg):
    if msg.is_group:
        if not await can_pin_msg(message=msg):
            return
    try:
        c = await msg.get_reply_message()
        await xbot.unpin_message(msg.chat_id, c)
        await msg.reply("Unpinned Successfully.")
    except Exception:
        await msg.reply("Failed to unpin.")



@xbot.on(events.NewMessage(pattern="/kick ?(.*)"))
async def kick(event):
    if not event.is_group:
        return
    if event.is_group:
        if not await can_ban_users(message=event):
            return
    user, reason = await get_user_from_event(event)
    kekme = await xbot.get_permissions(event.chat_id, user)
    momos = user
    momos.first_name
    if kekme.is_admin:
        await event.reply("Oh, Yeah? Lets Start kicking Admins.")
        retur
    if not user:
        await event.reply("Mention A User")
        return
    if user.id in DEVS:
     await event.reply("Sorry I Can't Act Against My Devs")
     return
    try:
        await xbot.kick_participant(event.chat_id, user.id)
    except:
        await event.reply("I Could't Kick That User Probably Due To Less Permissions.")
        return
    if reason:
        await event.reply(
            f"`Kicked` [{user.first_name}](tg://user?id={user.id})`!`\nReason: {reason}"
        )
    else:
        await event.reply(f"`Kicked` [{user.first_name}](tg://user?id={user.id})`!`")


@xbot.on(events.NewMessage(pattern="/mute ?(.*)"))
async def mute(event):
    if not event.is_group:
        return
    if event.is_group:
        if not await can_ban_users(message=event):
            return
    user, reason = await get_user_from_event(event)
    kekme = await xbot.get_permissions(event.chat_id, user)
    momos = user
    momos.first_name
    if kekme.is_admin:
        await event.reply("Oh, Mutting? Lets Start Banning Admins.")
        retur
    if not user:
        await event.reply("Mention A User")
        return
    if user.id in DEVS:
     await event.reply("Sorry I Can't Act Against My Devs")
     return
    try:
        await xbot(EditBannedRequest(event.chat_id, user.id, MUTE_RIGHTS))
    except:
        await event.reply("I Could't Mute That User Probably Due To Less Permissions.")
        return
    if reason:
        await event.reply(
            f"`Muted` [{user.first_name}](tg://user?id={user.id})`!`\nReason: {reason}"
        )
    else:
        await event.reply(f"`Kicked` [{user.first_name}](tg://user?id={user.id})`!`")


@xbot.on(events.NewMessage(pattern="/unmute ?(.*)"))
async def mute(event):
    if not event.is_group:
        return
    if event.is_group:
        if not await can_ban_users(message=event):
            return
    user, reason = await get_user_from_event(event)
    if not user:
        await event.reply("Mention A User")
        return
    try:
        await xbot(EditBannedRequest(event.chat_id, user.id, UNMUTE_RIGHTS))
    except:
        await event.reply(
            "I Could't UnMute That User Probably Due To Less Permissions."
        )
        return
    if reason:
        await event.reply(
            f"`UnMuted` [{user.first_name}](tg://user?id={user.id})`!`\nReason: {reason}"
        )
    else:
        await event.reply(f"`Unmute` [{user.first_name}](tg://user?id={user.id})`!`")
