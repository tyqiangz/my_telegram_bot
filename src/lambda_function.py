import os
import json
import asyncio
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

BOT_TOKEN = os.environ["BOT_TOKEN"]
application = ApplicationBuilder().token(BOT_TOKEN).build()

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    return asyncio.get_event_loop().run_until_complete(main(event, context))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    The bot will reply `"I'm a bot, please talk to me!"` when the message `"/start"` is received.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text="")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    The bot will reply whatever message that was send to it.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def main(event, context):
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    
    try:    
        await application.initialize()
        await application.process_update(
            Update.de_json(json.loads(event["body"]), application.bot)
        )
    
        return {
            'statusCode': 200,
            'body': 'Success'
        }

    except Exception as e:
        logging.warning(e)
        logging.warning(event)
        logging.warning(context)
        
        return {
            'statusCode': 500,
            'body': 'Failure'
        }