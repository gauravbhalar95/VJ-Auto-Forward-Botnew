# Ask Doubt on telegram @KingVJ01

import logging
logger = logging.getLogger(__name__)

from pyrogram import filters
from bot import channelforward
from config import Config
from translation import Translation

################################################################################################################################################################################################################################################
# start command

@channelforward.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    await message.reply(
        text=Translation.START,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# about command

@channelforward.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    await message.reply(
        text=Translation.ABOUT,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# addchannel command

@channelforward.on_message(filters.command("addchannel") & filters.private & filters.incoming)
async def add_channel(client, message):
    if len(message.command) < 3:
        await message.reply("Usage: /addchannel <pickup_channel_id> <target_channel_id>")
        return
    pickup, target = message.command[1], message.command[2]
    channel_mappings[pickup] = target
    await message.reply(f"Added mapping: {pickup} → {target}")

################################################################################################################################################################################################################################################
# removechannel command

@channelforward.on_message(filters.command("removechannel") & filters.private & filters.incoming)
async def remove_channel(client, message):
    if len(message.command) < 2:
        await message.reply("Usage: /removechannel <pickup_channel_id>")
        return
    pickup = message.command[1]
    if pickup in channel_mappings:
        del channel_mappings[pickup]
        await message.reply(f"Removed mapping for {pickup}")
    else:
        await message.reply("Channel not found in mappings.")
