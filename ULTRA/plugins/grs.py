""" Powered by @Google
Available Commands:
.grs <query> """

import asyncio
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from google_images_download import google_images_download
from ULTRA.utils import admin_cmd, sudo_cmd

@borg.on(admin_cmd(pattern="grs$"))
@borg.on(sudo_cmd(pattern="grs$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    OUTPUT_STR = "`Reply to an image to do Google Reverse Search....`"
    if event.reply_to_msg_id:
        madboyevent = await edit_or_reply(event, "`Pre Processing Media....`")
        previous_message = await event.get_reply_message()
        previous_message_text = previous_message.message
        BASE_URL = "http://www.google.com"
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            SEARCH_URL = "{}/searchbyimage/upload".format(BASE_URL)
            multipart = {
                "encoded_image": (
                    downloaded_file_name,
                    open(downloaded_file_name, "rb"),
                ),
                "image_content": "",
            }
            # https://stackoverflow.com/a/28792943/4723940
            google_rs_response = requests.post(
                SEARCH_URL, files=multipart, allow_redirects=False
            )
            the_location = google_rs_response.headers.get("Location")
            os.remove(downloaded_file_name)
        else:
            previous_message_text = previous_message.message
            SEARCH_URL = "{}/searchbyimage?image_url={}"
            request_url = SEARCH_URL.format(BASE_URL, previous_message_text)
            google_rs_response = requests.get(request_url, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
        await madboyevent.edit("`Found Google Result. Pouring some soup on it!!!!`")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        # document.getElementsByClassName("r5a77d"): PRS
        try:
            prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
            prs_anchor_element = prs_div.find("a")
            prs_url = BASE_URL + prs_anchor_element.get("href")
            prs_text = prs_anchor_element.text
            # document.getElementById("jHnbRc")
            img_size_div = soup.find(id="jHnbRc")
            img_size = img_size_div.find_all("div")
        except Exception:
            return await edit_delete(
                madboyevent, "`Sorry, I'm unable to find similar images!.!.`"
            )
        end = datetime.now()
        ms = (end - start).seconds
        OUTPUT_STR = """
        <b>┏━━━━━━━━━━━━━━━━━━━━━</b>\n<b>┣ {img_size}\n<b>┣ Possible Related Search:</b> <a href="{prs_url}">{prs_text}</a> \n<b>┣ More Info:</b> Open this <a href="{the_location}">Link</a> \n<b>┣ </b><i>Fetched in {ms} seconds</i>\n<b>┗━━━━━━━━━━━━━━━━━━━━━</b>""".format(
            **locals()
 )
    await madboyevent.edit(OUTPUT_STR, parse_mode="HTML", link_preview=False)
