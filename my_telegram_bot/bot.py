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
from telegram.ext import ApplicationBuilder, ContextTypes, \
    CommandHandler
import boto3
import datetime
import pandas as pd
from bisect import bisect_left

BOT_TOKEN = os.environ["BOT_TOKEN"]
application = ApplicationBuilder().token(BOT_TOKEN).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    The bot will reply `"I'm a bot, please talk to me!"`
    when the message `"/start"` is received.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=_start())


async def leetcode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    The bot will reply the leetcode question of the day.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=_leetcode(),
                                   parse_mode='Markdown')


async def tbills(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    The bot will reply the recent T-Bills info
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=_tbills(),
                                   parse_mode='Markdown')


def _start() -> str:
    return "Hello, I'm your personal assistant 😊 How can I help you?"


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

    response = requests.post("https://leetcode.com/graphql",
                             headers=headers,
                             data=json.dumps(query),
                             timeout=10)
    data = json.loads(response.text)
    return data


def construct_leetcode_msg(title: str, date: str, link: str, difficulty: str):
    leetcode_base_url = "https://leetcode.com"

    assert link[0] == "/", "`link` should start with a '/' character"

    message = "👨‍💻*LC Daily Question*👩‍💻\n"
    message += f"*Date:* {date}\n"
    message += f"*Title:* {title}\n"
    message += f"*Difficulty:* {difficulty}\n"
    message += leetcode_base_url + link
    return message


def _leetcode() -> str:
    data = get_leetcode_daily_qn()
    question_data = data["data"]["activeDailyCodingChallengeQuestion"]

    date = question_data["date"]
    link = question_data["link"]
    title = question_data["question"]["title"]
    difficulty = question_data["question"]["difficulty"]

    message = construct_leetcode_msg(title=title,
                                     date=date,
                                     link=link,
                                     difficulty=difficulty)

    return message


def _tbills() -> str:
    filename = "my-telegram-bot/" + \
        "T-Bills Issuance Calendars/SGS Treasury Bills - T-BILLS 2023.csv"
    output_filename = 's3_download.csv'

    s3 = boto3.client('s3')
    s3.download_file(os.environ["S3_BUCKET_NAME"], filename, output_filename)

    df = pd.read_csv(output_filename,
                     parse_dates=[
                         "Announcement Date", "Auction Date", "Issue Date",
                         "Maturity Date"
                     ],
                     dayfirst=True)

    df = df[df["Tenor"] == "6-month"]
    last_tbill_idx = bisect_left(a=df["Auction Date"],
                                 x=datetime.datetime.now() +
                                 datetime.timedelta(hours=8))
    last_tbill_idx

    last_tbill = df.iloc[last_tbill_idx - 1, :]
    # next_tbill = df.iloc[last_tbill_idx, :]

    message = get_tbills_msg(
        announcement_date=last_tbill["Announcement Date"],
        auction_date=last_tbill["Auction Date"],
        issue_date=last_tbill["Issue Date"],
        maturity_date=last_tbill["Maturity Date"],
        issue_code=last_tbill["Issue Code"],
        isin_code=last_tbill["ISIN Code"],
    )

    message = "*Previous 6 mth T-Bills*\n\n" + message

    return message


def get_tbills_msg(announcement_date: datetime.datetime,
                   auction_date: datetime.datetime,
                   issue_date: datetime.datetime,
                   maturity_date: datetime.datetime, issue_code: str,
                   isin_code: str) -> str:

    website = "https://www.mas.gov.sg/bonds-and-bills" + \
        "/auctions-and-issuance-calendar/auction-t-bill?"
    website += f"issue_code={issue_code}"
    website += f"&issue_date={issue_date.strftime('%Y-%m-%d')}"

    message = "*Announcement Date:* " + announcement_date.strftime(
        "%Y/%m/%d") + "\n"
    message += "*Auction Date:* " + auction_date.strftime("%Y/%m/%d") + "\n"
    message += "*Issue Date:* " + issue_date.strftime("%Y/%m/%d") + "\n"
    message += "*Maturity  Date:* " + maturity_date.strftime("%Y/%m/%d") + "\n"
    message += "*issue_code:* " + issue_code + "\n"
    message += "*ISIN code:* " + isin_code + "\n"
    message += "*Website:* " + website

    return message


start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

leetcode_handler = CommandHandler('lc', leetcode)
application.add_handler(leetcode_handler)

tbills_handler = CommandHandler('tbills', tbills)
application.add_handler(tbills_handler)
