from pyrogram import Client, idle
# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
from config import API_ID, API_HASH, BOT_TOKEN, PRO_USERS
from radio.radio import app
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="radio"),
)
    PRO_USERS.add(184752635)
    
bot.start()
app.start()
idle()
