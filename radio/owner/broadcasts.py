from pyrogram import Client, filters
import datetime
import time
from radio.database import db
from config import ADMINS
from utils import broadcast_messages
import asyncio
        
@Client.on_message(filters.command("broadcasting") & filters.user(ADMINS) & filters.reply)
# https://t.me/JosProjects
async def verupikkals(bot, message):
    chats = await db.get_all_chats()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Broadcasting your messages...'
    )
    start_time = time.time()
    total_chats = await db.total_chat_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0

    success = 0
    async for user in chats:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Bocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"Broadcast in progress:\n\nTotal Users {total_chats}\nCompleted: {done} / {total_chats}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Broadcast Completed:\nCompleted in {time_taken} seconds.\n\nTotal Users {total_chats}\nCompleted: {done} / {total_chats}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")
