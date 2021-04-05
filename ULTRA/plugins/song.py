#    Copyright (C) 2020 LEGENDBOT

######### maked by LEGENDX22 🔥🔥🔥###################

#    This program is free software: you can redistribute it and/or modify

#    it under the terms of the GNU Affero General Public License as published by

#    the Free Software Foundation, either version 3 of the License, or

#    maked by LEGEND X by shivam help thanks LEGENDX

#    This program is distributed in the hope that it will be useful,

#    but WITHOUT ANY WARRANTY; without even the implied warranty of

#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

#    GNU Affero General Public License for more details.

#

#    You should have received a copy of the GNU Affero General Public License

#    along with this program.  If not, see <https://www.gnu.org/licenses/>.






"""Thanks To 
TEAMLEGEND
TEAMULTRA
KEINSHIN
@LEGENDX22

"""





"""Only ULTRA X and LEGEND-BOT (Can Use Without Credits) Can Use This Inline WithOut Copyright (Just Give The Credits Pls)

Thanks"""












import os
import re

import json

from math import ceil

from ULTRA.uniborgConfig import Config



from telethon import Button, custom, events, functions



from ULTRA import ALIVE_NAME, CMD_HELP, CMD_LIST, bot



from var import Var





LIGHT_LOGS = Config.PM_LOGGR_BOT_API_ID 

ultra_bot = Var.TG_BOT_USER_NAME_BF_HER

import asyncio



from datetime import datetime

from pathlib import Path





from ULTRA.utils import load_module, remove_plugin,admin_cmd as ultra_cmd



DELETE_TIMEOUT = 5





thumb_image_path = "./resources/541200.png"



ULTRA_USER = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"

ULTRAXBOT = Var.TG_BOT_TOKEN_BF_HER









 

from LEGENDX import ID
from telethon import events

BOT_MSG = os.environ.get("BOT_MSG", None)

if BOT_MSG is None:

    BOT_LIT = f"Hello Sir MySelf ULTRA X Here For {ULTRA_USER}'s Protection "

else:

    BOT_LIT = BOT_MSG   





ULTRA_WARN = os.environ.get("ULTRA_WARN", None)

if ULTRA_WARN is None:

    WARNING = (

    f"**{BOT_LIT}"

   f"__Hey There!! I'm__ **υℓтяα χ** __and I'm here to protect {ULTRA_USER}..\nDon't under estimate Me 😈😈__\n\n**\n\n"

    f"__My Master **{ULTRA_USER}** is Busy Right Now !__ \n"

    f"My Master assigned me the duty to keep a check on his PM, and I'll do it faithfully..So you're not allowed to disturb him."

    f"**If u spam, or tried anything funny, I've full permission to Block + Report you as Spam in Telegram's Server...**\n\n"

    f"**Better be Careful..**\n\n"

    f"**Choose Any Reason & Then Get Lost**\n"

)

else:

    WARNING = ULTRA_WARN



ULTRA_BOT_PIC = os.environ.get("PMPERMIT_PIC", None)

if ULTRA_BOT_PIC is None:

    ULTRA_WARNING = "https://telegra.ph/file/a44f1363bddbba84a2b98.jpg"

else:

    ULTRA_WARNING = ULTRA_BOT_PIC














from ULTRA import CMD_HELP

@tgbot.on(events.InlineQuery)

async def inline_handler(ultra):

    builder = ultra.builder

    result = None

    query = ultra.text

    if ultra.query.user_id == bot.uid and query.startswith("**help") or query.startswith("help"):
        print (False)
    elif ultra.query.user_id == bot.uid and query == "**Cool":

        result = builder.article(

            title="Cool",

            text=f"**How If Face Problem \n{ULTRA_USER}** \nChoose Your Problem For Help ",

            buttons=[

                [custom.Button.inline("Help ⚙️", data="what?")],

                [Button.url("Commands Not Working 🤔", "https://t.me/teamishere")],

                [Button.url("Help Article 🤔", "https://app.gitbook.com/@poxsisofficial/s/help/")],

                [

                    Button.url(

                

                    "Want To Learn CMDS ☺️☺️",

                    "https://t.me/UltraXchaT" ,

                    )

                ], 

            ],

        )

        await ultra.answer([result])

    elif ultra.query.user_id == bot.uid and query.startswith("**Hello Sir"):

        result = builder.photo(

            file=ULTRA_WARNING,

            text=WARNING,

            buttons=[

                [custom.Button.inline("Wanna Spam Something?🥺🥺", data="ultra_is_here_cant_spam")],

                [

                    custom.Button.inline(

                        "My Friend 🧐🧐",

                        data="he_sucks",

                    )

                ],

                [custom.Button.inline("Requesting ⚜️⚜️", data="fck_ask")],

                [

                    custom.Button.inline(

                        "Lemme In ;)", 

                        data="lol_u_think_so",

                        

                    )

                        

                ],



            ],

            )

        await ultra.answer([result] if result else None)

    else:

        return

    



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"what?")))

