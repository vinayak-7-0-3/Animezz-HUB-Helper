from pyrogram import Client
from bot import LOGGER, API_ID, API_HASH, BOT_TOKEN, STRING_SESSION
from bot.plugins import tracemoe_handler

plugins = dict(
    root="bot/plugins"
)

"""user = Client(
    session_name=STRING_SESSION,
    api_id=API_ID,
    api_hash=API_HASH)"""

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bott",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=plugins
        )

    async def start(self):
        await super().start()
        #await user.start()
        LOGGER.info(
            """
|====================================================|
|                                                    |
|               Bot Started Successfully             |
|                    AnimezzHUB Bot                  |
|                        v1.0.0                      |
|                                                    |
|====================================================|
""")

    async def stop(self, *args):
        await super().stop()
        LOGGER.info('Exiting User........')
        #await user.stop()
        LOGGER.info('Bot Stopped ! Bye..........')

if __name__ == "__main__":
    app = Bot()
    app.run()
