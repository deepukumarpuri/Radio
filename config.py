import os
from os import getenv
from os import environ
from dotenv import load_dotenv
from radio.uptools import fetch_heroku_git_url

load_dotenv()
que = {}
admins = {}
#BOT SETTINGS
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "VC RADIO PLAY BOT")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "VC_RADIO_PLAY_BOT")
RADIO_BOT = getenv("RADIO_BOT", "VC RADIO PLAY BOT")
MUSICBOT = getenv("MUSICBOT", "GROUP_MUSIC_PLAY_BOT")
SESSION = getenv("BOT_USERNAME")

#BOT ASSISTANT
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VC RADIO BOT PREMIUM")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "VCRADIOPLAYBOTHELPER")

#BOT PHOTOS
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/8628c642a266a22effd8c.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/4c39fbb88932761913fff.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/73e10ed6e2bd32b478de6.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
PICS = list(getenv("PICS", "https://telegra.ph/file/8b42f6caf6ef5fd76766f.jpg https://telegra.ph/file/82b5bbbab6d5e5593b6b2.jpg").split())
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")


#OWNERS CONFIG
SUDO_USERS = list(map(int, getenv("SUDO_USER", "1805398747").split()))
PRO_USERS = list(map(int, getenv("PRO_USERS", "1805398747").split()))
NOOB_USERS = list(map(int, getenv("NOOB_USERS", "1805398747").split()))
OWNER_ID = int(os.environ.get("OWNER_ID", "1805398747"))
ADMINS = int(os.environ.get("OWNER_ID", "1805398747"))

#CHANNEL AND GROUPS
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DK_BOTZ")
SUPPORT_CHAT = getenv("SUPPORT_CHATS", "DK_BOTZ")
UPDATES_CHANNEL = getenv("UPDATES_CHANNELS", "DKBOTZ")
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
AUTH_CHANNEL = int(os.environ.get("AUTH_CHANNEL"))
auth_channel = int(os.environ.get("AUTH_CHANNEL"))
INDEX_REQ_CHANNEL = int(os.environ.get("INDEX_REQ_CHANNEL", LOG_CHANNEL))

#OTHERS
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAMES", "DKBOTZHELP")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAMES", "Anonymous")

# just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

#MONGA DB URL
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DATABASE_URL = environ.get('DATABASE_URL', "mongodb://mongo:wWp1Uq4pxGd0L88A3Owm@containers-us-west-65.railway.app:5653")
DATABASE_URI = environ.get('DATABASE_URL', "mongodb://mongo:wWp1Uq4pxGd0L88A3Owm@containers-us-west-65.railway.app:5653")
DATABASE_NAME = environ.get('DATABASE_NAME', "Watermarks")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')



#IMDB SETTINGS
IMDB_TEMPLATE = getenv("IMDB_TEMPLATE", "<b>???? Title:</b> <a href={url}>{title}</a>\n<b>???? Type:</b> {kind}\n<b>???? Release:</b> <a href={url}/releaseinfo>{release_date}</a>\n<b>???? Rating:</b> <a href={url}/ratings>{rating} / 10</a>\n(based on <code>{votes}</code> user ratings.)\n\n<b>???? Runtime:</b> <code>{runtime} minutes</code>\n<b>???? Genres:</b> {genres}\n\n<b>?????? Languages:</b> {languages}\n<b>???? Countries:</b> {countries}\n<b>???? Director:</b> {director}\n<b>???? Writers:</b> {writer}\n\n<b>?? Powered by: <a href='https://t.me/+y53tWFUw6Q43NzE9'>{message.chat.title}</a></b>\n\n<b>?????? Note:</b> <s>This message will be Auto-deleted after 5 minutes to avoid copyright issues.</s>")
IMDB = getenv("IMDB", "True")
LONG_IMDB_DESCRIPTION = getenv("LONG_IMDB_DESCRIPTION", "False")
P_TTI_SHOW_OFF = getenv("P_TTI_SHOW_OFF", "True")
SPELL_CHECK_REPLY = getenv("SPELL_CHECK_REPLY", "True")
SINGLE_BUTTON = getenv("SINGLE_BUTTON", "True")
MAX_LIST_ELM = os.environ.get("MAX_LIST_ELM", None)

# UPDATER CONFIG (HEROKU)
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/levina-lab/VeezMusic"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)


# Bot settings

CACHE_TIME = os.environ.get("CACHE_TIME", 300)
USE_CAPTION_FILTER = os.environ.get("USE_CAPTION_FILTER", False)

#Heroku 2

HEROKU_APP = os.environ.get("HEROKU_APP", None)
HEROKU_API = os.environ.get("HEROKU_API", None)
