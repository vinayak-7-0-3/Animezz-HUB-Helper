import logging
import pyrogram
from os import getenv

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

# TG Things
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

BOT_USERNAME = getenv("BOT_USERNAME")
if BOT_USERNAME.startswith("@"):
        BOT_USERNAME = BOT_USERNAME[1:]

CHANNEL_ID = int(getenv("CHANNEL_ID"))
ADMINS = set(int(x) for x in getenv("ADMINS", "").split())

FOOTER = getenv("FOOTER")
INLINE_THUMB = getenv("INLINE_THUMB", False)

plugins = dict(
    root="bot/plugins"
)

app = pyrogram.Client(
    'Bott',
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins ) 

"""user = pyrogram.Client(
    session_name=STRING_SESSION,
    #bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH)"""
