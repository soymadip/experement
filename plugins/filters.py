

import re
import pyrogram
import asyncio

from pyrogram import (
    filters,
    Client
)

from pyrogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    Message,
    CallbackQuery
)

from bot import Bot
from script import script
from config import MAINCHANNEL_ID, ADMINS, LOG_CHANNEL

BUTTONS = {}
 

@Client.on_message(filters.incoming & filters.text)
async def sfilter(client: Bot, message):
    await client.USER.reply_message(chat_id=message.message_id, text='π°π‘π’π§ππππ°\n\nDo not request hereπ‘\nThis chat is only for <u>movie delevery</u>.\n\n<b>Tell your query in CINEMA HUB groupππ»</b>')
