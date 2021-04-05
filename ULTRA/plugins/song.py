#    Copyright (C) 2020 LEGENDX22

######### made by LEGENDX22 🔥🔥🔥###################

#    This program is free software: you can redistribute it and/or modify

#    it under the terms of the GNU Affero General Public License as published by

#    the Free Software Foundation, either version 3 of the License, or

#    made by LEGEND X by shivam help 

#    This program is distributed in the hope that it will be useful,

#    but WITHOUT ANY WARRANTY; without even the implied warranty of

#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

#    GNU Affero General Public License for more details.

#

#    You should have received a copy of the GNU Affero General Public License

#    along with this program.  If not, see <https://www.gnu.org/licenses/>.






"""
Thanks To :-

TEAMLEGEND

TEAMULTRA

KEINSHIN

@LEGENDX22

MadBoy482
"""





""" Only ULTRA X and LEGEND-BOT Can Use This Inline WithOut Credits/Copyright Info..
Rest all need to give The Credits, else DMCA.

Thanks
"""

# made by legendx22 
# modify by madboy482
import os
import re
# made by legendx22 
# modify by madboy482
import json
# made by legendx22 
# modify by madboy482
from math import ceil
# made by legendx22 
# modify by madboy482
from ULTRA.uniborgConfig import Config
# made by legendx22 
# modify by madboy482
# made by legendx22 
# modify by madboy482
# made by legendx22 
# modify by madboy482
from telethon import Button, custom, events, functions
# made by legendx22 
# modify by madboy482
# made by legendx22 
# modify by madboy482
# made by legendx22 
# modify by madboy482
from ULTRA import ALIVE_NAME, CMD_HELP, CMD_LIST, bot
# made by legendx22 
# modify by madboy482
# made by legendx22 
# modify by madboy482
# made by legendx22 
# modify by madboy482
from var import Var
# made by legendx22 
# modify by madboy482
# made by legendx22 
# modify by madboy482
# made by legendx22 
# modify by madboy482


LIGHT_LOGS = Config.PM_LOGGR_BOT_API_ID 

ultra_bot = Var.TG_BOT_USER_NAME_BF_HER

import asyncio



from datetime import datetime

from pathlib import Path


# made by legendx22 
# modify by madboy482


from ULTRA.utils import load_module, remove_plugin,admin_cmd as ultra_cmd



DELETE_TIMEOUT = 5


# made by legendx22 
# modify by madboy482


thumb_image_path = "./resources/541200.png"



ULTRA_USER = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"

ULTRAXBOT = Var.TG_BOT_TOKEN_BF_HER

# made by legendx22 
# modify by madboy482

# made by legendx22 
# modify by madboy482


# made by legendx22 
# modify by madboy482
 

from LEGENDX import ID
from telethon import events

BOT_MSG = os.environ.get("BOT_MSG", None)

if BOT_MSG is None:

    BOT_LIT = f"Hᴇʟʟᴏ sɪʀ ᴍʏsᴇʟғ UʟᴛʀᴀX, ғᴏʀ {ULTRA_USER}'s Pʀᴏᴛᴇᴄᴛɪᴏɴ "

else:

    BOT_LIT = BOT_MSG   


# made by legendx22 
# modify by madboy482


ULTRA_WARN = os.environ.get("ULTRA_WARN", None)

if ULTRA_WARN is None:
# made by legendx22 
# modify by madboy482

