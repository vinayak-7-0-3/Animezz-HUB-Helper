import logging
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
STRING_SESSION = getenv("STRING_SESSION")

BOT_USERNAME = getenv("BOT_USERNAME")
if BOT_USERNAME.startswith("@"):
        BOT_USERNAME = BOT_USERNAME[1:]

CHANNEL_ID = int(getenv("CHANNEL_ID"))
ADMINS = set(int(x) for x in getenv("ADMINS", "").split())
BACKUP_CHANNEL = int(getenv("BACKUP_CHANNEL", -100))
STORAGE_CHANNEL = int(getenv("STORAGE_CHANNEL", -100))
ALLOW_BACKUP = bool(int(getenv("ALLOW_BACKUP", 0)))

FOOTER = getenv("FOOTER")
INLINE_THUMB = getenv("INLINE_THUMB", False)

DOWNLOAD_DIR = getenv("DOWNLOAD_DIR", "./downloads")
