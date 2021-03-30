# COPYRIGHT (C) 2021-2022 BY LEGENDX22
# modify by madboy482 and alain_champion

from ULTRA import bot
from LEGENDX import xbot, ID
import heroku3
from telethon import events
from ULTRA import StartTime
import time
import datetime

from telethon import events, Button, custom
import re, os
from LEGENDX import PHOTO, xbot, BOT, VERSION
from ULTRA import bot
@xbot.on(events.NewMessage(pattern=("/alive")))
async def awake(event):
  LEGENDX = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
  LEGENDX += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
  LEGENDX += f"**{BOT} Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
  LEGENDX += f"**Usᴇʀ** : @{bot.me.username}\n\n"
  LEGENDX += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
  LEGENDX += "**Tᴇʟᴇᴛʜᴏɴ** : `1.20`\n\n"
  LEGENDX += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
  BUTTON = [[Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/ULTRA-OP/ULTRA-X")]]
  BUTTON += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="LEGENDX")]]
  await xbot.send_file(event.chat_id, PHOTO, caption=LEGENDX,  buttons=BUTTON)




@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOY22 🔥
  PROBOYX = [[Button.url("Rᴇᴘᴏ UʟᴛʀᴀX", "https://github.com/ULTRA-OP/ULTRA-X")]]
  PROBOYX +=[[Button.url("Dᴇᴘʟᴏʏ UʟᴛʀᴀX", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2Flegendpack&template=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2Flegendpack")]]
  PROBOYX +=[[Button.url("Tᴜᴛᴏʀɪᴀʟ", "https://youtu.be/rGCSSFPsS4Q"), Button.url("Sᴛʀɪɴɢ Sᴇssɪᴏɴ", "https://repl.it/@legendx22/LEGEND-BOT#main.py")]]
  PROBOYX +=[[Button.url("Aᴘɪ Iᴅ & Aᴘɪ Hᴀsʜ", "https://t.me/usetgxbot"), Button.url("Rᴇᴅɪs", "https://redislabs.com")]]
  PROBOYX +=[[Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ", "https://t.me/LEGENDBOT_OFFICIAL"), Button.url("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", "https://t.me/UltraXChat")]]
  PROBOYX +=[[custom.Button.inline("«« Aʟɪᴠᴇ", data="PROBOY")]]
  await event.edit(text=f"Aʟʟ Dᴇᴛᴀɪʟs Oғ Rᴇᴘᴏs", buttons=PROBOYX)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOY22 🔥
  LEGENDX = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
  LEGENDX += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
  LEGENDX += f"**{BOT} Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
  LEGENDX += f"**Usᴇʀ** : @{bot.me.username}\n\n"
  LEGENDX += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
  LEGENDX += "**Tᴇʟᴇᴛʜᴏɴ** : `1.20`\n\n"
  LEGENDX += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
  BUTTONS = [[Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/ULTRA-OP/ULTRA-X")]]
  BUTTONS += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="LEGENDX")]]
  await event.edit(text=LEGENDX, buttons=BUTTONS)


@xbot.on(events.NewMessage(pattern=("/repo")))
async def repo(event):
  await xbot.send_message(event.chat, "**Hᴇʀᴇ Is Tʜᴇ Rᴇᴘᴏ Fᴏʀ υℓтяα χ Usᴇʀʙᴏᴛ** \n\nFᴏʀ Aɴʏ Hᴇʟᴘ :- @UltraXOT", buttons=[[Button.url("🔰 Rᴇᴘᴏ 🔰", "https://github.com/ULTRA-OP/ULTRA-X")]])


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@xbot.on(events.NewMessage(pattern="/ping"))
async def ok(event):
    start_time = datetime.datetime.now()
    message = await event.reply("_.._.._Pinging_.._.._")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b><i>☞ Pᴏɴɢ !!</i></b>\n"
        "<b>➥ Tɪᴍᴇ Tᴀᴋᴇɴ:</b> <code>{}</code>\n"
        "<b>➥ Sᴇʀᴠɪᴄᴇ Uᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )


Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
@xbot.on(events.NewMessage(pattern="/set"))
async def heroku(event):
  if event.sender_id == bot.me.id or event.sender_id == ID:
    pro = [[Button.inline("🙂 BOT NICK NAME 🙂", data="nick")]]
    pro += [[Button.inline("🙂 ALIVE PHOTO 🙂", data="alive_photo")]]
    pro += [[Button.inline("🙂 FBAN GROUP ID 🙂", data="fban_id")]]
    pro += [[Button.inline("🙂 ALIVE_NAME 🙂", data="alive_name")]]
    pro += [[Button.inline("🙂 STRING SESSION 🙂", data="session")]]
    await xbot.send_message(event.chat_id, "choose", buttons=pro)
  else:
    await event.reply("JNL, Mera bot mat chuu!!")
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'ass_back')))
async def heroku(event):
  if event.sender_id == bot.me.id or event.sender_id == ID:
    pro = [[Button.inline("🙂 BOT NICK NAME 🙂", data="nick")]]
    pro += [[Button.inline("🙂 ALIVE PHOTO 🙂", data="alive_photo")]]
    pro += [[Button.inline("🙂 FBAN GROUP ID 🙂", data="fban_id")]]
    pro += [[Button.inline("🙂 ALIVE_NAME 🙂", data="alive_name")]]
    pro += [[Button.inline("🙂 STRING SESSION 🙂", data="session")]]
    await event.edit("choose", buttons=pro)
  else:
    await event.answer("JNL, Mera bot mat chu!!", alert=True)
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'setnick')))
async def heroku(event):
  Pro = bot.me.id
  global Heroku
  app = Heroku.app(Var.HEROKU_APP_NAME)
  heroku_var = app.config()
  if event.sender_id == Pro or event.sender_id == ID:
     if event.is_private:
        await event.delete()
        async with xbot.conversation(event.chat_id) as pro:
          await pro.send_message("Give your value....")
          op = await pro.get_response()
          await pro.send_message("Now wait..I am restarting./.\./.\.")
          try:
            heroku_var['BOT_NICK_NAME'] = f'{op.message}'
          except Exception as e:
            await event.reply(f"{e}")  
     else:
         warn = "Please use this in PM"
         await event.answer(warn, alert=True)
  else:
     pro = "Chala ja bhosdike.."
     await event.answer(pro, alert=True)

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'setphoto')))
async def heroku(event):
  Pro = bot.me.id
  global Heroku
  app = Heroku.app(Var.HEROKU_APP_NAME)
  heroku_var = app.config()
  if event.sender_id == Pro or event.sender_id == ID:
     if event.is_private:
        await event.delete()
        async with xbot.conversation(event.chat_id) as pro:
          await pro.send_message("Give your value....")
          op = await pro.get_response()
          await pro.send_message("Now wait..I am restarting./.\./.\.")
          try:
            heroku_var['ALIVE_PHOTTO'] = f'{op.message}'
          except Exception as e:
            await event.reply(f"{e}")  
     else:
         warn = "Please use this in PM"
         await event.answer(warn, alert=True)
  else:
     pro = "Chala ja bhosdike.."
     await event.answer(pro, alert=True)

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'setfban')))
async def heroku(event):
  Pro = bot.me.id
  global Heroku
  app = Heroku.app(Var.HEROKU_APP_NAME)
  heroku_var = app.config()
  if event.sender_id == Pro or event.sender_id == ID:
     if event.is_private:
        await event.delete()
        async with xbot.conversation(event.chat_id) as pro:
          await pro.send_message("Give your value....")
          op = await pro.get_response()
          await pro.send_message("Now wait..I am restarting./.\./.\.")
          try:
            heroku_var['FBAN_GROUP_ID'] = f'{op.message}'
          except Exception as e:
            await event.reply(f"{e}")  
     else:
         warn = "Please use this in PM"
         await event.answer(warn, alert=True)
  else:
     pro = "Chala ja bhosdike.."
     await event.answer(pro, alert=True)

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'setname')))
async def heroku(event):
  Pro = bot.me.id
  global Heroku
  app = Heroku.app(Var.HEROKU_APP_NAME)
  heroku_var = app.config()
  if event.sender_id == Pro or event.sender_id == Id:
     if event.is_private:
        await event.delete()
        async with xbot.conversation(event.chat_id) as pro:
          await pro.send_message("Give your value....")
          op = await pro.get_response()
          await pro.send_message("Now wait..I am restarting./.\./.\.")
          try:
            heroku_var['ALIVE_NAME'] = f'{op.message}'
          except Exception as e:
            await event.reply(f"{e}")  
     else:
         warn = "Please use this in PM"
         await event.answer(warn, alert=True)
  else:
     pro = "Chala ja bhosdike.."
     await event.answer(pro, alert=True)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'setsession')))
