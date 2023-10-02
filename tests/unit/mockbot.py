from pathlib import Path
import sys
from telegram import Update

# directory reach
directory = Path(__file__).absolute().parent.parent.parent / "src"

# setting path
sys.path.insert(0, str(directory))

from bot import application

application.run_polling(allowed_updates=Update.ALL_TYPES)