# made by legendx22 
# modify by madboy482
    WARNING = (

    f"**{BOT_LIT}"

   f"__Hᴇʏ ᴛʜᴇʀᴇ!! I'ᴍ__ **υℓтяα χ** __ᴀɴᴅ I'ᴍ ʜᴇʀᴇ ᴛᴏ Pʀᴏᴛᴇᴄᴛ {ULTRA_USER}..\nDᴏɴ'ᴛ ᴜɴᴅᴇʀ Esᴛɪᴍᴀᴛᴇ ᴍᴇ 😈😈__\n\n**\n\n"
# made by legendx22 
# modify by madboy482
    f"__Mʏ Mᴀsᴛᴇʀ **{ULTRA_USER}**  ɪs ʙᴜsʏ ʀɪɢʜᴛ ɴᴏᴡ !!__ \n"
# made by legendx22 
# modify by madboy482
    f"Mʏ Mᴀsᴛᴇʀ ʜᴀs ᴀssɪɢɴᴇᴅ ᴍᴇ ᴛʜᴇ ᴅᴜᴛʏ ᴛᴏ ᴋᴇᴇᴘ ᴀ ᴄʜᴇᴄᴋ ᴏɴ ʜɪs PM, Aɴᴅ ɪ'ʟʟ ᴅᴏ ɪᴛ ғᴀɪᴛʜғᴜʟʟʏ..Sᴏ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅɪsᴛᴜʀʙ ʜɪᴍ..\n"
# made by legendx22 
# modify by madboy482
    f"**Iғ ᴜ Sᴘᴀᴍ, ᴏʀ ᴛʀɪᴇᴅ ᴀɴʏᴛʜɪɴɢ ғᴜɴɴʏ, I'ᴠᴇ ғᴜʟʟ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ Bʟᴏᴄᴋ + Rᴇᴘᴏʀᴛ ʏᴏᴜ ᴀs Sᴘᴀᴍ ɪɴ Tᴇʟᴇɢʀᴀᴍ's sᴇʀᴠᴇʀ...**\n\n"
# made by legendx22 
# modify by madboy482
    f"**Bᴇᴛᴛᴇʀ ʙᴇ ᴄᴀʀᴇғᴜʟ..**\n\n"
# made by legendx22 
# modify by madboy482
    f"**Cʜᴏᴏsᴇ ᴀɴʏ Rᴇᴀsᴏɴ & GTFO**\n"

)

else:
# made by legendx22 
# modify by madboy482

# made by legendx22 
# modify by madboy482
    WARNING = ULTRA_WARN



ULTRA_BOT_PIC = os.environ.get("PMPERMIT_PIC", None)

if ULTRA_BOT_PIC is None:

    ULTRA_WARNING = "https://telegra.ph/file/a44f1363bddbba84a2b98.jpg"

else:

    ULTRA_WARNING = ULTRA_BOT_PIC




# made by legendx22 
# modify by madboy482

# made by legendx22 
# modify by madboy482

# made by legendx22 
# modify by madboy482

# made by legendx22 
# modify by madboy482



from ULTRA import CMD_HELP

@tgbot.on(events.InlineQuery)

async def inline_handler(ultra):

    builder = ultra.builder

    result = None

    query = ultra.text

    if ultra.query.user_id == bot.uid and query.startswith("**help") or query.startswith("help"):
        print (False)
    elif ultra.query.user_id == bot.uid and query == "**Cool":
# made by legendx22 
# modify by madboy482
        result = builder.article(

            title="Cool",

            text=f"**Wʜᴀᴛ ɪғ ʏᴏᴜ ғᴀᴄᴇ sᴏᴍᴇ ᴘʀᴏʙʟᴇᴍ\n{ULTRA_USER}** \nCʜᴏᴏsᴇ ʏᴏᴜʀ ᴘʀᴏʙʟᴇᴍ ғᴏʀ ʜᴇʟᴘ",
# made by legendx22 
# modify by madboy482
            buttons=[

                [custom.Button.inline("Hᴇʟᴘ ⚙️", data="what?")],

                [Button.url("Cᴏᴍᴍᴀɴᴅs ɴᴏᴛ ᴡᴏʀᴋɪɴɢ 🤔", "https://t.me/teamishere")],

                [Button.url("Hᴇʟᴘ Aʀᴛɪᴄʟᴇ 🤔", "https://app.gitbook.com/@poxsisofficial/s/help/")],

                [

                    Button.url(

                

                    "Wᴀɴᴛ ᴛᴏ ʟᴇᴀʀɴ Cᴍᴅs ☺️☺️",

                    "https://t.me/UltraXchaT" ,

                    )

                ], 
# made by legendx22 
# modify by madboy482
            ],

        )

        await ultra.answer([result])

    elif ultra.query.user_id == bot.uid and query.startswith("**Hᴇʟʟᴏ sɪʀ**"):

        result = builder.photo(

            file=ULTRA_WARNING,

            text=WARNING,

            buttons=[

                [custom.Button.inline("Wᴀɴɴᴀ Sᴘᴀᴍ Sᴏᴍᴇᴛʜɪɴɢ?🥺🥺", data="ultra_is_here_cant_spam")],

                [

                    custom.Button.inline(

                        "Mʏ Fʀɪᴇɴᴅ🧐🧐",

                        data="he_sucks",

                    )

                ],

                [custom.Button.inline("Rᴇǫᴜᴇsᴛɪɴɢ⚜️⚜️", data="fck_ask")],

                [

                    custom.Button.inline(

                        "Lᴇᴍᴍᴇ Iɴ ;)", 

                        data="lol_u_think_so",
# made by legendx22 
# modify by madboy482
                        

                    )

# made by legendx22 
# modify by madboy482                       

                ],

# made by legendx22 
# modify by madboy482
             
# made by legendx22 
# modify by madboy482

            ],

            )

        await ultra.answer([result] if result else None)

    else:

        return

    



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"what?")))

