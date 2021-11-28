import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_NAME = os.getenv("SESSION_NAME")
BOT_USERNAME = getenv("BOT_USERNAME", "veezmusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DKBOTZ")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DKBOTZ")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DKBOTZ")
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAME", "DKBOTZ")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAME", "DKBOTZ")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID"))
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/levina-lab/VeezMusic"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)

