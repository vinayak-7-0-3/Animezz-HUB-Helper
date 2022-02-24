import ffmpeg
from pyrogram import Client, filters
from bot import BOT_USERNAME, DOWNLOAD_DIR

@Client.on_message(filters.command(["getvidinfo", f"getvidinfo@{BOT_USERNAME}"]))
async def fetch_tg_vid_info(bot, update):
    try:
        vid_file = update.reply_to_message
    except:
        vid_file = None
    if vid_file:
        file_path = f"{DOWNLOAD_DIR}/{update.reply_to_message.message_id}/"
        init_msg = await bot.send_message(
            chat_id=update.chat.id,
            text="Downloading Video...",
            reply_to_message_id=update.message_id
        )
        dl_path = await bot.download_media(
            message=update.reply_to_message,
            file_name=file_path
        )
        if dl_path:
            await bot.edit_message_text(
                chat_id=update.chat.id,
                message_id=init_msg.message_id,
                text="Processing..."
            )
            vid_info = await ffmpeg.probe(dl_path)["streams"]
            print(vid_info)
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text="Reply to a video to get info about it",
            reply_to_message_id=update.message_id
        )

