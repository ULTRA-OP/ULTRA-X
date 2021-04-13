"""night Plugin for UltraX_userbot
Syntax: .study REASON"""

# ported from madboy482

# kang mat kr lawde, muh tod dunga
import asyncio
import datetime

from telethon import events
from telethon.tl import functions, types

from ULTRA import ALIVE_NAME
from ULTRA.utils import admin_cmd

global USER_night  # pylint:disable=E0602
global night_time  # pylint:disable=E0602
global last_night_message  # pylint:disable=E0602
USER_night = {}
# ported from madboy482

# kang mat kr lawde, muh tod dunga
night_time = None
last_night_message = {}

DEFAULTUSER = (str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ")


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_night(event):
    global USER_night  # pylint:disable=E0602
    global night_time  # pylint:disable=E0602
    global last_night_message  # pylint:disable=E0602
    current_message = event.message.message
# ported from madboy482

# kang mat kr lawde, muh tod dunga
    if ".night" not in current_message and "yes" in USER_night:  # pylint:disable=E0602
        try:
            await borg.send_message(  # pylint:disable=E0602
                Var.PLUGIN_CHANNEL,  # pylint:disable=E0602
                "Aʀʀᴇ BSDK Pᴀᴅʜ Lᴇ\n\n`Fᴇʀ Sᴇ Aᴀ Gʏᴀ Mᴜᴛʜ Mᴀʀɴᴇ`😂😂😂",
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PLUGIN_CHANNEL` "
                + "for the proper functioning of study command \n\n"
                + "Ask your doubts, in @UltraXchaT \n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        USER_night = {}  # pylint:disable=E0602
        night_time = None  # pylint:disable=E0602


@borg.on(admin_cmd(pattern=r"study ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    global USER_night  # pylint:disable=E0602
    global night_time  # pylint:disable=E0602
    global last_night_message  # pylint:disable=E0602
    global reason
    USER_night = {}
# ported from madboy482

# kang mat kr lawde, muh tod dunga
    night_time = None
    last_night_message = {}
    reason = event.pattern_match.group(1)
    if not USER_night:  # pylint:disable=E0602
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            night_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_night = f"yes: {reason}"  # pylint:disable=E0602
        if reason:
            await event.edit(f"Mᴏɪ Bᴏss Iᴢ Sᴛᴜᴅʏɪɴɢ\n\nDɴD")
        else:
            await event.edit(f"Mᴏɪ Bᴏss Iᴢ Gᴏɪɴɢ Tᴏ Sᴛᴜᴅʏ")
        await asyncio.sleep(5)
# ported from madboy482

# kang mat kr lawde, muh tod dunga
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                Var.PLUGIN_CHANNEL, f"Mᴏɪ Oᴡɴᴇʀ Iᴢ Sᴛᴜᴅʏɪɴɢ\n\n`Pᴜʀᴇ Dɪɴ Bᴀᴋᴄʜᴏᴅɪ Mᴀʀᴛᴀ Hᴀɪ, Aᴜʀ Aʙ Pᴀᴅʜ Rʜᴀ Hᴀɪ`"  # pylint:disable=E0602
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


@borg.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_night(event):
    if event.fwd_from:
        return
    global USER_night  # pylint:disable=E0602
    global night_time  # pylint:disable=E0602
    global last_night_message  # pylint:disable=E0602
    night_since = "**A while Ago**"
# ported from madboy482

# kang mat kr lawde, muh tod dunga
    current_message_text = event.message.message.lower()
    if "night" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_night and not (await event.get_sender()).bot:  # pylint:disable=E0602
        if night_time:  # pylint:disable=E0602
            now = datetime.datetime.now()
            datime_since_night = now - night_time  # pylint:disable=E0602
            time = float(datime_since_night.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                night_since = "**Yesterday**"
            elif days > 1:
                if days > 6:
# ported from madboy482

# kang mat kr lawde, muh tod dunga
                    date = now + datetime.timedelta(
                        days=-days, hours=-hours, minutes=-minutes
                    )
                    night_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    night_since = wday.strftime("%A")
            elif hours > 1:
                night_since = f"`{int(hours)}h {int(minutes)}m` **ago**"
            elif minutes > 0:
                night_since = f"`{int(minutes)}m {int(seconds)}s` **ago**"
            else:
# ported from madboy482

# kang mat kr lawde, muh tod dunga
                night_since = f"`{int(seconds)}s` **ago**"
        msg = None
        message_to_reply = (
            f"Mᴏɪ Bᴏss Hᴀs Bᴇᴇɴ Gᴏɴᴇ Fᴏʀ {night_since}\nWʜᴇʀᴇ Hᴇ Is: **Sᴛᴜᴅʏɪɴɢ** "
            + f"\n\n__I'ʟʟ Bᴀᴄᴋ Iɴ A Fᴇᴡ Lɪɢʜᴛ Yᴇᴀʀs__\n**"
            if reason
            else f"**::~~:: 𝑰𝒎𝒑𝒐𝒓𝒕𝒂𝒏𝒕 𝑵𝒐𝒕𝒊𝒄𝒆 ::~~::**\n\n**[{DEFAULTUSER} Is Sᴛᴜᴅʏɪɴɢ, Aɴᴅ Tᴜᴍ Bʜɪ Pᴀᴅʜᴀɪɪ Lɪᴋʜᴀɪɪ Kʀᴏ, IAS-YAS Bᴀɴᴏ...](https://telegra.ph/file/c5e851b88b539a04727aa.mp4)**"
        )
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_night_message:  # pylint:disable=E0602
            await last_night_message[event.chat_id].delete()  # pylint:disable=E0602
        last_night_message[event.chat_id] = msg  # pylint:disable=E0602

# ported from madboy482

# kang mat kr lawde, muh tod dunga
