#BY SH1VAM DONT KANG
#BY SH1VAM DONT KANG
import os


from telethon import Button, custom, events, functions
  
import math
import heroku3

from ULTRA import HEROKU_APP_NAME, HEROKU_API_KEY

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
            shivamslog = builder.article(title="Cant Get It",description="Configuration Error",text="Please Check `HEROKU_APP_NAME`, It Must Be Same As Your App Name Or Check `HEROKU_API_KEY`; U Can Regenerate From https://dashboard.heroku.com/account, Scroll Down Regenerate And Change In settings Of App U Need To Reveal Config Vars",buttons=[[Button.switch_inline("Search Again", query="logs", same_peer=True)],], )
            await event.answer([shivamslog])
            return
        else:
            with open('logs.txt', 'w') as log:
                log.write(app.get_log())
            shivamlog=builder.document("logs.txt",title="Logs",description="Here iz your HEROKU APP Logs",text="Use .paste to paste in dogbin or .neko to paste in nekobin",buttons=[[Button.switch_inline("Search Again", query="logs", same_peer=True)],], )
            await event.answer([shivamlog])
            return os.remove('logs.txt')
    if not event.query.user_id == me.id:
        resultm = builder.article(title="Me iz not your Bot",description="Mind Your Own Bizness",text="Hey!! U Must Use https://github.com/ULTRA-OP/ULTRA-X",buttons=[[Button.switch_inline("Search Again", query="logs", same_peer=True)],], )
        await event.answer([resultm])
        return
