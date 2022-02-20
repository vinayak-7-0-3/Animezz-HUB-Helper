# myanilist api
from jikanpy import Jikan
from pyrogram import Client, filters
from bot import BOT_USERNAME

animelist = Jikan()

@Client.on_message(filters.command(["anime", f"anime@{BOT_USERNAME}"]))
async def anime_mal(bot, update):
    try:
        name = update.text.split(" ", maxsplit=1)[1]
    except:
        name = None
    if name:
        pass


