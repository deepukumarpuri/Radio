#!/usr/bin/env python3
# Copyright (C) @DKBOTZ
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random, os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_USERNAME


@Client.on_message(filters.command(["genpassword", f"genpassword@{BOT_USERNAME}, 'genpw', f"genpw@{BOT_USERNAME}"]))
async def password(bot, update):
    message = await update.reply_text(text="`Processing...`")
    password = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+".lower()
    try:
        limit = int(message.text)
    except:
        await message.edit_text('Limit is wrong \n\nExample :- `/genpassword 123`\n `/genpassword abcd`')
        return
    if limit > 100 or limit <= 0:
        text = "Sorry... Failed To Create Password, Because Limit is 1 to 100."
    else:
        random_value = "".join(random.sample(password, limit))
        text = f"**Limit :-** `{str(limit)}`.\n**Password :-** `{random_value}`**\n\nGenerate By @VC_RADI_PLAY_BOT",
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('Share The Bot', url='tg://msg?text=%2A%2AHai%20%E2%9D%A4%EF%B8%8F%2C%2A%2A%20%0A__Today%20i%20Just%20Found%20Out%20An%20Intresting%20And%20Powerful__%20%2A%2AVC%20Radio%20Play%20Bot%20With%20Many%20Features%2A%2A%20For%20Group%F0%9F%A5%B0.__%20%20%0A%2A%2ABot%20Link%20%3A%20%40VC_RADI_PLAY_BOT%2A%2A%20%F0%9F%94%A5')]])
    await message.edit_text(text, True)
