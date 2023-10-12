"""
This scripts initialises the telegram bot specified in
`./bot.py` and sets up a AWS Lambda function containing
the telegram bot.
"""

import json
import asyncio
import logging
from telegram import Update
from .bot import application


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc:
        https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc:
        https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc:
        https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    return asyncio.get_event_loop().run_until_complete(main(event, context))


async def main(event, context):
    """
    Initialise the telegram bot and feed the AWS Lambda input to the bot.
    """
    try:
        await application.initialize()
        await application.process_update(
            Update.de_json(json.loads(event["body"]), application.bot))

        return {'statusCode': 200, 'body': 'Success'}

    except Exception as e:
        logging.warning(e)
        logging.warning(event)
        logging.warning(context)

        return {'statusCode': 500, 'body': 'Failure'}
