from pyrogram import Client, filters

@Client.on_message(filters.command(["getvidinfo"]))
async def fetch_tg_vid_info(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Reply to a video to get info about it",
        reply_to_message_id=update.message_id
    )
    