async def heroku(event):
  Pro = bot.me.id
  global Heroku
  app = Heroku.app(Var.HEROKU_APP_NAME)
  heroku_var = app.config()
  if event.sender_id == Pro or event.sender_id == ID:
     if event.is_private:
        await event.delete()
        async with xbot.conversation(event.chat_id) as pro:
          await pro.send_message("Give your value....")
          op = await pro.get_response()
          await pro.send_message("Now wait..I am restarting./.\./.\.")
          try:
            heroku_var['STRING_SESSION'] = f'{op.message}'
          except Exception as e:
            await event.reply(f"{e}")  
     else:
         warn = "Please use this in PM"
         await event.answer(warn, alert=True)
  else:
     pro = "Chala ja bhosdike.."
     await event.answer(pro, alert=True)

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'nick')))
async def call_back(event):
  legend = [[Button.inline("SET ?", data='setnick')]]
  legend += [[Button.inline("«« BACK", data='ass_back')]]
  if event.is_private:
    await event.edit("Want to set the bot name", buttons=legend)
  else:
    pro = "Please use this in PM"
    await event.answer(pro, alert=False)



@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'alive_name')))
async def call_back(event):
  legend = [[Button.inline("SET ?", data='setname')]]
  legend += [[Button.inline("«« BACK", data='ass_back')]]
  if event.is_private:
    await event.edit("Want to set your name", buttons=legend)
  else:
    pro = "Please use this in PM"
    await event.answer(pro, alert=False)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'session')))
async def call_back(event):
  legend = [[Button.inline("SET ?", data='setsession')]]
  legend += [[Button.inline("«« BACK", data='ass_back')]]
  if event.is_private:
    await event.edit("Want to set your StringSession", buttons=legend)
  else:
    pro = "Please use this in PM"
    await event.answer(pro, alert=False)



@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'fban_id')))
async def call_back(event):
  legend = [[Button.inline("SET ?", data='setfban')]]
  legend += [[Button.inline("«« BACK", data='ass_back')]]
  if event.is_private:
    await event.edit("Want to set the FBAN ID", buttons=legend)
  else:
    pro = "Please use this in PM"
    await event.answer(pro, alert=False)



@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'alive_photo')))
async def call_back(event):
  legend = [[Button.inline("SET ?", data='setphoto')]]
  legend += [[Button.inline("«« BACK", data='ass_back')]]
  if event.is_private:
    await event.edit("Want to set your photo", buttons=legend)
  else:
    pro = "Please use this in PM"
    await event.answer(pro, alert=False)
