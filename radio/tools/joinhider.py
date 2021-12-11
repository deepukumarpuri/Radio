import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = os.environ.get("BOT_TOKEN", "")
API_HASH = os.environ.get("BOT_TOKEN", "")

DkBotz = Client(
        "DKBOTZ",
        bot_token=BOT_TOKEN,
	api_hash=API_HASH,
        api_id=API_ID
    )


@DkBotz.on_message(filters.new_chat_members)
async def welcome(bot, message):
	await message.delete()	
	
@DkBotz.on_message(filters.left_chat_member)
async def goodbye(bot, message):
	await message.delete()	


	
DkBotz.run()
#just a simple . nothing special.
