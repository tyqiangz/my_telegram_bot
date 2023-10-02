from pathlib import Path
import sys
import os
import asyncio
import telegram

# directory reach
directory = Path(__file__).absolute().parent.parent.parent / "src"
 
# setting path
sys.path.insert(0, str(directory))

async def main():
    bot = telegram.Bot(os.environ["BOT_TOKEN"])
    async with bot:
        response = bot.get_chat(chat_id=os.environ["CHAT_ID"])
        print(await response)

from telethon.sync import TelegramClient

with TelegramClient("my_account", os.environ["API_ID"], os.environ["API_HASH"]) as client:
    for message in client.iter_messages(chat):
        print(message.sender_id, ':', message.text)

asyncio.run(main())