async def what(ultra):

    if ultra.query.user_id == bot.uid or ultra.query.user_id == ID:

        fck_bit = f"{ULTRA_USER}  Use The Buttons Below "

        await ultra.answer(fck_bit, alert=True)

    else:

        txt = f"Ohh!! You Think That This Is For You?\nOk I'll Complain To {ULTRA_USER} ⚜️⚜️"

        await ultra.answer(txt, alert=True)





@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ultra_is_here_cant_spam")))

async def ultra_is_better(ultra):

    if ultra.query.user_id == bot.uid:

        fck_bit = f"Oh! Master {ULTRA_USER} I'm Trying To Get Rid Of This Nigga...Pls Dont Touch!!"

        await ultra.answer(fck_bit, cache_time=0, alert=True)

        return

    await ultra.get_chat()

    ultra_id = ultra.query.user_id

    text1 = f"LOL **You Think So You Can**😂\n\n**[Nibba](tg://user?id={ultra_id}) Bye Goin To Block You Gay**😈😈"

    await ultra.edit("Off Course Go To Hell Dude")

    await bot.send_message(ultra.query.user_id, text1)

    await bot(functions.contacts.BlockRequest(ultra.query.user_id))

    await ultra.edit("😈")

    await bot.send_message(

        LIGHT_LOGS,

        f"Hey Master Sorry Disturb You, [Noob](tg://user?id={ultra_id}) Tryin To Spam 🥺\n\n**So Blocked**.",

    )



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lol_u_think_so")))

async def ultra_is_better(ultra):

    if ultra.query.user_id == bot.uid:

        fck_bit = f"Oh! C'mon Master {ULTRA_USER} Im Try To Get Rid Of This Nigga Pls Dont Touch"

        await ultra.answer(fck_bit, cache_time=0, alert=True)

        return

    await ultra.get_chat()

    ultra_id = ultra.query.user_id

    text1 = f"LOL You Think So You Can😂😂\nGo and wait🥴🥴"

    await ultra.edit("Off Course Go To Hell Dudeð😑")

    await bot.send_message(ultra.query.user_id, text1)

    await bot(functions.contacts.BlockRequest(ultra.query.user_id))

    await bot.send_message(

        LIGHT_LOGS,

        f"Hey Master Sorry Disturb You, [Noob](tg://user?id={ultra_id}) Tryin To Enter With Out approvalð \n.",

    )











@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"he_sucks")))

async def ultra_is_better(ultra):

    if ultra.query.user_id == bot.uid:

        fck_bit = f"Oh! C'mon Master {ULTRA_USER} Im Try To Get Rid Of This Nigga Pls Dont Touch"

        await ultra.answer(fck_bit, cache_time=0, alert=True)

        return

    await ultra.get_chat()

    ultra_id = ultra.query.user_id

    await ultra.edit("Oh You Wanna Talk With My Master\n\nPls Wait Dear \n\n**Btw** **You Can Wait For My Master**")

    await asyncio.sleep(2)

    await ultra.edit(

        "Name Which Type Of Friend?", buttons= [

        [Button.inline("School", data="school")],

        [Button.inline("Tg Causal Friend", data="tg_okay")],

        ], 

    )

    light_text = "`Warning`- 😈😈Dont Try Anything Stupid  Wait Kindly!!!😈😈"

    await bot.send_message(ultra.query.user_id, light_text)

    

    

    

    

    

    

    

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"tg_okay")))

