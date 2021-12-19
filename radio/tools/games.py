from pyrogram import Client, filters
@Client.on_message(filters.command(["football"]))
async def football(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='⚽️')

@Client.on_message(filters.command(["spin"]))
async def spin(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎰')

@Client.on_message(filters.command(["dice"]))
async def dice(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎲')

@Client.on_message(filters.command(["dart"]))
async def dart(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎯')

@Client.on_message(filters.command(["death"]))
async def death(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='⚰️')

@Client.on_message(filters.command(["roll"]))
async def roll(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎳')

@Client.on_message(filters.command(["cheers"]))
async def cheers(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🥂')

@Client.on_message(filters.command(["rip"]))
async def rip(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='⚰️')

@Client.on_message(filters.command(["thunder"]))
async def thunder(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='⚡')

@Client.on_message(filters.command(["happybirthday"]))
async def happybirthday(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎊')

@Client.on_message(filters.command(["vgame"]))
async def vgame(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎮')

@Client.on_message(filters.command(["peech"]))
async def peech(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🍑')

#GROUP COMMAND

@Client.on_message(filters.command(["football"]) & filters.group
)
async def football(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='⚽️')

@Client.on_message(filters.command(["spin"]) & filters.group
)
async def spin(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎰')

@Client.on_message(filters.command(["dice"]) & filters.group
)
async def dice(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎲')

@Client.on_message(filters.command(["dart"]) & filters.group
)
async def dart(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎯')

@Client.on_message(filters.command(["death"]) & filters.group
)
async def death(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='⚰️')

@Client.on_message(filters.command(["roll"]) & filters.group
)
async def roll(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎳')

@Client.on_message(filters.command(["cheers"]) & filters.group
)
async def cheers(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🥂')

@Client.on_message(filters.command(["rip"]) & filters.group
)
async def rip(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='⚰️')

@Client.on_message(filters.command(["thunder"]) & filters.group
)
async def thunder(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='⚡')

@Client.on_message(filters.command(["happybirthday"]) & filters.group
)
async def happybirthday(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎊')

@Client.on_message(filters.command(["vgame"]) & filters.group
)
async def vgame(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎮')

@Client.on_message(filters.command(["peech"]) & filters.group
)
async def peech(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🍑')