async def what(ultra):

    if ultra.query.user_id == bot.uid or ultra.query.user_id == ID:

        fck_bit = f"{ULTRA_USER} Usᴇ ᴛʜᴇ Bᴜᴛᴛᴏɴs Bᴇʟᴏᴡ"

        await ultra.answer(fck_bit, alert=True)

    else:

        txt = f"Oʜʜ!! Yᴏᴜ ᴛʜɪɴᴋ ᴛʜᴀᴛ ᴛʜɪs ɪs ғᴏʀ ʏᴏᴜ??\nOᴋ I'ʟʟ ᴄᴏᴍᴘʟᴀɪɴ ᴛᴏ {ULTRA_USER} ⚜️⚜️"

        await ultra.answer(txt, alert=True)

# made by legendx22 
# modify by madboy482

# made by legendx22 
# modify by madboy482

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ultra_is_here_cant_spam")))

async def ultra_is_better(ultra):

    if ultra.query.user_id == bot.uid:

        fck_bit = f"Oʜ!! Mᴀsᴛᴇʀ, {ULTRA_USER}...I'ᴍ Tʀʏɪɴɢ Tᴏ Gᴇᴛ Rɪᴅ Oғ Tʜɪs Nɪɢɢᴀ...Pʟs Dᴏɴᴛ Tᴏᴜᴄʜ!!"

        await ultra.answer(fck_bit, cache_time=0, alert=True)

        return

    await ultra.get_chat()
# made by legendx22 
# modify by madboy482

# made by legendx22 
# modify by madboy482

# made by legendx22 
# modify by madboy482
    ultra_id = ultra.query.user_id

    text1 = f'''
██╗░░░░░░█████╗░██╗░░░░░
██║░░░░░██╔══██╗██║░░░░░
██║░░░░░██║░░██║██║░░░░░
██║░░░░░██║░░██║██║░░░░░
███████╗╚█████╔╝███████╗
╚══════╝░╚════╝░╚══════╝\n\n**Yᴏᴜ Tʜɪɴᴋ Sᴏ Yᴏᴜ Cᴀɴ**😂\n\n**[Nibba](tg://user?id={ultra_id})\nBʏᴇ Gᴏɪɴ Tᴏ Bʟᴏᴄᴋ Yᴏᴜ Gᴀʏ**😈😈'''

    await ultra.edit("Oғғ Cᴏᴜʀsᴇ Gᴏ Tᴏ Hᴇʟʟ Dᴜᴅᴇ")

    await bot.send_message(ultra.query.user_id, text1)

    await bot(functions.contacts.BlockRequest(ultra.query.user_id))

    await ultra.edit("😈")

    await bot.send_message(

        LIGHT_LOGS,

        f"Hᴇʏ Mᴀsᴛᴇʀ Sᴏʀʀʏ Tᴏ Dɪsᴛᴜʀʙ Yᴏᴜ, [Noob](tg://user?id={ultra_id}) Tʀʏɪɴ Tᴏ Sᴘᴀᴍ 🥺\n\n**Sᴏ Bʟᴏᴄᴋᴇᴅ**.",
# made by legendx22 
# modify by madboy482
    )
# made by legendx22 
# modify by madboy482


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lol_u_think_so")))

