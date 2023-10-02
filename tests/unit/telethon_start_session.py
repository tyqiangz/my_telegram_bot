from telethon import TelegramClient
from telethon.sessions import StringSession
import os

api_id = os.environ["api_id"]
api_hash = os.environ["api_hash"]
session_string = os.environ["session_string"]

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Session string:", client.session.save())