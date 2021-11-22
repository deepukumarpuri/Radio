from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, Chat, CallbackQuery

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
      await m.reply(f"✨ **Hello, I Am a Telegram Most Powerful RADIO Bot.**\n\n💭 **I Was Created To Play Radio in Group Voice chats easily.**\n\n❔ **To Find Out How To Use Me, Press The Help Button Below** 👇🏻\n Must Be Read Terms & Condition For Bot Adding in Your Group",
                    reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "❔ HOW TO USE THIS BOT", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "🌐 Terms & Condition", callback_data="cbinfo")
                       ],[
                          InlineKeyboardButton(
                             "👩🏻‍💻 Developer", url="https://t.me/DKBOTZHELP")
                       ],[
                          InlineKeyboardButton(
                             "💭 Group", url="https://t.me/DK_BOTZ"),
                          InlineKeyboardButton(
                             "✨ Channel", url="https://t.me/DKBOTZ")
                       ]]
                    ))
   else:
      await m.reply("**✨ Bot is Online Now ✨**")