async def ultra_is_better(ultra):

    if ultra.query.user_id == bot.uid:

        fck_bit = f"Oʜ C'ᴍᴏɴ Mᴀsᴛᴇʀ!!, {ULTRA_USER}...I'ᴍ Tʀʏɪɴɢ Tᴏ Gᴇᴛ Rɪᴅ Oғ Tʜɪs Nɪɢɢᴀ...Pʟs Dᴏɴᴛ Tᴏᴜᴄʜ!!"

        await ultra.answer(fck_bit, cache_time=0, alert=True)

        return

    await ultra.get_chat()

    ultra_id = ultra.query.user_id

    text1 = f'''
██╗░░░░░░█████╗░██╗░░░░░
██║░░░░░██╔══██╗██║░░░░░
██║░░░░░██║░░██║██║░░░░░
██║░░░░░██║░░██║██║░░░░░
███████╗╚█████╔╝███████╗
╚══════╝░╚════╝░╚══════╝\n\n**Yᴏᴜ Tʜɪɴᴋ Sᴏ Yᴏᴜ Cᴀɴ**😂\n\nGo and wait 🥴🥴...'''

    await ultra.edit("Oғғ Cᴏᴜʀsᴇ Gᴏ Tᴏ Hᴇʟʟ Dᴜᴅᴇð😑")

    await bot.send_message(ultra.query.user_id, text1)

    await bot(functions.contacts.BlockRequest(ultra.query.user_id))

    await bot.send_message(

        LIGHT_LOGS,

        f"Hᴇʏ Mᴀsᴛᴇʀ Sᴏʀʀʏ Tᴏ Dɪsᴛᴜʀʙ Yᴏᴜ, [Noob](tg://user?id={ultra_id}) Tʀʏɪɴ Tᴏ Eɴᴛᴇʀ Wɪᴛʜ Oᴜᴛ ᴀᴘᴘʀᴏᴠᴀʟð \n.",

    )



# made by legendx22 
# modify by madboy482

# made by legendx22 
# modify by madboy482

# made by legendx22 
# modify by madboy482



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"he_sucks")))

async def ultra_is_better(ultra):

    if ultra.query.user_id == bot.uid:

        fck_bit = f"Oʜ C'ᴍᴏɴ Mᴀsᴛᴇʀ!!, {ULTRA_USER}...I'ᴍ Tʀʏɪɴɢ Tᴏ Gᴇᴛ Rɪᴅ Oғ Tʜɪs Nɪɢɢᴀ...Pʟs Dᴏɴᴛ Tᴏᴜᴄʜ!!"

        await ultra.answer(fck_bit, cache_time=0, alert=True)

        return

    await ultra.get_chat()

    ultra_id = ultra.query.user_id

    await ultra.edit('''Oʜ Yᴏᴜ Wᴀɴɴᴀ Tᴀʟᴋ Wɪᴛʜ Mʏ Mᴀsᴛᴇʀ\n\nPʟs Wᴀɪᴛ Dᴇᴀʀ\n\n
░██╗░░░░░░░██╗░█████╗░██╗████████╗
░██║░░██╗░░██║██╔══██╗██║╚══██╔══╝
░╚██╗████╗██╔╝███████║██║░░░██║░░░
░░████╔═████║░██╔══██║██║░░░██║░░░
░░╚██╔╝░╚██╔╝░██║░░██║██║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░''')

    await asyncio.sleep(2)

    await ultra.edit(

        "Wʜɪᴄʜ Tʏᴘᴇ Oғ Fʀɪᴇɴᴅ, Hᴜʜ?", buttons= [

        [Button.inline("Sᴄʜᴏᴏʟ Bᴜᴅᴅʏ", data="school")],

        [Button.inline("TG Cᴀᴜsᴀʟ Fʀɪᴇɴᴅ", data="tg_okay")],

        ], 

    )

    light_text = '''
█░█░█ ▄▀█ █▀█ █▄░█ █ █▄░█ █▀▀
▀▄▀▄▀ █▀█ █▀▄ █░▀█ █ █░▀█ █▄█\n\n😈😈Dᴏɴ'ᴛ Tʀʏ Aɴʏᴛʜɪɴɢ Sᴛᴜᴘɪᴅ, Wᴀɪᴛ Pᴀᴛɪᴇɴᴛʟʏ!!!😈😈'''

    await bot.send_message(ultra.query.user_id, light_text)

    

    

    

    

    

    

    

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"tg_okay")))

