"""
Made By @Rohithaditya Inspired by Xditya Telebot Anime dp 
kang = keep all lines 
dont kang blindly 
after reading this and you removed = U will be blitch son 
# (C) @GodhackerzULTRA
# Space DP
# GOT THIS Idea FROM TELEBOT
# KEEP CREDITS IF YOU KANG 
# Wrote BY @Rohithaditya
# KEEP ABove Lines 
"""
import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from ULTRA import CMD_HELP
from ULTRA.utils import admin_cmd

COLLECTION_STRING = [
                  "tron-background"
		  "iron-man-jarvis-animated-wallpaper"
		  "batcomputer-wallpaper"
]
# ----------------For @GodhackerzULTRA-------------------------------------------------------------------Wrote BY @Rohithaditya-----------------------------------------

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile(r"/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")

# ----------------For @GodhackerzULTRA-------------------------------------------------------------------Wrote BY @Rohithaditya-----------------------------------------
@borg.on(admin_cmd(pattern="sethackerdp ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting  DP..\n\nDone !!! Check Your DP in 5 seconds. By [GODHACKERZUSERBOT](https://github.com/rohithaditya/Godhackerz-ULTRA)**"
    )

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(600)  # Edit this to your required needs

# ----------------For @GodhackerzULTRA-------------------------------------------------------------------Wrote BY @Rohithaditya-----------------------------------------
