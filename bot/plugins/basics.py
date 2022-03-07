from bot import BOT_USERNAME, DOWNLOAD_DIR 
from pyrogram import Client, filters
from pyrogram.types import  CallbackQuery
from bot.helpers.tracemoe_api import tracemoe_trace

@Client.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Hi Sir!",
        reply_to_message_id=update.message_id
    )

@Client.on_callback_query(filters.regex("close"))
async def close_menu(c: Client, cb: CallbackQuery):
    await c.delete_messages(
        chat_id=cb.message.chat.id,
        message_ids=cb.message.message_id
    )
    try:
        await c.delete_messages(
            chat_id=cb.message.chat.id,
            message_ids=cb.message.reply_to_message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["check_anime", f"check_anime@{BOT_USERNAME}"]))
async def check_anime(bot, update):
    if update.reply_to_message:
        init_msg = await bot.send_message(
            chat_id=update.chat.id,
            text="Downloading .......",
            reply_to_message_id=update.message_id
        )
        file_path = await bot.download_media(
            message=update.reply_to_message,
            file_name=DOWNLOAD_DIR + "/"
        )
        await bot.edit_message_text(
            chat_id=update.chat.id,
            message_id=init_msg.message_id,
            text="Scanning........Uwu........"
        )
        msg, video_link = await tracemoe_trace(file_path)
        await bot.edit_message_text(
            chat_id=update.chat.id,
            message_id=init_msg.message_id,
            text=msg
        )
        if video_link:
            await bot.send_video(
                chat_id=update.chat.id,
                video=video_link,
                reply_to_message_id=update.message_id
            )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text="Reply to trace",
            reply_to_message_id=update.message_id
        )
