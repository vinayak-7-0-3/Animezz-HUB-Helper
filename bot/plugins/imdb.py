from pyrogram import Client, filters
from bot import BOT_USERNAME
from bot.helpers.imdb_api import reqLinkID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command(["imdb", f"imdb@{BOT_USERNAME}"]))
async def imdb(bot, update):
    try:
        query = update.text.split(" ", maxsplit=1)[1]
    except:
        query = None
    if query:
        titles, id_list = await reqLinkID(query)
        if id_list:
            inline_keyboard = []
            for id in id_list:
                name = titles[id_list.index(id)]
                inline_keyboard.append([
                    inline_keyboard.append([InlineKeyboardButton(text=name,callback_data=id)])
                ])
            await bot.send_message(
                    chat_id=update.chat.id,
                    text="Select the movie you want to request",
                    reply_markup=InlineKeyboardMarkup(inline_keyboard),
                    reply_to_message_id=update.message_id
                )
        else:
            await bot.send_message(
                chat_id=update.chat.id,
                text="No movie found 🥺\nDont blame me 🥺",
                reply_to_message_id=update.message_id,
            )
    else:
        await bot.send_message(
                chat_id=update.chat.id,
                text="Please enter the movie title 😇",
                reply_to_message_id=update.message_id
            )