from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🌐 **Bot information**

🤖 __This Bot Was Created To Play RADIO in Telegram Group in Voice Chats__

💡 __Powered By PyTgcalls The Async client API for the Telegram Group Calls, And Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users And Bots.__


❄1�7 HOW TO USE THIS BOT

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
  await query.edit_message_text(f"�7�8 **Hello, I Am a Telegram Most Powerful RADIO Bot.**\n\n�9�7 **I Was Created To Play Radio in Group Voice chats easily.**\n\n�7�2 **To Find Out How To Use Me, Press The Help Button Below** �9�5�9�9\n Must Be Read Terms & Condition For Bot Adding in Your Group",
                                reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "❄1�7 HOW TO USE THIS BOT", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "🌐 Terms & Condition", callback_data="cbinfo")
                       ],[
                          InlineKeyboardButton(
                             "👩🏻‍💄1�7 Developer", url="https://t.me/DKBOTZHELP")
                       ],[
                          InlineKeyboardButton(
                             "💭 Group", url="https://t.me/DK_BOTZ"),
                          InlineKeyboardButton(
                             "✄1�7 Channel", url="https://t.me/DKBOTZ")
                       ]]
                    ))

@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🌐 **Terms & Condition** For Bot Adding in Group

This Bot Only Add My Owner. 

You Can Use Me in Your Group To Play 24 Hours Radio in Your Group.

No Sound Errors

You Can Buy Bot Premium To Use Me in Your Group From My Owner. Price Of Bot Premium :- @DKBOTZNETWORK

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