async def yeahbaba(ultra):

        if ultra.query.user_id == bot.uid:

            fck_bit = f"Oh! C'mon Master {ULTRA_USER} "

            await ultra.answer(fck_bit, cache_time=0, alert=True)

            return

        light_text = "**So You  Are TG Friend** Okay wait"

        ultra_id = ultra.query.user_id

        await asyncio.sleep(2)

        await ultra.edit(f"`Informing To Master {ULTRA_USER}`")

        await asyncio.sleep(2)

        await ultra.edit("`Done Informed`")

        await bot.send_message(ultra.query.user_id, light_text)

        await bot.send_message(

        LIGHT_LOGS,

        message=f"Hello, Master  [Friend](tg://user?id={ultra_id}). Your Casual Telegram Friend His Here To Chat pls See The Message [Tg Friend](tg://user?id={ultra_id}) Is Waiting.",

    

    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"School")))

async def yeahbaba(ultra):

        if ultra.query.user_id == bot.uid:

            fck_bit = f"Oh! C'mon Master {ULTRA_USER} "

            await ultra.answer(fck_bit, cache_time=0, alert=True)

            return

        light_text = "**So You  Are  Friend** Okay wait"

        ultra_id = ultra.query.user_id

        await asyncio.sleep(2)

        await ultra.edit(f"`Informing To Master {ULTRA_USER}`")

        await asyncio.sleep(2)

        await ultra.edit("`Done Informed`")

        await bot.send_message(ultra.query.user_id, light_text)

        await bot.send_message(

        LIGHT_LOGS,

        message=f"Hello, Master  [Friend](tg://user?id={ultra_id}). Your Casual Telegram Friend His Here To Chat pls See The Message [Tg Friend](tg://user?id={ultra_id}) Is Waiting.",

        )





@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fck_ask")))

async def ultra_is_better(ultra):

    if ultra.query.user_id == bot.uid:

        fck_bit = f"Oh! C'mon Master {ULTRA_USER} Im Try To Get Rid Of This Nigga Pls Dont Touch"

        await ultra.answer(fck_bit, cache_time=0, alert=True)

        return

    await ultra.get_chat()

    ultra_id = ultra.query.user_id

    await ultra.edit("Okay let Me Think🤔🤔«")

    await asyncio.sleep(2)

    await ultra.edit("Okay Giving You A Chance🧐¨")

    await asyncio.sleep(2)

    await ultra.edit(

        "You Will Spam?", buttons= [

        [Button.inline("Yes", data="lemme_ban")],

        [Button.inline("No", data="hmm")],

        ],

    )



    

    reqws = "`Warning`- 😈😈Dont Try Anything Stupid  Wait Kindly!!!😈😈"





    await bot.send_message(ultra.query.user_id, reqws)

    await bot.send_message(

        LIGHT_LOGS,

        message=f"Hello, Master  [Nibba](tg://user?id={ultra_id}). Wants To Request Something.",

        buttons=[Button.url("Contact Him", f"tg://user?id={ultra_id}")],

    )



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hmm")))

async def yes_ucan(ultra):

    if ultra.query.user_id == bot.uid:

           lmaoo = "You Are Not Requesting , Lol."

           await ultra.answer(lmaoo, cache_time=0, alert=True)

           return          

    await ultra.get_chat()

    await asyncio.sleep(2)

    await ultra.edit("Okay You Can Wait Till Wait")

    hmmmmm = "Okay Kindly wait  i will inform you"

    await bot.send_message(

              ultra.query.user_id, hmmmmm)

          

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))

async def yes_ucan(ultra):

    if ultra.query.user_id == bot.uid:

           lmaoo = "You Are Not Requesting , Lol."

           await ultra.answer(lmaoo, cache_time=0, alert=True)

           return    

    await ultra.get_chat()

    await asyncio.sleep(2)

    await ultra.edit("Get Lost Retard")

    ban = "Get Lost Goin To Block You" 

    await bot.send_message(

         ultra.query.user_id, ban)

    await bot(functions.contacts.BlockRequest(ultra.query.user_id))










"""

Thanks To LEGEND BOT and @LEGENDX22 For This idea



"""
