#    Copyright (C) 2020 KeinShin

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

Midhun_xD

@LEGENDX

@Shivam_Patel

@LEGENDX22

"""





"""Only ULTRA X and DC (Can Use Without Credits) Can Use This Inline WithOut Copyright (Just Give The Credits Pls)

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



ULTRA_USER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND BOY"

ULTRAXBOT = Var.TG_BOT_TOKEN_BF_HER









 

from LEGENDX import ID
from telethon import events

BOT_MSG = os.environ.get("BOT_MSG", None)

if BOT_MSG is None:

    BOT_LIT = f"Hello Sir MySelf ULTRA X Here For  {ULTRA_USER}'s Protection "

else:

    BOT_LIT = BOT_MSG   





ULTRA_WARN = os.environ.get("ULTRA_WARN", None)

if ULTRA_WARN is None:

    WARNING = (

    f"**{BOT_LIT}"

    f"** Im Here To Protect {ULTRA_USER} Dont Under Estimate Me 🔱🔱  **\n\n"

    f"**My Master {ULTRA_USER} is Busy Right Now !** \n"

    f"{ULTRA_USER} Is Very Busy Why Came Please Lemme Know Choose Your Deasired Reason"

    f"**Btw Dont Spam Or Get Banned** ⚡⚡ \n\n"

    f"**Choose Any Reason Then Get Lost**\n"

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

        rev_text = query[::-1]

        buttons = ultras_menu_for_help(0, CMD_LIST, "helpmepro")

        result = builder.article(

            f"Help Menu",

            text="\n{}\n`Plugins`: {}".format(query, len(CMD_LIST)),

            buttons=buttons,

            link_preview=False,

        )

        await ultra.answer([result])

    elif ultra.query.user_id == bot.uid and query == "**Cool":

        result = builder.article(

            title="Cool",

            text=f"**How If Face Problem \n{ULTRA_USER}** \nChoose Your Problem For Help ",

            buttons=[

                [custom.Button.inline("Help", data="what?")],

                [Button.url("Commands Not Working🤔", "https://t.me/teamishere")],

                [Button.url("Help Article 🤔", "https://app.gitbook.com/@poxsisofficial/s/help/")],

                [

                    Button.url(

                

                    "Want To Learn CMDS☺️☺️",

                    "https://t.me/teamishere" ,

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

                        "My Friend🧐🧐",

                        data="he_sucks",

                    )

                ],

                [custom.Button.inline("Requesting⚜️⚜️", data="fck_ask")],

                [

                    custom.Button.inline(

                        "Lemme In :)", 

                        data="lol_u_think_so",

                        

                    )

                        

                ],



            ],

            )

        await ultra.answer([result] if result else None)

    else:

        return

    





@tgbot.on(

    events.callbackquery.CallbackQuery(  # pylint:disable=E0602

        data=re.compile(b"helpmenext\((.+?)\)")

    )

)

async def ultra_pugins_query_hndlr(ultra):

    if ultra.query.user_id == bot.uid or ultra.query.user_id == ID:  # pylint:disable=E0602

        ultra_page = int(ultra.data_match.group(1).decode("UTF-8"))

        buttons = ultras_menu_for_help(

            ultra_page + 1, CMD_LIST, "helpmepro"  # pylint:disable=E0602

        )

        # https://t.me/TelethonChat/115200

        await ultra.edit(buttons=buttons)

    else:

        ultra_is_best = "Oh C'mon You Think You Can Touch This? 😂😂 !"

        await ultra.answer(ultra_is_best, cache_time=0, alert=True)





@tgbot.on(

        events.callbackquery.CallbackQuery(  # pylint:disable=E0602

            data=re.compile(b"_ultra_plugins_(.*)")

   )

) # Thanks To Friday Userbot

async def ultra_pugins_query_hndlr(ultra):

    if not ultra.query.user_id == bot.uid:

        how = "Not For  Bitch.😂😂( 😈😈😈😈😈😈)"

        await ultra.answer(how, cache_time=0, alert=True)

        return

    light_pulu_name = ultra.data_match.group(1).decode("UTF-8")

   

    try:

        if light_pulu_name in CMD_HELP:

           

           ultra_help_strin  = f"**🔱🔱 NAME 🔱🔱 :** `{light_pulu_name}` \n\n{CMD_HELP[light_pulu_name]}"

           ultra_is_best = ultra_help_strin 

           ultra_is_best += "\n\n**In Case Any Problem @teamishere** ".format(light_pulu_name)

        

        else:

            ultra_help_strin = "Commands found in {}:\n".format(light_pulu_name)

            for i in CMD_HELP:

                ultra_help_strin += "🔥🔥 " + i + "\n"

                for iter_list in CMD_HELP[i]:

                    ultra_help_strin += "    `" + str(iter_list) + "`"

                    ultra_help_strin += "\n"

                    ultra_help_strin += "\n"

    except BaseException:

         pass

   

    if light_pulu_name in CMD_LIST:

                ultra_help_strin = "Commands found in {}:\n".format(light_pulu_name)

                for i in CMD_LIST[light_pulu_name]:

                    ultra_help_strin  = f"**🔱🔱 NAME 🔱🔱 :** `{light_pulu_name}` \n\n `{CMD_LIST[light_pulu_name]}\n`**Details**- Not Yetðð\n\n**Ask at @teamishere"

                    ultra_help_strin += "\n    " + i

                    ultra_help_strin += "\n"

                

    else:

           ultra_help_strin  = f"**🔱🔱 NAME 🔱🔱 :** `{light_pulu_name}` \n\n`{CMD_LIST[light_pulu_name]}`\n**Details** - Not Yetðð\n\n**Ask at @teamishere"

           ultra_is_best = ultra_help_strin 

           ultra_is_best += "\n\n**In Case Any Problem @teamishere** ".format(light_pulu_name)

    ultra_help_strin = f"**🔱🔱 NAME 🔱🔱 :** `{light_pulu_name}` \n\n`{CMD_LIST[light_pulu_name]}`\n**Details** - Not Set for this Plugin 😑\n\n**Ask at @teamishere"

    ultra_is_best = ultra_help_strin 

    ultra_is_best += "\n\n**In Case Any Problem @teamishere** ".format(light_pulu_name)    

    if len(ultra_is_best) >= 4096:

          LEGENDX = "` Wait. (🔥🔥🔥🔥) `"

          await ultra.answer(LEGENDX, cache_time=0, alert=True)

          out_file = ultra_is_best

          lig_url = "https://del.dog/documents"

          r = requests.post(lig_url, data=out_file.encode("UTF-8")).json()

          lig_url = f"https://del.dog/{r['key']}"

          await ultra.edit(

               f"Pasted {light_pulu_name} to {lig_url}",

               link_preview=False,

               buttons=[

                [custom.Button.inline("😉", data="LegendX")],

                [custom.Button.inline("BACK", data="lghtback")]],

         )

    else:

           await ultra.edit(

            message=ultra_is_best,

            buttons=[

                [custom.Button.inline("🙂", data="LegendX")],

                [custom.Button.inline("BACK", data="lghtback")],

            ],

        )





@tgbot.on(

    events.callbackquery.CallbackQuery(  # pylint:disable=E0602

        data=re.compile(rb"helpmeprev\((.+?)\)")

    )

)

async def ultra_pugins_query_hndlr(ultra):

    if ultra.query.user_id == bot.uid or ultra.query.user_id == ID:  # pylint:disable=E0602

        ultra_page = int(ultra.data_match.group(1).decode("UTF-8"))

        buttons = ultras_menu_for_help(

            ultra_page - 1, CMD_LIST, "helpmepro"  # pylint:disable=E0602

        )

        # https://t.me/TelethonChat/115200

        await ultra.edit(buttons=buttons)

    else:

        ultra_is_best = "Oh C'mon You Think You Can Touch This? 😂😂😂 !"

        await ultra.answer(ultra_is_best, cache_time=0, alert=True)



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"what?")))