async def yeahbaba(ultra):

        if ultra.query.user_id == bot.uid:

            fck_bit = f"Oʜ! C'ᴍᴏɴ Mᴀsᴛᴇʀ {ULTRA_USER} "

            await ultra.answer(fck_bit, cache_time=0, alert=True)

            return

        light_text = "**Hᴜᴍᴍ!! I C, Yᴏᴜ'ʀᴇ ᴀ TG Fʀɪᴇɴᴅ** Oᴋᴀʏ Wᴀɪᴛ"

        ultra_id = ultra.query.user_id

        await asyncio.sleep(2)

        await ultra.edit(f"`Iɴғᴏʀᴍɪɴɢ Tᴏ Mᴀsᴛᴇʀ {ULTRA_USER}`")

        await asyncio.sleep(2)

        await ultra.edit("`Dᴏɴᴇ Iɴғᴏʀᴍᴇᴅ`")

        await bot.send_message(ultra.query.user_id, light_text)

        await bot.send_message(

        LIGHT_LOGS,

        message=f"Hᴇʟʟᴏ, Mᴀsᴛᴇʀ. Yᴏᴜʀ Cᴀsᴜᴀʟ Tᴇʟᴇɢʀᴀᴍ Fʀɪᴇɴᴅ ɪs Hᴇʀᴇ Tᴏ Cʜᴀᴛ ᴡɪᴛʜ ᴜ.\nPʟs Sᴇᴇ Tʜᴇ Mᴇssᴀɢᴇ, [Tg Friend](tg://user?id={ultra_id}) Is Wᴀɪᴛɪɴɢ.",

    

    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"School")))

async def yeahbaba(ultra):

        if ultra.query.user_id == bot.uid:

            fck_bit = f"Oʜ! C'ᴍᴏɴ Mᴀsᴛᴇʀ {ULTRA_USER} "

            await ultra.answer(fck_bit, cache_time=0, alert=True)

            return

        light_text = "**Hᴜᴍᴍ!! I C, Yᴏᴜ'ʀᴇ ᴀ Fʀɪᴇɴᴅ** Oᴋᴀʏ Wᴀɪᴛ"

        ultra_id = ultra.query.user_id

        await asyncio.sleep(2)

        await ultra.edit(f"`Iɴғᴏʀᴍɪɴɢ Tᴏ Mᴀsᴛᴇʀ {ULTRA_USER}`")

        await asyncio.sleep(2)

        await ultra.edit("`Dᴏɴᴇ Iɴғᴏʀᴍᴇᴅ`")

        await bot.send_message(ultra.query.user_id, light_text)

        await bot.send_message(

        LIGHT_LOGS,

        message=f"Hᴇʟʟᴏ, Mᴀsᴛᴇʀ. Oɴᴇ ᴏғ ʏᴏᴜʀ Fʀɪᴇɴᴅs' ɪs Hᴇʀᴇ Tᴏ Cʜᴀᴛ ᴡɪᴛʜ ᴜ.\nPʟs Sᴇᴇ Tʜᴇ Mᴇssᴀɢᴇ, [Friend](tg://user?id={ultra_id}) Is Wᴀɪᴛɪɴɢ.",

        )





@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fck_ask")))

async def ultra_is_better(ultra):

    if ultra.query.user_id == bot.uid:

        fck_bit = f"Oʜ C'ᴍᴏɴ Mᴀsᴛᴇʀ!!, {ULTRA_USER}...I'ᴍ Tʀʏɪɴɢ Tᴏ Gᴇᴛ Rɪᴅ Oғ Tʜɪs Nɪɢɢᴀ...Pʟs Dᴏɴᴛ Tᴏᴜᴄʜ!!"

        await ultra.answer(fck_bit, cache_time=0, alert=True)

        return
