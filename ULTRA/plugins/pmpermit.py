#    @keinshin a.k.a KeinShin

#    Copyright (C) 2020 KeinShin



#    This program is free software: you can redistribute it and/or modify

#    it under the terms of the GNU Affero General Public License as published by

#    the Free Software Foundation, either version 3 of the License, or

#    maked by LEGENDX22 🔥🔥🔥🔥 helper shivam ⚡⚡⚡

#    This program is distributed in the hope that it will be useful,

#    but WITHOUT ANY WARRANTY; without even the implied warranty of

#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

#    GNU Affero General Public License for more details.

#

#    You should have received a copy of the GNU Affero General Public License

#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os

import asyncio



from telethon import events, functions

from telethon.tl.functions.users import GetFullUserRequest



import userbot.plugins.sql_helper.pmpermit_sql as lightning_sql

from userbot import ALIVE_NAME, bot

from userbot.uniborgConfig import Config

from var import Var

LIGHTNINGUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND BOY"

from userbot.utils import admin_cmd as lightning_cmd



LIGHTNING_WRN = {}

LIGHTNING_REVL_MSG = {}



LIGHTNING_PROTECTION = os.environ.get("PM_PROTECT","yes")



SPAM = os.environ.get("SPAM", None)

if SPAM is None:

    HMM_LOL = "5"

else:

    HMM_LOL = SPAM



LIGHTNING_PM = os.environ.get("PMPERMIT_PIC", None)

CUSTOM_LIGHTNING_PM_PIC = LIGHTNING_PM

FUCK_OFF_WARN = f"**Blocked You As You Spammed {LIGHTNINGUSER}'s DM\n\n **IDC**"









OVER_POWER_WARN = (

    f"**Hello Sir Im Here To Protect {LIGHTNINGUSER} Dont Under Estimate Me 😈😈 **\n\n"

    f"`My Master {LIGHTNINGUSER} is Busy Right Now !` \n"

    f"{LIGHTNINGUSER} Is Very Busy Why Came Please Lemme Know Choose Your Deasired Reason"

    f"**Btw Dont Spam Or Get Banned** 😈 \n\n"

    f"**{CUSTOM_LIGHTNING_PM_PIC}**\n"

)



LIGHTNING_STOP_EMOJI = (

    "â"

)