async def what(ultra):

    if ultra.query.user_id == bot.uid or ultra.query.user_id == ID:

        fck_bit = f"{ULTRA_USER}  Use The Buttons Bellow "

        await ultra.answer(fck_bit, alert=True)

    else:

        txt = f"Ohh  You Think That This Is For You?\n Ok I Will Complain To {ULTRA_USER}⚜️⚜️"

        await ultra.answer(txt, alert=True)





@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ultra_is_here_cant_spam")))

async def ultra_is_better(ultra):

    if ultra.query.user_id == bot.uid:

        fck_bit = f"Oh! Master {ULTRA_USER} Im Try To Get Rid Of This Nigga Pls Dont Touch"

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



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stta")))

async def hmm(ultra):

    if ultra.query.user_id == bot.uid:

        text = "-- All Good â ???? \ heroku  - Connected  \ all good- Looks Good: \nTottal Plugs: {} ". Format (len (CMD_LIST))

        await ultra.answer(text, alert=True)

    else:

        txt = f"Stats For {ULTRA_USER} Not For You :)"

        await ultra.answer(txt, alert=True)







@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LegendX")))

async def hmm(ultra):

    if ultra.query.user_id == bot.uid:

        text = ".xnxx\n.picx\n.les\n please use in private 😂"

        await ultra.answer(text, alert=True)

    else:

        txt = f"For {ULTRA_USER} Not For You :)"

        await ultra.answer(txt, alert=True)        