# made by legendx22 
# modify by madboy482

    await ultra.get_chat()

    ultra_id = ultra.query.user_id

    await ultra.edit("Oᴋᴀʏ ʟᴇᴛ Mᴇ Tʜɪɴᴋ🤔🤔«")

    await asyncio.sleep(2)

    await ultra.edit("Oᴋᴀʏ Gɪᴠɪɴɢ Yᴏᴜ A Cʜᴀɴᴄᴇ🧐¨")

    await asyncio.sleep(2)

    await ultra.edit(

        "Wɪʟʟ ʏᴏᴜ Sᴘᴀᴍ?", buttons= [

        [Button.inline("Yᴇs", data="lemme_ban")],

        [Button.inline("Nᴏ", data="hmm")],

        ],

    )



    

    reqws = '''
█░█░█ ▄▀█ █▀█ █▄░█ █ █▄░█ █▀▀
▀▄▀▄▀ █▀█ █▀▄ █░▀█ █ █░▀█ █▄█\n\n😈😈Dᴏɴ'ᴛ Tʀʏ Aɴʏᴛʜɪɴɢ Sᴛᴜᴘɪᴅ, Wᴀɪᴛ Pᴀᴛɪᴇɴᴛʟʏ!!!😈😈'''





    await bot.send_message(ultra.query.user_id, reqws)

    await bot.send_message(

        LIGHT_LOGS,

        message=f"Hᴇʟʟᴏ, Mᴀsᴛᴇʀ [Nibba](tg://user?id={ultra_id}), Wᴀɴᴛs Tᴏ Rᴇᴏ̨ᴜᴇsᴛ Sᴏᴍᴇᴛʜɪɴɢ.",

        buttons=[Button.url("Cᴏɴᴛᴀᴄᴛ Hɪᴍ", f"tg://user?id={ultra_id}")],

    )



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hmm")))

async def yes_ucan(ultra):

    if ultra.query.user_id == bot.uid:

           lmaoo = '''Yᴏᴜ Aʀᴇ'ɴᴛ Rᴇᴏ̨ᴜᴇsᴛɪɴɢ..\n\n
██╗░░░░░░█████╗░██╗░░░░░
██║░░░░░██╔══██╗██║░░░░░
██║░░░░░██║░░██║██║░░░░░
██║░░░░░██║░░██║██║░░░░░
███████╗╚█████╔╝███████╗
╚══════╝░╚════╝░╚══════╝'''

           await ultra.answer(lmaoo, cache_time=0, alert=True)

           return          

    await ultra.get_chat()

    await asyncio.sleep(2)

    await ultra.edit("Oᴋᴀʏ Yᴏᴜ Cᴀɴ Wᴀɪᴛ..")

    hmmmmm = "Okay Kindly wait, I'll inform you..."

    await bot.send_message(

              ultra.query.user_id, hmmmmm)

          

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))

async def yes_ucan(ultra):

    if ultra.query.user_id == bot.uid:

           lmaoo = '''Yᴏᴜ Aʀᴇ'ɴᴛ Rᴇᴏ̨ᴜᴇsᴛɪɴɢ..\n\n
██╗░░░░░░█████╗░██╗░░░░░
██║░░░░░██╔══██╗██║░░░░░
██║░░░░░██║░░██║██║░░░░░
██║░░░░░██║░░██║██║░░░░░
███████╗╚█████╔╝███████╗
╚══════╝░╚════╝░╚══════╝'''

           await ultra.answer(lmaoo, cache_time=0, alert=True)

           return    

    await ultra.get_chat()
# made by legendx22 
# modify by madboy482
    await asyncio.sleep(2)

    await ultra.edit("Gᴇᴛ Lᴏsᴛ Rᴇᴛᴀʀᴅ")
    
    await asyncio.sleep(2)
# made by legendx22 
# modify by madboy482
    await ultra.edit('''
███╗░░██╗██╗██████╗░██████╗░░█████╗░░██████╗
████╗░██║██║██╔══██╗██╔══██╗██╔══██╗██╔════╝
██╔██╗██║██║██████╦╝██████╦╝███████║╚█████╗░
██║╚████║██║██╔══██╗██╔══██╗██╔══██║░╚═══██╗
██║░╚███║██║██████╦╝██████╦╝██║░░██║██████╔╝
╚═╝░░╚══╝╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝╚═════╝░''')

    ban = "Gᴇᴛ Lᴏsᴛ, Gᴏɪɴ Tᴏ Bʟᴏᴄᴋ Yᴏᴜ" 

    await bot.send_message(

         ultra.query.user_id, ban)

    await bot(functions.contacts.BlockRequest(ultra.query.user_id))




# made by legendx22 
# modify by madboy482

# made by legendx22 
# modify by madboy482



"""

Thanks To LEGEND BOT, @LEGENDX22 and @NubBoy_007

"""
