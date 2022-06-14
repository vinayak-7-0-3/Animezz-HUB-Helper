from bot import BOT_USERNAME, ADMINS, CHANNEL_ID, \
    ALLOW_BACKUP, BACKUP_CHANNEL, LOGGER, STORAGE_CHANNEL
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
        await bot.copy_message(
            chat_id=BACKUP_CHANNEL,
            from_chat_id=update.chat.id,
            message_id=update.message_id
        )


@Client.on_message(filters.command(["p2c", f"p2c@{BOT_USERNAME}"]))
async def post_to_channel(bot, update):
    LOGGER.info(f"{update.from_user.first_name} {update.from_user.last_name} {update.from_user.username}")
    if update.from_user.id in ADMINS:
        if update.reply_to_message:
            try:
                c_id = update.text.split(" ")[1]
                try:
                    buttons = update.text.split("\n")
                    buttons.pop(0)
                    if buttons:
                        inline_keyboard = []
                        for button in buttons:
                            name = button.split(" | ")[0]
                            url = button.split(" | ")[1]
                            inline_keyboard.append([InlineKeyboardButton(name, url=url)])
                except:
                    inline_keyboard = None
            except:
                c_id = None
            if c_id and buttons:    
                await bot.copy_message(
                    chat_id=c_id,
                    from_chat_id=update.chat.id,
                    message_id=update.reply_to_message.message_id,
                    reply_markup=InlineKeyboardMarkup(inline_keyboard)
                )
            else:
                await bot.copy_message(
                    chat_id=c_id,
                    from_chat_id=update.chat.id,
                    message_id=update.reply_to_message.message_id
                )
        else:
            await bot.send_message(
                chat_id=update.chat.id,
                text="Please reply to a message to copy it to a channel"
            )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text="You are not allowed to use this command"
        )