from config import Config
from database.database import Database

db = Database(Config.MONGODB_URI, Config.BOT_USERNAME)
