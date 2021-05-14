# COPYRIGHT (C) 2021-2022 BY LEGENDX22 (TEAMULTRA)
# KANG WITH KEEP CREDITS
# MADE BY LEGENDX22
ok = "https://telegra.ph/file/a361854079cc8e19586e8.png"
ok1 = 'https://telegra.ph/file/dbbb03bdad2f78c1e0895.png'
ok2 = "https://telegra.ph/file/1cc3e2a4cea7a4c553606.png"
ok3 = "https://telegra.ph/file/1007a1a1240a6b60a8e78.png"
ok4 = "https://telegra.ph/file/4b1b04d81379cf6e095fa.png"
ok5 = "https://telegra.ph/file/3caac90be53f7aee5130f.png"
ok6 = "https://telegra.ph/file/c4f765b9fd047bcc61aef.png"
ok7 = "https://telegra.ph/file/00e9a2c74697840a10725.png"
ok8 = "https://telegra.ph/file/fe2308bb79153f7e69ce5.png"
ok9 = "https://telegra.ph/file/e626a077513f3156fa34d.png"
ok10 = "https://telegra.ph/file/ff6e1a2edcfeb46db6087.png"
ok11 = "https://telegra.ph/file/70588911027a76b9ee14f.png"
ok12 = "https://telegra.ph/file/d88a2adff2166148db600.png"
ok13 = "https://telegra.ph/file/9c3c6923ab942ee376a75.png"
ok14 = "https://telegra.ph/file/94251355cd9dcdd9d5444.png"
ok15 = "https://telegra.ph/file/45cbae820b133ed213e59.png"
ok16 = "https://telegra.ph/file/0115bcdeba49e1f3874ce.png"
ok17 = "https://telegra.ph/file/75a8dde657d2718db8463.png"
cap = "Hahaha"
cap2 = "chote insaan 😂😂"
cap3 = "aaja gale mill"
cap4 = "golli mar duga"
cap5 = "Coffee pe le"
cap6 = "hands up"
cap7 = "Ruk Bhai"
cap8 = "pc chalale"
cap9 = "role bacha role"
cap10 = "padne de"
cap11 = "O bhai"
cap12 = "Namaste"
cap13 = "are bc"
cap14 = "Hat marke dikha"
cap15 = "Khel le"
cap16 = "Naam bata"
cap17 = "Saar dard"
cap18 = "Nikal lodu"
import asyncio
from ..utils import admin_cmd, sudo_cmd
@borg.on(admin_cmd(pattern="lel"))# by LEGENDX22 🔥
@borg.on(sudo_cmd(pattern="lel", allow_sudo=True))
async def _(event):
  await event.delete()
  if not event.is_reply:
    file = await bot.send_file(event.chat, ok, caption=cap)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap2, file=ok1)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap3, file=ok2)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap4, file=ok3)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap5, file=ok4)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap6, file=ok5)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap7, file=ok6)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap8, file=ok7)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap9, file=ok8)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap10, file=ok9)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap11, file=ok10)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap12, file=ok11)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap13, file=ok12)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap14, file=ok13)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap15, file=ok14)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap16, file=ok15)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap17, file=ok16)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap18, file=ok17)
  elif event.is_reply:
    Pro = await event.get_reply_message()
    file = await bot.send_file(event.chat, ok, caption=cap, reply_to=Pro)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap2, file=ok1)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap3, file=ok2)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap4, file=ok3)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap5, file=ok4)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap6, file=ok5)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap7, file=ok6)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap8, file=ok7)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap9, file=ok8)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap10, file=ok9)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap11, file=ok10)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap12, file=ok11)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap13, file=ok12)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap14, file=ok13)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap15, file=ok14)
