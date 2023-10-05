# run this file to get a telegram bot running.

from src.bot import application
from telegram import Update


application.run_polling(allowed_updates=Update.ALL_TYPES)