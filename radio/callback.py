from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""馃寪 **Bot information**

馃 __This Bot Was Created To Play RADIO in Telegram Group in Voice Chats__

馃挕 __Powered By PyTgcalls The Async client API for the Telegram Group Calls, And Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users And Bots.__


鉂� HOW TO USE THIS BOT

/radio Radio Station Link - To Play 24 Hours Music in Your Group
/stop - Stop Radio Playing in Group 

More information Contact To My Owner :- @DKBOTZHELP


__This Bot Licensed Under GNU-GPL 3.0 License By @DKBOTZ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "馃彙 Go Back", callback_data="cbstart")
      ]]
    ))

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"✨ **Hello, I Am a Telegram Most Powerful RADIO Bot.**\n\n💭 **I Was Created To Play Radio in Group Voice chats easily.**\n\n❔ **To Find Out How To Use Me, Press The Help Button Below** 👇🏻\n Must Be Read Terms & Condition For Bot Adding in Your Group",
                                reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "鉂� HOW TO USE THIS BOT", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "馃寪 Terms & Condition", callback_data="cbinfo")
                       ],[
                          InlineKeyboardButton(
                             "馃懇馃徎鈥嶐煉� Developer", url="https://t.me/DKBOTZHELP")
                       ],[
                          InlineKeyboardButton(
                             "馃挱 Group", url="https://t.me/DK_BOTZ"),
                          InlineKeyboardButton(
                             "鉁� Channel", url="https://t.me/DKBOTZ")
                       ]]
                    ))

@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""馃寪 **Terms & Condition** For Bot Adding in Group

This Bot Only Add My Owner. 

You Can Use Me in Your Group To Play 24 Hours Radio in Your Group.

No Sound Errors

You Can Buy Bot Premium To Use Me in Your Group From My Owner. Price Of Bot Premium :- @DKBOTZNETWORK

More information Contact To My Owner :- @DKBOTZHELP


__This Bot Licensed Under GNU-GPL 3.0 License By @DKBOTZ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "馃彙 Go Back", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )
