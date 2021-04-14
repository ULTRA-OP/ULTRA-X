# (C) 2021 by UltraX

# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482

# (C) 2021 by UltraX
import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
import ULTRA.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from ULTRA import ALIVE_NAME, CMD_HELP, CUSTOM_PMPERMIT, bot
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
from ULTRA.uniborgConfig import Config
from var import Var

ULTRA_USER = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"

from ULTRA.utils import admin_cmd

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/3825a98c29aa89fcbd2c3.png"
else:
    WARN_PIC = PMPERMIT_PIC
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
MESAG = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
      else f"__Hey There!! I'm__ **υℓтяα χ** __and I'm here to protect {ULTRA_USER}..\nDon't under estimate Me 😈😈__\n\n**\n\n"
  f"__My Master **{ULTRA_USER}** is Busy Right Now !__ \n"
  f"My Master assigned me the duty to keep a check on his PM, and I'll do it faithfully..So you're not allowed to disturb him."
  f"**If u spam, or tried anything funny, I've full permission to Block + Report you as Spam in Telegram's Server...**\n\n"
  f"**Better be Careful..**\n\n"
  f"**{WARN_PIC}**\n"
)

MADBOY = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
USER_BOT_WARN_ZERO = "HuH, I already informed u not to spam, still u did 😒😒; As a result, U r now in moi Master's BlockList + in Telegram's Spam Users' List.😊😊\n\n**GoodBye!** "
USER_BOT_NO_WARN = (
    "**PM Security by ~  υℓтяα χ**\n\nNice to see you here, but  "
    "**[{}](tg://user?id={})** is currently unavailable.\nDon't Try To Spam In My Master's PM or You'll Be Blocked + Reported Spam In Fucin Few Seconds.\n\n"
    "{}\n\n**You have** `{}/{}` **warnings...**"
    "\n\n   ~ Thank You."
)


@borg.on(admin_cmd(pattern="a ?(.*)"))
@borg.on(admin_cmd(pattern="approve ?(.*)"))
async def approve_p_m(event):
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    reason = event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            if chat.id in PM_WARNS:
                del PM_WARNS[chat.id]
            if chat.id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat.id].delete()
                del PREV_REPLY_MESSAGE[chat.id]
            pmpermit_sql.approve(chat.id, reason)
            await event.edit(
                "Approved [{}](tg://user?id={}) to PM you.".format(firstname, chat.id)
            )
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
            await asyncio.sleep(3)
            await event.delete()


# Approve outgoing


@bot.on(events.NewMessage(outgoing=True))
async def you_dm_niqq(event):
    if event.fwd_from:
        return
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            if not chat.id in PM_WARNS:
                pmpermit_sql.approve(chat.id, "outgoing")
                madboi = "**Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇᴅ Bᴄᴜᴢ ᴏᴜᴛɢᴏɪɴɢ ʕ•ᴥ•ʔ**"
                rko = await borg.send_message(event.chat_id, madboi)
                await asyncio.sleep(3)
                await rko.delete()


@borg.on(admin_cmd(pattern="block ?(.*)"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if chat.id == 1100231654:
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
            await event.edit("You fuckin Nubb Nibba, U r tryin to block My Master **LEGEND X**, HuH??\n\nGoodBye for 100 seconds! 💤")
            await asyncio.sleep(100)
        elif chat.id == 1078841825:
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
          await event.edit("You fuckin Nubb Nibba, U r tryin to block My Master **😼°『ᴍᴇᴏᴡ ᴀʀᴍʏ』°😼**, HuH??\n\nGoodBye for 100 seconds! 💤")
          await asyncio.sleep(100)
        elif chat.id == 1695676469:
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
          await event.edit("You fuckin Nubb Nibba, U r tryin to block My Master **╚» Alain «╝**, HuH??\n\nGoodBye for 100 seconds! 💤")
          await asyncio.sleep(100)
        elif chat.id == 1037581197:
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
          await event.edit("You fuckin Nubb Nibba, U r tryin to block My Master **Devil**, HuH??\n\nGoodBye for 100 seconds! 💤")
          await asyncio.sleep(100)
# proboy's id pending....
        else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(
                    "Get lost retard.\nBlocked [{}](tg://user?id={})".format(
                        firstname, chat.id
                    )
                )
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))


