from pathlib import Path
import sys
 
# directory reach
directory = Path(__file__).absolute().parent.parent.parent / "src"
 
# setting path
sys.path.append(directory)

print(directory)

from src.bot import application
from telegram import Update
import json

def test_echo(body):
    update_body = Update.de_json(json.loads(body), application.bot)

    return update_body

body = {}
print(test_echo(body))