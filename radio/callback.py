from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from config import (
    RADIO_BOT,
    MUSICBOT,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    ASSISTANT_USERNAME,
    ASSISTANT_NAME,
    UPDATES_CHANNEL,
)

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🌐 **Bot information**

🤖 __This Bot Was Created To Play RADIO in Telegram Group in Voice Chats And Many More Tools__ 

💡 __Powered By PyTgcalls The Async client API for the Telegram Group Calls, And Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users And Bots.__


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
    await query.edit_message_text(
        f"""✨ **Hello  User !**\n
✨ **I Am a Telegram Most Powerful [{RADIO_BOT}](https://t.me/{BOT_USERNAME}).**\n\n💭 **I Was Created To Play Radio in Group Voice Chats Easily.**\n\n❔ **To Find Out How To Use Me, Press The Help Button Below** 👇🏻\n Must Be Read Terms & Condition For Bot Adding in Your Group

💡 **Find out all the Bot's commands and how they work by clicking On The » 📚 Commands Button!**

🔖 **To know how to use this bot, please click on the Below Button**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❔ HOW TO USE THIS BOT", callback_data="cbguide",
                    )
                ],
                [InlineKeyboardButton("📚 Commands", callback_data="dkcmd")],
                [
                    InlineKeyboardButton("🌐 Terms & Condition", callback_data="cbinfo"),
                    InlineKeyboardButton("❤️ Donate", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "✨ NEW Features Coming Soon", callback_data="cbfeatures"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("dkcmd"))
async def dkcmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello !**

» **Press The Button Below To Read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📘 Admin Command", callback_data="cbadmin"),
                    InlineKeyboardButton("📗 Sudo Command", callback_data="cbsudo"),
                ],
                [
                    InlineKeyboardButton("📙 Owner Command", callback_data="cbowner"),
                    InlineKeyboardButton("🌐 Terms & Condition", callback_data="cbinfo"),
                ],
                [InlineKeyboardButton("❤️ Donate", url=f"https://t.me/{OWNER_NAME}")],
                [InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")],
            ]
        ),
    )


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

@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Here is The Admin Commands**

/radio Radio Station Link - To Play 24 Hours Music in Your Group
/stop - Stop Radio Playing in Group

🏮 **Here is The Group Users Commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="dkcmd")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Here is The SUDO Users Commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/clear - remove all .jpg files
/eval (query) - execute code
/sh (query) - run code
/update - Update @{MUSICBOT}
/setvar - Set Var Of @{MUSICBOT}
/delvar - Delete Var Of @{MUSICBOT}

🏮 **Here is The NOOB Users Commands**
This Tools For Control @{MUSICBOT}. This Command Allow For Some Users. Contact To @DKBOTZHELP

/usage - Check @{MUSICBOT} Dyno Usage
/reset - Reset @{MUSICBOT} Bot
/logs - Check @{MUSICBOT} Bot log
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="dkcmd")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Here is The Owner Commands**

/stats - show the bot statistic
/broadcast (reply to message) - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 Note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="dkcmd")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbfeature"))
async def cbfeature(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""**Here is The ✨ NEW Features Coming Soon in Bot**

✨ Games Playing in Group

✨ Deezer Song Downloading Features

✨ Jio Savan Song Downloading Features

✨ Ban And Unban Users Features For Group

✨ Mute And Unmute Users Features For Group

⚡ Premium Features ⚡

✨ Pro Users Tools ✨

__This Bot Licensed Under GNU-GPL 3.0 License By @DKBOTZ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🏡 Go Back", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )