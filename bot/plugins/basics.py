from bot import BOT_USERNAME
from pyrogram import Client, filters

@Client.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Hi Sir!",
        reply_to_message_id=update.message_id
    )
