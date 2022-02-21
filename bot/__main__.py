from pyrogram import Client
from bot import LOGGER, API_ID, API_HASH, BOT_TOKEN, STRING_SESSION


plugins = dict(
    root="bot/modules"
)

user = Client(
    session_name=STRING_SESSION,
    api_id=API_ID,
    api_hash=API_HASH)

class Bot(Client):
    def __init__(self):
        super().__init__(
            "TidalDLBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=plugins
        )

    async def start(self):
        await super().start()
        await user.start()
        LOGGER.info("Bot Started...... Now Enjoy")

    async def stop(self, *args):
        await super().stop()
        LOGGER.info('Exiting User........')
        await user.stop()
        LOGGER.info('Bot Stopped ! Bye..........')

if __name__ == "__main__":
    app = Bot()
    app.run()