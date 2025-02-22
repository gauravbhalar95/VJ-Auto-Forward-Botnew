import logging
from pyrogram import Client, filters
from config import Config

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize bot
bot = Client("AutoForwardBot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

@bot.on_message(filters.channel)
async def forward_messages(client, message):
    try:
        pickup_id = str(message.chat.id)
        for mapping in Config.CHANNEL:
            from_channel, to_channel = mapping.split(":")
            if pickup_id == from_channel:
                func = message.copy if Config.AS_COPY else message.forward
                await func(int(to_channel))
                logger.info(f"Forwarded message from {from_channel} to {to_channel}")
    except Exception as e:
        logger.exception(f"Error forwarding message: {e}")
