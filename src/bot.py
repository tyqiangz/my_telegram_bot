import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

BOT_TOKEN = os.environ["BOT_TOKEN"]
application = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    The bot will reply `"I'm a bot, please talk to me!"` when the message `"/start"` is received.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text="hello, im your personal assistant <3")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    The bot will reply whatever message that was send to it.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
application.add_handler(echo_handler)