"""
This script specifies all the telegram inputs that the chatbot 
would accept and give an output.

There should be a function of the form 
`func(update: Update, context: ContextTypes.DEFAULT_TYPE)`
that specifies how the telegram bot will react to the input.

A corresponding `_func` function will also exists that implements
the logic of the `func`.

Unit tests are written for all `_func` functions.
"""

import os
import json
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

BOT_TOKEN = os.environ["BOT_TOKEN"]
application = ApplicationBuilder().token(BOT_TOKEN).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    The bot will reply `"I'm a bot, please talk to me!"` when the message `"/start"` is received.
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=_start()
    )


async def leetcode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    The bot will reply the leetcode question of the day.
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=_leetcode()
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    The bot will reply whatever message that was sent to it.
    """
    response = _echo(update.message.text)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=response
    )


def _echo(msg: str) -> str:
    return msg


def _start() -> str:
    return "Hello, I'm your personal assistant <3 How can I help you?"


def get_leetcode_daily_qn():
    """
    Obtains the Leetcode question of the day from Leetcode's Graphql endpoint
    and returns the result as a json object.
    """
    query = {
        "query":
        """
            query questionOfToday { 
                activeDailyCodingChallengeQuestion { 
                    date
                    userStatus
                    link
                    question { 
                        acRate
                        difficulty
                        freqBar
                        frontendQuestionId: questionFrontendId
                        isFavor
                        paidOnly: isPaidOnly
                        status
                        title
                    }
                }
            }
        """
    }
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post(
        "https://leetcode.com/graphql",
        headers=headers,
        data=json.dumps(query),
        timeout=10
    )
    data = json.loads(response.text)
    return data


def _leetcode() -> str:
    leetcode_base_url = "https://leetcode.com"
    data = get_leetcode_daily_qn()
    date = data["data"]["activeDailyCodingChallengeQuestion"]["date"]
    link = data["data"]["activeDailyCodingChallengeQuestion"]["link"]
    title = data["data"]["activeDailyCodingChallengeQuestion"]["question"][
        "title"]

    return f"""Leetcode problem for the day ({date}) is {title}.\n{leetcode_base_url + link}"""


start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

leetcode_handler = CommandHandler('lc', leetcode)
application.add_handler(leetcode_handler)

echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
application.add_handler(echo_handler)
