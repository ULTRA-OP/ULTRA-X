
import os
import sys
import time
from telethon.sessions import StringSession
from telethon import TelegramClient
from ULTRA.uniborgConfig import Config
from var import Var
StartTime = time.time()
os.system("pip install --upgrade pip")
if Var.STRING_SESSION:
    session_name = str(Var.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)

DEVS = [1100231654, 1636374066, 1037581197, 1695676469, 1207066133, 1732236209]
CMD_LIST = {}
# for later purposes
CMD_HELP = {}
CMD_HELP_BOT = {}
BRAIN_CHECKER = []
INT_PLUG = ""
LOAD_PLUG = {}
#from ULTRAX import xbot 
#xbot = xbot 
# PaperPlaneExtended Support Vars
ENV = os.environ.get("ENV", False)
def HELP(**LEGENDX):
	see = LEGENDX.get("NAME", None)
	helper = LEGENDX.get("HELP", None)
	if see is None:
		LEGENDX["NAME"] = __name__
		CMD_HELP.update({see: helper})
	elif helper is None:
		LEGENDX[
		    "HELP"] = "🥺🥺NOT COMMAND HELP🥺🥺\nADDED HERE\nIF YOU WANT TO KNOW ABOUT THIS PLUG-IN\nJOIN @ULTRAXCHAT"
	else:
	  CMD_HELP.update({see: helper})
	CMD_HELP.update({see: helper})


LEGEND_ID = ["1100231654"]

""" PPE initialization. """

from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
import asyncio
SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
import pylast
from pySmartDL import SmartDL
from requests import get
# Bot Logs setup:
async def eor(event, msg):
  try:
      await event.edit(msg)
  except:
       await event.reply(msg)

if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=INFO)
    LOGS = getLogger(__name__)

    # Check if the config was edited by using the already used variable.
    # Basically, its the 'virginity check' for the config file ;)
    CONFIG_CHECK = os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

    if CONFIG_CHECK:
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)

    # Logging channel/group configuration.
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except:
        pass

    # Userbot logging feature switch.
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    PATTERNS = os.environ.get("PATTERNS", ".;!,")
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\.")
  
    # Bleep Blop, this is a bot ;)
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

    # Console verbose logging
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    # SQL Database URI
    DB_URI = os.environ.get("DATABASE_URL", None)

    # OCR API key
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

    # remove.bg API key
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

    # Chrome Driver and Headless Google Chrome Binaries
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

    # OpenWeatherMap API Key
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

    # Anti Spambot Config
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))

    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

    # FedBan Premium Module
    F_BAN_LOGGER_GROUP = os.environ.get("F_BAN_LOGGER_GROUP", None)

    #make by LEGEND X 
    botnickname = os.environ.get("BOT_NICK_NAME", None)

# Heroku Credentials for updater.
    HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

   
    # Youtube API key
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

    # Default .alive name
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    AUTONAME = os.environ.get("AUTONAME", None)
    REDIRECTCHANNEL = os.environ.get("REDIRECTCHANNEL", None)

    # Time & Date - Country and Time Zone
    COUNTRY = str(os.environ.get("COUNTRY", "India"))

    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

    # Clean Welcome
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    
    # Custom Module
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    CUSTOM_AFK = os.environ.get("CUSTOM_AFK", None)

    # Upstream Repo
    UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/LEGENDXOP/LEGEND-BOT.git")

    # Last.fm Module
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    BIO_MSG = os.environ.get("BIO_MSG", None)

    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
    if not LASTFM_USERNAME == "None":
        lastfm = pylast.LastFMNetwork(api_key=LASTFM_API,
                                      api_secret=LASTFM_SECRET,
                                      username=LASTFM_USERNAME,
                                      password_hash=LASTFM_PASS)
    else:
        lastfm = None

    # Google Drive Module
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
else:
    # Put your ppe vars here if you are using local hosting
    PLACEHOLDER = None

# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
SUDO_LIST = {}

from ULTRA.helpers import *
from ULTRA.helpers import functions as legdef