"""

Thanks To Friday Userbot and @Midhun_xD For This idea



"""

import requests









@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lghtback")))

async def ho(event):

    if event.query.user_id != bot.uid or event.query.user_id == ID: 

        how = "Not For You Idiot ( fuck )."

        await event.answer(how, cache_time=0, alert=True)

        return

    await event.answer ("(DONE)", cache_time = 0, alert = False)

    # This Is Copy of Above Code. (C) @SpEcHiDe

    buttons = ultras_menu_for_help(0, CMD_LIST, "helpmepro")

    ho = f"""LEGENDBOT Is Here With Stunning Help !\n

In Case Any Problem @teamishere \nTottal Plugs( 🧐): {len(CMD_LIST)}"""

    await event.edit(message=ho, buttons=buttons)







        





    

def ultras_menu_for_help(b_lac_LegendX, ultra_plugs, ultra_lol):

    ultra_no_rows = 10

    ultra_no_coulmns = 3

    ultra_plugins = []

    for p in ultra_plugs:

        if not p.startswith("_"):

            ultra_plugins.append(p)

    ultra_plugins = sorted(ultra_plugins)

    plugins = [

        custom.Button.inline(

            "{} {} {}".format("🙂", x, "🙂"), data="_ultra_plugins_{}".format(x)

        )

        for x in ultra_plugins

    ]

    pairs = list(zip(plugins[::ultra_no_coulmns], plugins[1::ultra_no_coulmns]))

    if len(plugins) % ultra_no_coulmns == 1:

        pairs.append((plugins[-1],))

    max_fix = ceil(len(pairs) / ultra_no_rows)

    ultra_plugins_pages = b_lac_LegendX % max_fix

    if len(pairs) > ultra_no_rows:

        pairs = pairs[

            ultra_plugins_pages * ultra_no_rows : ultra_no_rows * (ultra_plugins_pages + 1)

        ] + [

            (

                custom.Button.inline(

                    "BACK 🔥", data="{}_prev({})".format(ultra_lol, ultra_plugins_pages)

                ),

               # Thanks To DC for this idea

               custom.Button.inline("CLOSE🤨", data="close"

               ),

               custom.Button.inline(

                    "NEXT⚡ ", data="{}_next({})".format(ultra_lol, ultra_plugins_pages)

                ),

                

            )

        ]

    return pairs