@borg.on(admin_cmd(pattern="da ?(.*)"))
@borg.on(admin_cmd(pattern="disapprove ?(.*)"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if chat.id == 1100231654:
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
          await event.edit("Sorry, I Can't Disapprove My Developer")
        elif chat.id == 1078841825:
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
          await event.edit("Sorry, I Can't Disapprove My Developer")
        elif chat.id == 1695676469:
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
          await event.edit("Sorry, I Can't Disapprove My Developer")
        elif chat.id == 1037581197:
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
          await event.edit("Sorry, I Can't Disapprove My Developer")
# proboy's id pending....
        else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(
                    "Disapproved [{}](tg://user?id={}) to PM you.".format(
                        firstname, chat.id
                    )
                )
            await asyncio.sleep(3)
            await event.delete()

# (C) 2021 by UltraX

@borg.on(admin_cmd(pattern="listapproved"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    approved_users = pmpermit_sql.get_all_approved()
    APPROVED_PMs = "**υℓтяα χ Currently Approved PMs**\n"
    if len(approved_users) > 0:
        for a_user in approved_users:
            if a_user.reason:
                APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
            else:
                APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
    else:
        APPROVED_PMs = "No Approved PMs (yet)"
    if len(APPROVED_PMs) > 4095:
        with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
            out_file.name = "approved.pms.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="**υℓтяα χ Current Approved PMs**",
                reply_to=event,
            )
            await event.delete()
    else:
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
        await event.edit(APPROVED_PMs)


@bot.on(events.NewMessage(incoming=True, from_users=(1100231654)))
async def hehehe(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chats.id):
            pmpermit_sql.approve(chats.id, "**🔥😎😎🔥 God Father is Here 🔥😎😎🔥**")
            await borg.send_message(
                chats, "**Heya @LEGENDX22!! YOU ARE MY CREATOR AND HENCE I'VE APPROVED YOU SIR ❤️🥰🔥⚜️**"
            )
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
            
@bot.on(events.NewMessage(incoming=True, from_users=(1078841825)))
async def hehehe(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chats.id):
            pmpermit_sql.approve(chats.id, "**🔥Hemlo Piru Sur..🔥**")
            await borg.send_message(
                chats, "**UwU, One of moi DEVs 😼°『ᴍᴇᴏᴡ ᴀʀᴍʏ』°😼 iz Here.\n\nGood to see you here sir, I don't have enough dare to warn you...\n\nYou've been Approved, Come In Sir** ðð"
            )
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482

@bot.on(events.NewMessage(incoming=True, from_users=(1037581197)))
async def hehehe(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chats.id):
            pmpermit_sql.approve(chats.id, "**🔥Hemlo Piru Sur..🔥**")
            await borg.send_message(
                chats, "**UwU, One of moi DEVs Devil iz Here.\n\nGood to see you here sir, I don't have enough dare to warn you...\n\nYou've been Approved, Come In Sir** ðð"
            )
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482

@bot.on(events.NewMessage(incoming=True, from_users=(1695676469)))
async def hehehe(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chats.id):
            pmpermit_sql.approve(chats.id, "**🔥Hemlo Piru Sur..🔥**")
            await borg.send_message(
                chats, "**UwU, One of moi DEVs, ╚» Alain «╝ iz Here.\n\nGood to see you here sir, I don't have enough dare to warn you...\n\nYou've been Approved, Come In Sir** ðð"
            )




@bot.on(events.NewMessage(incoming=True))
async def on_new_private_message(event):
    if event.sender_id == bot.uid:
        return

    if Var.PRIVATE_GROUP_ID is None:
        return

    if not event.is_private:
        return

    message_text = event.message.message
    chat_id = event.sender_id

    message_text.lower()
    if USER_BOT_NO_WARN == message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return
    sender = await bot.get_entity(chat_id)

    if chat_id == bot.uid:

        # don't log Saved Messages

        return

    if sender.bot:

        # don't log bots

        return

    if sender.verified:

        # don't log verified accounts

        return

    if not pmpermit_sql.is_approved(chat_id):
        # pm permit
        await do_pm_permit_action(chat_id, event)

# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482

async def do_pm_permit_action(chat_id, event):
    if Var.PMSECURITY.lower() == "off":
        return
    if chat_id not in PM_WARNS:
        PM_WARNS.update({chat_id: 0})
    if PM_WARNS[chat_id] == Var.MAX_SPAM:
        r = await event.reply(USER_BOT_WARN_ZERO)
        await asyncio.sleep(3)
        await event.client(functions.contacts.BlockRequest(chat_id))
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r
        the_message = ""
        the_message += "#BLOCKED_PMs\n\n"
        the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
        the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
        # the_message += f"Media: {message_media}"
        try:
            await event.client.send_message(
                entity=Var.PRIVATE_GROUP_ID,
                message=the_message,
                # reply_to=,
                # parse_mode="html",
                link_preview=False,
                # file=message_media,
                silent=True,
            )
            return
        except BaseException:
            return
    # inline pmpermit menu
    mybot = Var.TG_BOT_USER_NAME_BF_HER
    MSG = USER_BOT_NO_WARN.format(
        DEFAULTUSER, myid, MESAG, PM_WARNS[chat_id] + 1, Var.MAX_SPAM
    )
    tele = await bot.inline_query(mybot, MSG)
    r = await tele[0].click(event.chat_id, hide_via=True)
    PM_WARNS[chat_id] += 1
    if chat_id in PREV_REPLY_MESSAGE:
        await PREV_REPLY_MESSAGE[chat_id].delete()
    PREV_REPLY_MESSAGE[chat_id] = r


# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
@bot.on(
    events.NewMessage(incoming=True, from_users=(1100231654, 1078841825, 1037581197, 1695676469))
)
async def hehehe(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chats.id):
            pmpermit_sql.approve(chats.id, "**🔥Hemlo Piru Sur..🔥**")
            await borg.send_message(
                chats, "**😎😎😎😎\nHuH?? Me iz not Sed Now, My Piru DEV iz Here\n🔥🔥🔥🔥**"
            )
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482


# instant block
NEEDIT = os.environ.get("INSTANT_BLOCK", None)
if NEEDIT == "on":

    @borg.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        event.message.message
        event.message.media
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
        event.message.id
        event.message.to_id
        chat_id = event.chat_id
        sender = await borg.get_entity(chat_id)
        if chat_id == borg.uid:
            return
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
        if sender.bot:
            return
        if sender.verified:
            return
# madboy482
# chal nikal lawde, kang krne ka try bhi mat mar
# fixed by madboy482
        if not pmpermit_sql.is_approved(chat_id):
            await borg(functions.contacts.BlockRequest(chat_id))


CMD_HELP.update(
    {
        "pmsecurity": ".approve/.a\nUse - Approve PM\
        \n\n.disapprove/.da\nUse - DisApprove PM\
        \n\n.listapproved\nUse - Get all approved PMs.\
        \n\nSet var PMPERMIT_PIC for custom PM Pic, CUSTOM_PMPERMIT for custom text, PM SECURITY <on/off> to enable/disable, INSTANT_BLOCK <on/off>.\
        \nGet help from @UltraXchaT."
    }
)

# (C) 2021 by UltraX