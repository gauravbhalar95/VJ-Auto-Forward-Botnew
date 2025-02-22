# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
import uvloop
from pyrogram import Client, filters
from config import Config

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(lineno)d - %(module)s - %(levelname)s - %(message)s'
)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

uvloop.install()

# Dictionary to store channel mappings
channel_mappings = {}

class channelforward(Client, Config):
    def __init__(self):
        super().__init__(
            name="CHANNELFORWARD",
            bot_token=self.BOT_TOKEN,
            api_id=self.API_ID,
            api_hash=self.API_HASH,
            workers=20,
            plugins={'root': 'Plugins'}
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"New session started for {me.first_name}({me.username})")

    async def stop(self):
        await super().stop()
        print("Session stopped. Bye!!")

    async def forward_messages(self, client, message):
        pickup_id = str(message.chat.id)
        if pickup_id in channel_mappings:
            target_id = int(channel_mappings[pickup_id])
            await message.copy(target_id)
            logging.info(f"Forwarded message from {pickup_id} to {target_id}")

    async def add_channel(self, client, message):
        if len(message.command) < 3:
            await message.reply("Usage: /addchannel <pickup_channel_id> <target_channel_id>")
            return
        pickup, target = message.command[1], message.command[2]
        channel_mappings[pickup] = target
        await message.reply(f"Added mapping: {pickup} → {target}")

    async def remove_channel(self, client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /removechannel <pickup_channel_id>")
            return
        pickup = message.command[1]
        if pickup in channel_mappings:
            del channel_mappings[pickup]
            await message.reply(f"Removed mapping for {pickup}")
        else:
            await message.reply("Channel not found in mappings.")

if __name__ == "__main__":
    app = channelforward()
    app.add_handler(filters.command("addchannel")(app.add_channel))
    app.add_handler(filters.command("removechannel")(app.remove_channel))
    app.add_handler(filters.channel(app.forward_messages))
    app.run()
