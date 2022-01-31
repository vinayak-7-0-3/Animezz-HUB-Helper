from pyrogram import Client
from bot import LOGGER, INLINE_THUMB
from bot.helpers.imdb import get_info
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent, InlineQueryResultAudio, InlineQueryResultPhoto

@Client.on_inline_query()
async def inline_search(_, event: InlineQuery):
    answers = list()
    msg = None
    links = None
    if event.query == "" or not event.query.startswith(("-m", "-imdb", "-s")):
        answers.append(
            InlineQueryResultArticle(
                title="Use the flags to get the results",
                input_message_content=InputTextMessageContent(
                    message_text="Use the flags to get the results"
                ),
                thumb_url=INLINE_THUMB,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Search",
                                switch_inline_query_current_chat=""
                            )
                        ]
                    ]
                )
            )
        )
    else:
        query = event.query
        if query.startswith("-m "):
            query = query[3:]
        elif query.startswith("-imdb "):
            query = query[6:]
            msg, title, photo = await get_info(query)
            if not photo == "None":
                for name in title:
                    answers.append(
                        InlineQueryResultPhoto(
                            photo_url=photo[title.index(name)],
                            title=name,
                            caption=msg[title.index(name)],
                            description=msg[title.index(name)]
                        )
                    )
        elif query.startswith("-s "):
            query = query[3:]
        else:
            msg = None

    try:
        await event.answer(
            results=answers,
            cache_time=0
        )
    except QueryIdInvalid:
        LOGGER.info(f"QueryIdInvalid: {event.query}")