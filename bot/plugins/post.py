from pyrogram import Client, filters
from bot import BOT_USERNAME, CHANNEL_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["post", f"post@{BOT_USERNAME}"]))
async def post_to_channel(bot, update):
    try:
        links = update.text.split("\n")
    except:
        links = None
    msg = update.reply_to_message
    if msg and links:
        inline_keyboard = []
        inline_keyboard.append([InlineKeyboardButton(text="Direct Download",url=links[1])])
        inline_keyboard.append([InlineKeyboardButton(text="TG File",url=links[2])])
        await bot.copy_message(
            chat_id=CHANNEL_ID,
            from_chat_id=msg.chat.id,
            message_id=msg.message_id,
            reply_markup=InlineKeyboardMarkup(inline_keyboard)
        )
