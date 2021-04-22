from ..utils import admin_cmd as ultra_cmd
@bot.on(ultra_cmd(pattern="gkick"))
async def kick(kick):
    xxx = await kick.edit("`Gʟᴏʙᴀʟʟʏ ᴋɪᴄᴋɪɴɢ ᴛʜɪs ɴᴏᴏʙ ᴋɪᴅᴅᴏ`")
    ids = (await kick.get_reply_message()).sender_id
    name = (await bot.get_entity(ids)).first_name
    ohk = (await bot.get_entity(ids)).id
    t = 0
    async for p in bot.iter_dialogs():
        if p.is_group or p.is_channel:
            try:
                await bot.kick_participant(p.id, ids)
                t += 1
            except:
                pass
    await xxx.edit(f"**Gʟᴏʙᴀʟʟʏ Kɪᴄᴋᴇᴅ [{name}](tg://user?id={ohk}) \\ Cʜᴀᴛs Aғғᴇᴄᴛᴇᴅ: {t}**")
