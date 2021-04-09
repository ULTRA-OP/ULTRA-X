""" 
FOR ALL DEVS I EDITED IT 
(C) @ROHTIHADITYA
(C) @PROBOYX
(C) @ROSELOVERX SCAMMER NOT IN TEAMULTRA OR TEAMLEGEND
(C) @LEGENDX22
(C) @NubBoy_007
"""
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from ULTRA import CMD_HELP
from ULTRA.utils import admin_cmd, sudo_cmd
import html
from ULTRAX import POST
from telethon import events
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from telethon.events import ChatAction
from ULTRAX import devs
async def get_full_user(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`User ID Is Required")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("**SOMETHING W3NT WRONG 🤔**", str(err))           
    return user_obj, extra


async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

@borg.on(admin_cmd(pattern="gban ?(.*)"))
@borg.on(sudo_cmd("gban ?(.*)", allow_sudo=True))
async def gspider(ULTRA):
    lol = ULTRA
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        friday = await lol.reply("GBanning This Retard DumbAss😁😁")
    else:
        friday = await lol.edit("Wait Processing.....")
    me = await ULTRA.client.get_me()
    await friday.edit(f"Global Ban Is Coming ! Wait And Watch You bitch😎🔥")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await ULTRA.get_chat()
    a = b = 0
    if ULTRA.is_private:
        user = ULTRA.chat
        reason = ULTRA.pattern_match.group(1)
    else:
        ULTRA.chat.title
    try:
        user, reason = await get_full_user(ULTRA)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await friday.edit(f"**Something W3NT Wrong 🤔**")
    if user:
        if user.id in devs:
            return await friday.edit(
                f"**Didn't, Your Father Teach You ? That You Can't Gban My Creator😑😑🖕**"
            )
        try:
            from ULTRA.modules.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await ULTRA.client(BlockRequest(user))
        except:
            pass
        testULTRA = [
            d.entity.id
            for d in await ULTRA.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testULTRA:
            try:
                await ULTRA.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await friday.edit(f"**GBANNING [{user.first_name}](tg://user?id={user.id})**\n\n__Please be Patient..This process takes time.__")
            except:
                b += 1
    else:
        await friday.edit(f"**Reply to a user !!**")
    try:
        if gmute(user.id) is False:
            return await friday.edit(f"**Error! User probably already gbanned.**")
    except:
        pass
    POST(user=user.id, msg=ULTRA.text[5:])
    await friday.edit(
        f"**Successfully GBanned [{user.first_name}](tg://user?id={user.id}) // Total Affected Chats :** `{a}` "
    )
    return


@borg.on(admin_cmd(pattern="ungban ?(.*)"))
async def gspider(ULTRA):
    lol = ULTRA
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        friday = await lol.reply("`Wait Let Me Process`")
    else:
        friday = await lol.edit("Just a Second ")
    me = await ULTRA.client.get_me()
    await friday.edit(f"Trying To Ungban User !")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await ULTRA.get_chat()
    a = b = 0
    if ULTRA.is_private:
        user = ULTRA.chat
        reason = ULTRA.pattern_match.group(1)
    else:
        ULTRA.chat.title
    try:
        user, reason = await get_full_user(ULTRA)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await friday.edit("**SOMETHING W3NT WRONG 🤔**")
    if user:
        if user.id in devs:
            return await friday.edit("**You Cant gban him... as a result you can not ungban him... He is My Creator!**")
        try:
            from ULTRA.modules.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await ULTRA.client(UnblockRequest(user))
        except:
            pass
        testULTRA = [
            d.entity.id
            for d in await ULTRA.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testULTRA:
            try:
                await ULTRA.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await friday.edit(f"**UNGBANNING [{user.first_name}](tg://user?id={user.id})**\n\n__Please be Patient..This process takes time.__")
            except:
                b += 1
    else:
        await friday.edit("**Reply to a user !!**")
    try:
        if ungmute(user.id) is False:
            return await friday.edit("**Error! User probably already ungbanned.**")
    except:
        pass
    return await friday.edit(
        f"**Successfully UnGBanned // USER - [{user.first_name}](tg://user?id={user.id}) IN CHATS :** `{a}`"
    )




@borg.on(ChatAction)
async def handler(rkG): 
   client = borg
   if rkG.user_joined or rkG.user_added:      
       try:       	
         from ULTRA.modules.sql_helper.gmute_sql import is_gmuted
         guser = await rkG.get_user()      
         gmuted = is_gmuted(guser.id)             
       except:      
          return
       if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):                                                                         
                chat = await rkG.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(rkG.chat_id, guser.id, view_messages=False)                              
                    await rkG.reply(
                     f"**Gbanned User Joined!!** \n"                      
                     f"**➥ Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**➥ Action **  : `Banned`")                                                
                 except:       
                    rkG.reply("`No Permission To Ban`")                   
                    return 
CMD_HELP.update({
    "gban":"gban any user using username or tag dont use id "})
