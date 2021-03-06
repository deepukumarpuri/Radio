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
    f"""๐ **Bot information**

๐ค __This Bot Was Created To Play RADIO in Telegram Group in Voice Chats And Many More Tools__ 

๐ก __Powered By PyTgcalls The Async client API for the Telegram Group Calls, And Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users And Bots.__


More information Contact To My Owner :- @DKBOTZHELP


__This Bot Licensed Under GNU-GPL 3.0 License By @DKBOTZ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "๐ก Go Back", callback_data="cbstart")
      ]]
    ))

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Hello  User !**\n
โจ **I Am a Telegram Most Powerful [{RADIO_BOT}](https://t.me/{BOT_USERNAME}).**\n\n๐ญ **I Was Created To Play Radio in Group Voice Chats Easily.**\n\nโ **To Find Out How To Use Me, Press The Help Button Below** ๐๐ป\n Must Be Read Terms & Condition For Bot Adding in Your Group

๐ก **Find out all the Bot's commands and how they work by clicking On The ยป ๐ Commands Button!**

๐ **To know how to use this bot, please click on the Below Button**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ HOW TO USE THIS BOT", callback_data="cbguide",
                    )
                ],
                [InlineKeyboardButton("๐ Commands", callback_data="dkcmd")],
                [
                    InlineKeyboardButton("๐ Terms & Condition", callback_data="cbinfo"),
                    InlineKeyboardButton("โค๏ธ Donate", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฅ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "โจ NEW Features Coming Soon", callback_data="cbfeatures"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("dkcmd"))
async def dkcmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Hello !**

ยป **Press The Button Below To Read the explanation and see the list of available commands !**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ Admin Command", callback_data="cbadmin"),
                    InlineKeyboardButton("๐ Sudo Command", callback_data="cbsudo"),
                ],
                [
                    InlineKeyboardButton("๐ Owner Command", callback_data="cbowner"),
                    InlineKeyboardButton("๐ Terms & Condition", callback_data="cbinfo"),
                ],
                [InlineKeyboardButton("โค๏ธ Donate", url=f"https://t.me/{OWNER_NAME}")],
                [InlineKeyboardButton("๐ Go Back", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""๐ **Terms & Condition** For Bot Adding in Group

This Bot Only Add My Owner. 

You Can Use in Your Group To Play 24 Hours Radio

No Sound Errors 

You Can Buy Radio Bot Premium To Use Me in Your Group From My Owner. Price Of Radio Bot Premium :- @DKBOTZNETWORK

More information Contact To My Owner :- @DKBOTZHELP


__This Bot Licensed Under GNU-GPL 3.0 License By @DKBOTZ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "๐ก Go Back", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )

@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ **Here is The Admin Commands**

/radio Radio Station Link - To Play 24 Hours Music in Your Group
/stop - Stop Radio Playing in Group

๐ฎ **Here is The Group Users Commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="dkcmd")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ **Here is The SUDO Users Commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/clear - remove all .jpg files
/eval (query) - execute code
/sh (query) - run code
/update - Update @{MUSICBOT}
/setvar - Set Var Of @{MUSICBOT}
/delvar - Delete Var Of @{MUSICBOT}

๐ฎ **Here is The NOOB Users Commands**
This Tools For Control @{MUSICBOT}. This Command Allow For Some Users. Contact To @DKBOTZHELP

/usage - Check @{MUSICBOT} Dyno Usage
/restart - Reset @{MUSICBOT} Bot
/logs - Check @{MUSICBOT} Bot log
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="dkcmd")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ **Here is The Owner Commands**

/stats - show the bot statistic
/broadcast (reply to message) - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

๐ Note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="dkcmd")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbfeature"))
async def cbfeature(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""**Here is The โจ NEW Features Coming Soon in Bot**

โจ Games Playing in Group

โจ Deezer Song Downloading Features

โจ Jio Savan Song Downloading Features

โจ Ban And Unban Users Features For Group

โจ Mute And Unmute Users Features For Group

โก Premium Features โก

โจ Pro Users Tools โจ

__This Bot Licensed Under GNU-GPL 3.0 License By @DKBOTZ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "๐ก Go Back", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )
