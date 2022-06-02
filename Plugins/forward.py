import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config 

@channelforward.on_message(filters.channel)
async def forward(c, m):
    # Forwarding the messages to the channel

    for id in Config.CHANNEL:
       from_channel, to_channel = -1001779474259 , -1001513827997
       if m.chat.id == from_channel):
          await m.forward(to_channel, as_copy=True)
          print("Forwarded a message from", from_channel, "to", to_channel)
          asyncio.sleep(1)
