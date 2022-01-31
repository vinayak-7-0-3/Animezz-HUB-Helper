from pyrogram import Client, filters
from bot import BOT_USERNAME, CHANNEL_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["post", f"post@{BOT_USERNAME}"]))
async def post_to_channel(bot, update):
    msg = update.reply_to_message
    if msg:
        await bot.copy_message(
            chat_id=CHANNEL_ID,
            from_chat_id=msg.chat.id,
            message_id=msg.message_id
        )
