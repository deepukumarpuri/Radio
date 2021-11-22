from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🌐 **Bot information**

🤖 __This Bot Was Created To Play RADIO in Telegram Group in Voice Chats__

💡 __Powered By PyTgcalls The Async client API for the Telegram Group Calls, And Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users And Bots.__


❔ HOW TO USE THIS BOT

/radio Radio Station Link - To Play 24 Hours Music in Your Group
/stop - Stop Radio Playing in Group 

More information Contact To My Owner :- @DKBOTZHELP


__This Bot Licensed Under GNU-GPL 3.0 License By @DKBOTZ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🏡 Go Back", callback_data="cbstart")
      ]]
    ))

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"✨ **Hello, I am a telegram video streaming bot.**\n\n💭 **I was created to stream videos in group video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
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

@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🌐 **Terms & Condition** For Bot Adding in Group

This Bot Only Add My Owner. 

You Can Use in Your Group To Play 24 Hours Radio

No Sound Errors 

You Can Buy Radio Bot Premium To Use Me in Your Group From My Owner. Price Of Radio Bot Premium :- @DKBOTZNETWORK

More information Contact To My Owner :- @DKBOTZHELP


__This Bot Licensed Under GNU-GPL 3.0 License By @DKBOTZ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🏡 Go Back", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )
