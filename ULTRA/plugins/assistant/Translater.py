from ULTRAX import xbot
from google_trans_new import google_translator
import requests
from PyDictionary import PyDictionary
from telethon import events
from telethon.tl import functions

@xbot.on(events.NewMessage(pattern="/tr ?(.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.reply("`/tr <LanguageCode>` as reply to a message or `/tr <LanguageCode> | <text>`")
        return
    text = text.strip()
    lan = lan.strip()
    translator = google_translator()  
    try:
        translated = translator.translate(text,lang_tgt=lan)  
        after_tr_text = translated
        detect_result = translator.detect(text)
        output_str = (
            "**TRANSLATED** from {} to {}\n\n"
            "{}"
        ).format(
            detect_result[0],
            lan,
            after_tr_text
        )
        await event.reply(output_str)
    except Exception as exc:
        await event.reply(str(exc))

@xbot.on(events.NewMessage(pattern="/define"))
async def _(event):
    text = event.text[len("/define "):]
    word = f"{text}"
    let = dictionary.meaning(word)
    set = str(let)
    jet = set.replace("{", "")
    net = jet.replace("}", "")
    got = net.replace("'", "")
    await event.reply(got)

@xbot.on(events.NewMessage(pattern="/ud"))
async def _(event):
    text = event.text[len("/ud "):]
    results = requests.get(f'http://api.urbandictionary.com/v0/define?term={text}').json()
    try:
        reply_text = f'**{text}**\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
    except:
        reply_text = "No results found."
    await event.reply(reply_text)

