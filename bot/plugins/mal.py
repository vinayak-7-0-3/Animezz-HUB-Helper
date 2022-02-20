# myanilist api
from pyrogram import Client, filters
from bot import BOT_USERNAME
from bot.helpers.mal_api import get_anime_list
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["anime", f"anime@{BOT_USERNAME}"]))
async def anime_mal(bot, update):
    try:
        name = update.text.split(" ", maxsplit=1)[1]
    except:
        name = None
    if name:
        titles, id_list = get_anime_list(name)
        if titles:
            inline_keyboard = []
            for id in id_list:
                name = titles[id_list.index(id)]
                inline_keyboard.append([InlineKeyboardButton(text=name,callback_data=id)])
            inline_keyboard.append([InlineKeyboardButton(text="Close",callback_data="close")])
            await bot.send_message(
                    chat_id=update.chat.id,
                    text="Select the anime",
                    reply_markup=InlineKeyboardMarkup(inline_keyboard),
                    reply_to_message_id=update.message_id
                )

