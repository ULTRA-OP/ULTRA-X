from ULTRA.utils import admin_cmd
@bot.on(admin_cmd(pattern="help"))
async def repo(event):
    if event.fwd_from:
        return
    LEGENDX = Var.TG_BOT_USER_NAME_BF_HER
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(LEGENDX, "Userbot")
    await response[0].click(event.chat_id)
    await event.delete()