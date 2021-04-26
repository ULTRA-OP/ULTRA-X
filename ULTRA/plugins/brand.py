import asyncio
import os
from ULTRAX import BOT, PHOTO, VERSION, MSG
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom
from ULTRA.utils import admin_cmd
from ULTRA import ALIVE_NAME
from ULTRA import bot as ultra
from telethon import Button, custom
from telethon.tl.types import ChannelParticipantsAdmins
global ok
ok = ultra.uid
from ULTRA.utils import admin_cmd
from PIL import Image
import requests
from io import BytesIO
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"
ALIVE_PHOTTO = PHOTO

pro_text=(f"**{BOT} ιѕ ση ƒιяє**\n\n{MSG}\n\n🔥 αвσυт му ѕуѕтєм 🔥\n\n➥ **Tᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** : 1.19.5\n\n➥ **Mʏ ᴍᴀsᴛᴇʀ** : [{DEFAULTUSER}](tg://user?id={ok})\n")
TG_BOT_USER_NAME_BF_HER = os.environ.get("ALIVE_PHOTTO", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await bot.get_me()
        x = await xbot.get_me()
        if query.startswith("brand") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{me.username}"),
                    Button.url("Assɪsᴛᴀɴᴛ", f"https://t.me/{x.username}")
                ]
            ]
            buttons += [[custom.Button.inline("Hᴇʟᴘ", data="open"), custom.Button.inline("Rᴇsᴛᴀʀᴛ", data='restart')]]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO and ALIVE_PHOTTO.endswith(("gif", "mp4"))::
                result = builder.video(
                    ALIVE_PHOTTO,
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="υℓтяα χ",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)

