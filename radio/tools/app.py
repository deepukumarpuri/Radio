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
from config import ADMINS, AUTH_CHANNEL, LOG_CHANNEL, PICS
from utils import get_size, is_subscribed, temp
import re
logger = logging.getLogger(__name__)

@Client.on_message(filters.command("started"))
async def start(client, message):
    if message.chat.type in ['group', 'supergroup']:
        buttons = [
            [
                InlineKeyboardButton('updates', url='https://t.me/josprojects')
            ],
            [
                InlineKeyboardButton('help', url=f"https://t.me/{temp.U_NAME}?start=help"),
                InlineKeyboardButton('Close ✗', callback_data="close_data"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(Script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), disable_web_page_preview=True, reply_markup=reply_markup)
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
            InlineKeyboardButton('Add me to your Chat', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('help', callback_data='help'),
            InlineKeyboardButton('about', callback_data='about')
            ],[
            InlineKeyboardButton('search here movie', switch_inline_query_current_chat='')
            ],[
            InlineKeyboardButton('updates', url='https://t.me/josprojects'),
            InlineKeyboardButton('movie club', url='https://t.me/+y53tWFUw6Q43NzE9')
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
            InlineKeyboardButton('Add me to your Chat', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('help', callback_data='help'),
            InlineKeyboardButton('about', callback_data='about')
            ],[
            InlineKeyboardButton('search here movie', switch_inline_query_current_chat='')
            ],[
            InlineKeyboardButton('updates', url='https://t.me/josprojects'),
            InlineKeyboardButton('movie club', url='https://t.me/+y53tWFUw6Q43NzE9')
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
