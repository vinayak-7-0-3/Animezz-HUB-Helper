from pyrogram import Client, filters
from bot import BOT_USERNAME, app
from bot.helpers.imdb_api import reqLinkID, get_info_from_id
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

imdb_link_prefix = "https://www.imdb.com/title/"

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
                inline_keyboard.append([InlineKeyboardButton(text=name,callback_data=id)])
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

@app.on_callback_query()
async def req_movie_cb(c: Client, cb: CallbackQuery):
    if cb.data == "close":
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
    else:
        link = imdb_link_prefix + str(cb.data)
        msg, photo = await get_info_from_id(link)
        if msg:
            await c.delete_messages(
                chat_id=cb.message.chat.id,
                message_ids=cb.message.message_id
            )
            await c.send_photo(
                chat_id=cb.message.chat.id,
                photo=photo,
                caption=msg,
                reply_to_message_id=cb.message.reply_to_message.message_id
            )
        else:
            await c.edit_message_text(
                chat_id=cb.message.chat.id,
                message_id=cb.message.message_id,
                text="Sorry, Couldnt Find A Proper Source For This Movie 😥"
            )