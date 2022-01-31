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
#STRING_SESSION = getenv("STRING_SESSION")
BOT_USERNAME = getenv("BOT_USERNAME")
if BOT_USERNAME.startswith("@"):
        BOT_USERNAME = BOT_USERNAME[1:]

# Logging Group where RSS bot dumps
#GROUP_ID = int(getenv("GROUP_ID"))
#CHANNEL_ID = int(getenv("CHANNEL_ID"))

# Both URLS (not the username)
SUPPORT_GROUP = getenv("SUPPORT_GROUP")
FOOTER = getenv("FOOTER")

#MSG_TIMEOUT = int(getenv("MSG_TIMEOUT"))

#DATABASE_URL = getenv("DATABASE_URL")
#DATABASE_NAME = getenv("DATABASE_NAME")

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
