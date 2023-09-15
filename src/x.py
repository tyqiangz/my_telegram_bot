import json
import os
from telegram.ext import Dispatcher, MessageHandler, Filters
from telegram import Update, Bot
import logging

os.environ["BOT_TOKEN"] = 

bot = Bot(token=os.environ["BOT_TOKEN"])
dispatcher = Dispatcher(bot, None, use_context=True)

def echo(update, context):
    
    chat_id = update.message.chat_id
    chat_user = update.message.from_user
    chat_text = update.message.text
    
    context.bot.send_message(chat_id=chat_id, text= "Message from " + str(chat_user.first_name) + ": \n " + chat_text)

def lambda_handler(event, context):
    
    # a function `echo` will be returned if a text is received.
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
   
    try:
        dispatcher.process_update(
            Update.de_json(json.loads(event["body"]), bot)
        )

    except Exception as e:
        print(e)
        logging.warning(e)
        return {"statusCode": 500}

    return {"statusCode": 200}
