from pyrogram import idle
from bot import app, LOGGER

LOGGER.info("Starting User & Bot") 
app.start()
#user.start()
idle() 
app.stop()
#LOGGER.info("User Stopped")
#user.stop()
#LOGGER.info("Bot Stopped")