if Var.PRIVATE_GROUP_ID is not None:

    @bot.on(events.NewMessage(outgoing=True))

    async def lightning_dm_niqq(event):

        if event.fwd_from:

            return

        chat = await event.get_chat()

        if event.is_private:

            if not lightning_sql.is_approved(chat.id):

                if not chat.id in LIGHTNING_WRN:

                    lightning_sql.approve(chat.id, "outgoing")

                    bruh = "Auto-approved bcuz outgoing 😗😗👍"

                    rko = await borg.send_message(event.chat_id, bruh)

                    await asyncio.sleep(3)

                    await rko.delete ()  



    @borg.on(lightning_cmd(pattern="(a|approve)"))

    async def block(event):

        if event.fwd_from:

            return

        replied_user = await borg(GetFullUserRequest(event.chat_id))

        firstname = replied_user.user.first_name

        chats = await event.get_chat()

        if event.is_private:

            if not lightning_sql.is_approved(chats.id):

                if chats.id in LIGHTNING_WRN:

                    del LIGHTNING_WRN[chats.id]

                if chats.id in LIGHTNING_REVL_MSG:

                    await LIGHTNING_REVL_MSG[chats.id].delete()

                    del LIGHTNING_REVL_MSG[chats.id]

                lightning_sql.approve(chats.id, f"Wow lucky You {LIGHTNINGUSER} Approved You")

                await event.edit(

                    "Approved to pm [{}](tg://user?id={})".format(firstname, chats.id)

                )

                await asyncio.sleep(3)

                await event.delete()



    @borg.on(lightning_cmd(pattern="block$"))

    async def lightning_approved_pm(event):

        if event.fwd_from:

            return

        replied_user = await event.client(GetFullUserRequest(event.chat_id))

        firstname = replied_user.user.first_name

        chat = await event.get_chat()

        if event.is_private:

            if lightning_sql.is_approved(chat.id):

                lightning_sql.disapprove(chat.id)

            await event.edit("Blocked [{}](tg://user?id={})".format(firstname, chat.id))

            await asyncio.sleep(2)

            await event.edit("Now Get Lost Retard [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(4)

            await event.edit("One Thing For You [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(3)

            await event.edit("ð [{}](tg://user?id={})".format(firstname, chat.id ))

            await event.client(functions.contacts.BlockRequest(chat.id))

            await event.delete()



            

    @borg.on(lightning_cmd(pattern="(da|disapprove)"))

    async def lightning_approved_pm(event):

        if event.fwd_from:

            return

        replied_user = await event.client(GetFullUserRequest(event.chat_id))

        firstname = replied_user.user.first_name

        chat = await event.get_chat()

        if event.is_private:

            if lightning_sql.is_approved(chat.id):

                lightning_sql.disapprove(chat.id)

            await event.edit("Disapproved [{}](tg://user?id={})".format(firstname, chat.id))

            await asyncio.sleep(2)

            await event.edit("Now Get Lost Retard [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(2)

            await event.edit("One Thing For You [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(2)

            await event.edit("ð [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(2)

            await event.edit(

                    "Disapproved User [{}](tg://user?id={})".format(firstname, chat.id)

                )

            await event.delete()



    



    @borg.on(lightning_cmd(pattern="listapproved$"))

    async def lightning_approved_pm(event):

        if event.fwd_from:

            return

        approved_users = lightning_sql.get_all_approved()

        PM_VIA_LIGHT = f"â¥â¿â¥ {LIGHTNINGUSER} Approved PMs\n"

        if len(approved_users) > 0:

            for a_user in approved_users:

                if a_user.reason:

                    PM_VIA_LIGHT += f"â¥â¿â¥ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"

                else:

                    PM_VIA_LIGHT += (

                        f"â¥â¿â¥ [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"

                    )

        else:

            PM_VIA_LIGHT = "no Approved PMs (yet)"

        if len(PM_VIA_LIGHT) > 4095:

            with io.BytesIO(str.encode(PM_VIA_LIGHT)) as out_file:

                out_file.name = "approved.pms.text"

                await event.client.send_file(

                    event.chat_id,

                    out_file,

                    force_document=True,

                    allow_cache=False,

                    caption="Current Approved PMs",

                    reply_to=event,

                )

                await event.delete()

        else:

            await event.edit(PM_VIA_LIGHT)



    @bot.on(events.NewMessage(incoming=True))

    async def lightning_new_msg(lightning):

        if lightning.sender_id == bot.uid:

            return



        if Var.PRIVATE_GROUP_ID is None:

            return



        if not lightning.is_private:

            return



        lightning_chats = lightning.message.message

        chat_ids = lightning.sender_id



        lightning_chats.lower()

        if OVER_POWER_WARN == lightning_chats:

            # lightning should not reply to other lightning

            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots

            return

        sender = await bot.get_entity(lightning.sender_id)

        if chat_ids == bot.uid:

            # don't log Saved Messages

            return

        if sender.bot:

            # don't log bots

            return

        if sender.verified:

            # don't log verified accounts

            return

        if LIGHTNING_PROTECTION == "NO":

            return

        if lightning_sql.is_approved(chat_ids):

            return

        if not lightning_sql.is_approved(chat_ids):

            # pm permit

            await lightning_goin_to_attack(chat_ids, lightning)



    async def lightning_goin_to_attack(chat_ids, lightning):

        if chat_ids not in LIGHTNING_WRN:

            LIGHTNING_WRN.update({chat_ids: 0})

        if LIGHTNING_WRN[chat_ids] == 3:

            lemme = await lightning.reply(FUCK_OFF_WARN)

            await asyncio.sleep(3)

            await lightning.client(functions.contacts.BlockRequest(chat_ids))

            if chat_ids in LIGHTNING_REVL_MSG:

                await LIGHTNING_REVL_MSG[chat_ids].delete()

            LIGHTNING_REVL_MSG[chat_ids] = lemme

            lightn_msg = ""

            lightn_msg += "#Some Retards ð\n\n"

            lightn_msg += f"[User](tg://user?id={chat_ids}): {chat_ids}\n"

            lightn_msg += f"Message Counts: {LIGHTNING_WRN[chat_ids]}\n"

            # lightn_msg += f"Media: {message_media}"

            try:

                await lightning.client.send_message(

                    entity=Var.PRIVATE_GROUP_ID,

                    message=lightn_msg,

                    # reply_to=,

                    # parse_mode="html",

                    link_preview=False,

                    # file=message_media,

                    silent=True,

                )

                return

            except BaseException:

                  await  lightning.edit("Something Went Wrong")

                  await asyncio.sleep(2) 

            return



        # Inline

        lightningusername = Var.TG_BOT_USER_NAME_BF_HER

        LIGHTNING_L = OVER_POWER_WARN.format(

        LIGHTNINGUSER, LIGHTNING_STOP_EMOJI, LIGHTNING_WRN[chat_ids] + 1, HMM_LOL

        )

        lightning_hmm = await bot.inline_query(lightningusername, LIGHTNING_L)

        new_var = 0

        yas_ser = await lightning_hmm[new_var].click(lightning.chat_id)

        LIGHTNING_WRN[chat_ids] += 1

        if chat_ids in LIGHTNING_REVL_MSG:

           await LIGHTNING_REVL_MSG[chat_ids].delete()

        LIGHTNING_REVL_MSG[chat_ids] = yas_ser







@bot.on(events.NewMessage(incoming=True, from_users=(1100231654)))

async def krish_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not lightning_sql.is_approved(chats.id):

            lightning_sql.approve(chats.id, "**GOD FATHER IS HERE**")

            await borg.send_message(

                chats, "**Heya @LEGENDX22 YOU ARE MY CREATOR I APPROVED YOU SIR ❤️🥰🔥⚜️**"

            )





@bot.on(

    events.NewMessage(incoming=True, from_users=(1100231654))

)

async def krish_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not lightning_sql.is_approved(chats.id):

            lightning_sql.approve(chats.id, "**Heya Sir**")

            await borg.send_message(

                chats, f"**Good To See You @LEGENDX22 How Can I Disapprove You Come In Sir**ðð"

            )

            print("Dev Here")

@bot.on(

    events.NewMessage(incoming=True, from_users=(1100231654))

)

async def krish_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not lightning_sql.is_approved(chats.id):

            lightning_sql.approve(chats.id, "**Heya Sir**")

            await borg.send_message(

                chats, f"**Good To See You master. How Can I Disapprove You Come In Sir**ðð"

            )            

@bot.on(

    events.NewMessage(incoming=True, from_users=(1100231654))

)

async def krish_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not lightning_sql.is_approved(chats.id):

            lightning_sql.approve(chats.id, "**Heya Sir**")

            await borg.send_message(

                chats, f"**Good To See You . How Can I Disapprove You Come In Sir**ðð"

            )               

            print("Dev Here")

            

            

@bot.on(

    events.NewMessage(incoming=True, from_users=(1100231654))

)

async def krish_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not lightning_sql.is_approved(chats.id):

            lightning_sql.approve(chats.id, "**Heya Sir**")

            await borg.send_message(

                chats, f"**Good To See You master. How Can I Disapprove You Come In Sir**ðð"

            )               

            print("Dev Here")

