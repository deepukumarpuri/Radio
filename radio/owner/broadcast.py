import os
import shutil
import sys
import traceback
from functools import wraps
from os import environ, execle
import psutil
from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_ID,
)
from radio.song import get_text, humanbytes
from radio.database import db
from radio.dbtools import main_broadcast_handler
from radio.decorators import sudo_users_only
from radio.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message
        
@Client.on_message(
    filters.private
    & filters.command("broadcast")
    & filters.user(OWNER_ID)
    & filters.reply
)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)

@Client.on_message(command("status"))
@sudo_users_only
async def botstats(_, message: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    total_users = await db.total_users_count()
    await message.reply_text(
        text=f"**📊 stats of @{BOT_USERNAME}** \n\n**🤖 bot version:** `2.0` \n\n**🙎🏼 total users:** \n » **on bot pm:** `{total_users}` \n\n**💾 disk usage:** \n » **disk space:** `{total}` \n » **used:** `{used}({disk_usage}%)` \n » **free:** `{free}` \n\n**🎛 hardware usage:** \n » **CPU usage:** `{cpu_usage}%` \n » **RAM usage:** `{ram_usage}%`",
        parse_mode="Markdown",
        quote=True,
    )
