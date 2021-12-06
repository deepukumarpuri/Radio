from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from configs import Config
import time
import string
import shutil
import psutil
import random
import math
from database.access_db import db
from database.add_user import AddUserToDatabase
from radio.broadcast import broadcast_handler
from pyrogram.errors import FloodWait, UserNotParticipant, MessageNotModified


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2 ** 10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'
    
@Client.on_message(filters.private & filters.command("broadcasts") & filters.reply & filters.user(Config.OWNER_ID) & ~filters.edited)
async def _broadcast(_, m: Message):
    await broadcast_handler(m)


@Client.on_message(filters.private & filters.command("status") & filters.user(Config.OWNER_ID)
async def _status(bot, update):
  total, used, free = shutil.disk_usage(".")
  total = humanbytes(total)
  used = humanbytes(used)
  free = humanbytes(free)
  cpu_usage = psutil.cpu_percent()
  ram_usage = psutil.virtual_memory().percent
  disk_usage = psutil.disk_usage('/').percent
  total_users = await db.total_users_count()
  await update.reply_text(
    text=f"""
**Total Disk Space: {total}
Used Space: {used}({disk_usage}%)
Free Space: {free} 
CPU Usage: {cpu_usage}% 
RAM Usage: {ram_usage}%

Total Users in DB: {total_users}**""",
    disable_web_page_preview=True,
    reply_markup=STAT_BUTTONS
  )

@Client.on_message(filters.private & filters.command("check") & filters.user(Config.OWNER_ID))
async def check_handler(bot: Client, m: Message):
    if len(m.command) == 2:
        editable = await m.reply_text(
            text="**Checking User Details...**"
        )
        user = await bot.get_users(user_ids=int(m.command[1]))
        detail_text = f"**Name:** [{user.first_name}](tg://user?id={str(user.id)})\n" \
                      f"**Username:** `{user.username}`\n" \
                      f"**Upload as Doc:** `{await db.get_upload_as_doc(id=int(m.command[1]))}`\n" \
                      f"**Generate Screenshots:** `{await db.get_generate_ss(id=int(m.command[1]))}`\n"
        await editable.edit(
            text=detail_text,
            parse_mode="Markdown",
            disable_web_page_preview=True
        )

@Client.on_message(filters.private & filters.command("ban_user") & filters.user(Config.OWNER_ID))
async def ban(c: Client, m: Message):
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to ban any user from the bot.\n\nUsage:\n\n`/ban_user user_id ban_duration ban_reason`\n\nEg: `/ban_user 1234567 28 You misused me.`\n This will ban user with id `1234567` for `28` days for the reason `You misused me`.",
            quote=True
        )
        return
    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = ' '.join(m.command[3:])
        ban_log_text = f"Banning user {user_id} for {ban_duration} days for the reason {ban_reason}."
        try:
            await c.send_message(
                user_id,
                f"You are banned to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n**Message from the admin**"
            )
            ban_log_text += '\n\nUser notified successfully!'
        except:
            traceback.print_exc()
            ban_log_text += f"\n\nUser notification failed! \n\n`{traceback.format_exc()}`"
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(
            ban_log_text,
            quote=True
        )
    except:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
       ) 
        
@Client.on_message(filters.private & filters.command("unban_user") & filters.user(Config.OWNER_ID))
async def unban(c: Client, m: Message):
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to unban any user.\n\nUsage:\n\n`/unban_user user_id`\n\nEg: `/unban_user 1234567`\n This will unban user with id `1234567`.",
            quote=True
        )
        return
    try:
        user_id = int(m.command[1])
        unban_log_text = f"Unbanning user {user_id}"
        try:
            await c.send_message(
                user_id,
                f"Your ban was lifted!"
            )
            unban_log_text += '\n\nUser notified successfully!'
        except:
            traceback.print_exc()
            unban_log_text += f"\n\nUser notification failed! \n\n`{traceback.format_exc()}`"
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(
            unban_log_text,
            quote=True
        )
    except:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )


@Client.on_message(filters.private & filters.command("banned_users") & filters.user(Config.OWNER_ID))
async def _banned_usrs(_, m: Message):
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ''
    async for banned_user in all_banned_users:
        user_id = banned_user['id']
        ban_duration = banned_user['ban_status']['ban_duration']
        banned_on = banned_user['ban_status']['banned_on']
        ban_reason = banned_user['ban_status']['ban_reason']
        banned_usr_count += 1
        text += f"> **user_id**: `{user_id}`, **Ban Duration**: `{ban_duration}`, **Banned on**: `{banned_on}`, **Reason**: `{ban_reason}`\n\n"
    reply_text = f"Total banned user(s): `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open('banned-users.txt', 'w') as f:
            f.write(reply_text)
        await m.reply_document('banned-users.txt', True)
        os.remove('banned-users.txt')
        return
    await m.reply_text(reply_text, True)

