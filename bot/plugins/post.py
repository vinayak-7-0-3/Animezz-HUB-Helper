from bot import BOT_USERNAME, ADMINS, CHANNEL_ID, \
    ALLOW_BACKUP, BACKUP_CHANNEL, STORAGE_CHANNEL
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["post", f"post@{BOT_USERNAME}"]))
async def post_in_channel(bot, update):
    if update.from_user.id in ADMINS:
        try:
            links = update.text.split("\n")
            links.pop(0)    
        except:
            links = None
        msg = update.reply_to_message
        if msg and links:
            inline_keyboard = []
            for link in links:
                name = link.split(" | ")[0]
                url = link.split(" | ")[1]
                inline_keyboard.append([InlineKeyboardButton(name, url=url)])
            await bot.copy_message(
                chat_id=CHANNEL_ID,
                from_chat_id=msg.chat.id,
                message_id=msg.message_id,
                reply_markup=InlineKeyboardMarkup(inline_keyboard)
            )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            from_chat_id=msg.chat.id,
            message_id=msg.message_id
        ) 

@Client.on_message(filters.incoming)
async def backup_file(bot, update):
    if update.chat.id == STORAGE_CHANNEL and ALLOW_BACKUP:
        msg = update.message
        await bot.copy_message(
            chat_id=BACKUP_CHANNEL,
            from_chat_id=msg.chat.id,
            message_id=msg.message_id
        )
