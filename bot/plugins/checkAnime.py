from bot import BOT_USERNAME, DOWNLOAD_DIR 
from pyrogram import Client, filters
from pyrogram.types import  CallbackQuery
from bot.helpers.tracemoe_api import tracemoe_trace

@Client.on_message(filters.command(["check_anime", f"check_anime@{BOT_USERNAME}"]))
async def check_anime_handler(bot, update):
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
            text="Scanning........UwU........"
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
        try:
            link = update.text.split(" ", maxsplit=1)[1]
        except:
            link = None
            return await bot.send_message(
                chat_id=update.chat.id,
                text="Reply to trace",
                reply_to_message_id=update.message_id
            )
        init_msg = await bot.send_message(
            chat_id=update.chat.id,
            text="Scanning........UwU........"
        )
        msg, video_link = await tracemoe_trace(link=link)
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