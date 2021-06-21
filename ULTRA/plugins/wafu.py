#some codes by javes
import os
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from ULTRA import bot , CMD_HELP
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from ULTRA import TEMP_DOWNLOAD_DIRECTORY
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
import   os,re, bs4, requests, io
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from telethon import events
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from pathlib import Path
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX
from os import remove
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from bs4 import BeautifulSoup
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from re import findall
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from urllib.parse import quote_plus
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from requests import get
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from PIL import Image
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from telethon.tl.types import MessageMediaPhoto
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
import urllib
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from bs4 import BeautifulSoup
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
opener = urllib.request.build_opener() ; useragent = 'Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 Mobile Safari/537.36' ; opener.addheaders = [('User-agent', useragent)]
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
from ..data.waifu_db import *
async def ParseSauce(googleurl):   
    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, 'html.parser')
    results = {'similar_images': '', 'best_guess': ''}
    try:
        for similar_image in soup.findAll('input', {'class': 'gLFyf'}):
            url = 'https://www.google.com/search?tbm=isch&q=' + \
                urllib.parse.quote_plus(similar_image.get('value'))
            results['similar_images'] = url
    except BaseException:
        pass
    for best_guess in soup.findAll('div', attrs={'class': 'r5a77d'}):
        results['best_guess'] = best_guess.get_text()
    return results
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
async def scam(results, lim):
    single = opener.open(results['similar_images']).read()
    decoded = single.decode('utf-8')
    imglinks = []
    counter = 0
    pattern = r'^,\[\"(.*[!png|!jpg|!jpeg])\",[0-9]+,[0-9]+\]$'
    oboi = re.findall(pattern, decoded, re.I | re.M)
    for imglink in oboi:
        counter += 1
        if not counter >= int(lim):
            imglinks.append(imglink)
        else:
            break
    return imglinks
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
async def chrome(chrome_options=None):
    if chrome_options is None:
        chrome_options = await options()
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.mkdir(TEMP_DOWNLOAD_DIRECTORY)
    prefs = {'download.default_directory': TEMP_DOWNLOAD_DIRECTORY}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    return driver
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX

from ..utils import admin_cmd
@bot.on(admin_cmd(pattern='addwafu'))
async def addwaifu(event):
  if not event.is_group:
    return await event.edit('Use in Group')
  if await is_waifu(event.chat_id):
    return await event.edit('this chat is already setted on waifu list')
  await add_waifu(event.chat_id)
  await event.edit("waifu system online for this chat")

@bot.on(admin_cmd(pattern='rmwafu'))
async def rmwaifu(event):
  if not event.is_group:
    return await event.edit('Use in Group')
  if not await is_waifu(event.chat_id):
    return await event.edit('this chat is already not on waifu list')
  await rm_waifu(event.chat_id)
  await event.edit("waifu system offline for this chat")

@bot.on(admin_cmd(pattern='wafu'))
async def addwaifu(event):
  allwaifu = await all_waifu()
  if not allwaifu:
    return await event.edit("waifu plug-in is offline no chat added on db type `.addwafu`")
  string = "**WAIFU CHATS LIST**\n"
  for x in allwaifu:
    string += f'`{x}`\n'
  await event.edit(string)


@bot.on(admin_cmd(pattern='checkwafu'))
async def addwaifu(event):
  if not event.is_group:
    return await event.edit('Use in Group')
  if await is_waifu(event.chat_id):
    return await event.edit('this chat is added on waifu list')
  await event.edit("this chat not added waifu list")


@bot.on(events.NewMessage(incoming=True))
async def on_new_message(event):
		

        all_chats = await all_waifu()
        name = event.raw_text
        snip = """A qt waifu appeared!
Add them to your harem by sending /protecc character name"""
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
				
                      
                      photo = io.BytesIO()
                      await event.client.download_media(event.media, photo)
                      image = Image.open(photo)
                      name = "okgoogle.png"
                      image.save(name, "PNG")
                      image.close()
                      searchUrl = 'https://www.google.com/searchbyimage/upload'
                      multipart = {
                              'encoded_image': (name, open(name, 'rb')),
                              'image_content': ''
                      }
                      response = requests.post(searchUrl,
                                                                       files=multipart,
                                                                       allow_redirects=False)
                      fetchUrl = response.headers['Location']
                      match = await ParseSauce(fetchUrl +"&preferences?hl=en&fg=1#languages")
                      guess = match['best_guess']
                      guesss = guess[12:]
                      if event.chat_id in all_chats:
                        await event.reply( f"/protecc {guesss}")
            except Exception as e:
                pass
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made#Made by PROBOYX, LEGENDX
#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX#Made by PROBOYX, LEGENDX
