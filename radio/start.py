from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 
from config import BOT_NAME

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**Hey I am Radio Bot 📻\n\n** \n`Use Me To Play Radio in Vc` \n\n** 💠 List Of Commands\n\n /radio link :- To Play Radio\n /stop :- Stop Radio\n\nWant Add Me in Your Group Contact To My Owner :- @DKBOTZHEP",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Support", url="t.me/DK_BOTZ")
                                    ]]
                            ))
   else:
      await m.reply(f"**@{BOT_NAME} is Alive! ✨**")
