#BY SH1VAM DONT KANG
#BY SH1VAM DONT KANG
#BY SH1VAM DONT KANG
#BY SH1VAM DONT KANG
#BY SH1VAM DONT KANG
#BY SH1VAM DONT KANG






import os


from telethon import Button, custom, events, functions
  





import math
import heroku3

from userbot import HEROKU_APP_NAME, HEROKU_API_KEY

heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"


@tgbot.on(events.InlineQuery(pattern=r"logs"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY);app = Heroku.app(HEROKU_APP_NAME)
        except:
            shivamslog = builder.article(title="Cant Get It",description="Configuration Error",text="Please Check Heroku App Name It Must Be Same As Your App Name Or Check Heroku Api Key U Can Regenerate From https://dashboard.heroku.com/account Scroll Down Regenerate And Change In settings Of App U Need To Reveal Config Vars",buttons=[[Button.switch_inline("Search Again", query="logs", same_peer=True)],], )
            await event.answer([shivamslog])
            return
        else:
            with open('logs.txt', 'w') as log:
                log.write(app.get_log())
            shivamlog=builder.document("logs.txt",title="Logs",description="logs of 100+ lines use .paste to past in dogbin",text="use .paste to paste inn dogbin",buttons=[[Button.switch_inline("Search Again", query="logs", same_peer=True)],], )
            await event.answer([shivamlog])
            return os.remove('logs.txt')
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/legendx22/LEGEND-BOT ",buttons=[[Button.switch_inline("Search Again", query="logs", same_peer=True)],], )
        await event.answer([resultm])
        return
