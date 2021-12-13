import os
import logging
import random
import asyncio
from script import Script
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from radio.database import db
from config import ADMINS, AUTH_CHANNEL, LOG_CHANNEL, PICS, OWNER_NAME
from utils import get_size, is_subscribed, temp
import re
from radio import __version__
from radio.decorators import sudo_users_only
from radio.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from datetime import datetime
from sys import version_info
from time import time
logger = logging.getLogger(__name__)

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)

@Client.on_message(filters.command("start"))
async def start(client, message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    if message.chat.type in ['group', 'supergroup']:
        buttons = [
            [
                InlineKeyboardButton('📣 Channel', url='https://t.me/DKBOTZ')
            ],
            [
                InlineKeyboardButton('📚 Commands', callback_data='dkcmd'),
                InlineKeyboardButton('Close ✗', callback_data="close_data"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(Script.GROUP_START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), disable_web_page_preview=True, reply_markup=reply_markup)
        await asyncio.sleep(2) # 😢 https://github.com/EvamariaTG/EvaMaria/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, Script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, Script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton('❔ HOW TO USE THIS BOT', callback_data='cbguide')
            ],[
            InlineKeyboardButton('📚 Commands', callback_data='dkcmd'),
            InlineKeyboardButton('🌐 Terms & Condition', callback_data='cdinfo')
            ],[
            InlineKeyboardButton('❤️ Donate', url=f'https://t.me/{OWNER_NAME}')
            ],[
            InlineKeyboardButton('📣 Official Channel', url='https://t.me/DKBOTZNETWORK'),
            InlineKeyboardButton('✨ NEW Features', callback_data='cbfeature')
            ],[
            InlineKeyboardButton('✗ Close the Menu ✗', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=Script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            quote=True,
            parse_mode='html'
        )
        return
    if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        except ChatAdminRequired:
            logger.error("Make sure Bot is admin in Forcesub channel")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "Join Official Channel", url=invite_link.invite_link
                )
            ]
        ]

        if message.command[1] != "subscribe":
            btn.append([InlineKeyboardButton(" 🔄 Try Again 👈 Tap me 🥰", callback_data=f"checksub#{message.command[1]}")])
        await client.send_message(
            chat_id=message.from_user.id,
            text=Script.FORCESUB_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode="markdown"
            )
        return
    if len(message.command) ==2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
        buttons = [[
            InlineKeyboardButton('❔ HOW TO USE THIS BOT', callback_data='cbguide')
            ],[
            InlineKeyboardButton('📚 Commands', callback_data='dkcmd'),
            InlineKeyboardButton('🌐 Terms & Condition', callback_data='cdinfo')
            ],[
            InlineKeyboardButton('❤️ Donate', url=f'https://t.me/{OWNER_NAME}')
            ],[
            InlineKeyboardButton('📣 Official Channel', url='https://t.me/DKBOTZNETWORK'),
            InlineKeyboardButton('✨ NEW Features', callback_data='cbfeature')
            ],[
            InlineKeyboardButton('✗ Close the Menu ✗', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=Script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            quote=True,
            parse_mode='html'
        )


