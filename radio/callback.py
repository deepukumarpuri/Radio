from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""ðŸŒ **Bot information**

ðŸ¤– __This Bot Was Created To Play RADIO in Telegram Group in Voice Chats__

ðŸ’¡ __Powered By PyTgcalls The Async client API for the Telegram Group Calls, And Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users And Bots.__


â„1¤7 HOW TO USE THIS BOT

/radio Radio Station Link - To Play 24 Hours Music in Your Group
/stop - Stop Radio Playing in Group 

More information Contact To My Owner :- @DKBOTZHELP

This Bot Licensed Under GNU-GPL 3.0 License By @DKBOTZ""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ðŸ¡ Go Back", callback_data="cbstart")
      ]]
    ))

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"7¿8 **Hello, I Am a Telegram Most Powerful RADIO Bot.**\n\n”9Ú7 **I Was Created To Play Radio in Group Voice chats easily.**\n\n7Ä2 **To Find Out How To Use Me, Press The Help Button Below** ”9Ð5”9È9\n Must Be Read Terms & Condition For Bot Adding in Your Group",
                                reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "â„1¤7 HOW TO USE THIS BOT", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "ðŸŒ Terms & Condition", callback_data="cbinfo")
                       ],[
                          InlineKeyboardButton(
                             "ðŸ‘©ðŸ»â€ðŸ’„1¤7 Developer", url="https://t.me/DKBOTZHELP")
                       ],[
                          InlineKeyboardButton(
                             "ðŸ’­ Group", url="https://t.me/DK_BOTZ"),
                          InlineKeyboardButton(
                             "âœ„1¤7 Channel", url="https://t.me/DKBOTZ")
                       ]]
                    ))

@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""ðŸŒ **Terms & Condition** For Bot Adding in Group

This Bot Only Add My Owner. 

You Can Use Me in Your Group To Play 24 Hours Radio in Your Group.

No Sound Errors

You Can Buy Bot Premium To Use Me in Your Group From My Owner. Price Of Bot Premium :- @DKBOTZNETWORK

More information Contact To My Owner :- @DKBOTZHELP


__This Bot Licensed Under GNU-GPL 3.0 License By @DKBOTZ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ðŸ¡ Go Back", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )
