"""Run this file to get a telegram bot running."""

from telegram import Update
from ...src.bot import application

application.run_polling(allowed_updates=Update.ALL_TYPES)
