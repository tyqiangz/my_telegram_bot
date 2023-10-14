# My Telegram Bot

A telegram bot that gives me information I require about things that I care about, e.g. weather, food recommendations.

The telegram bot is deployed on AWS Lambda using the [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/) CLI tool.

Learn how to use AWS SAM here: https://catalog.workshops.aws/complete-aws-sam/en-US.
Documentation: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html

## Setup
1. Create a telegram bot on Telegram by messaging BotFather at https://t.me/BotFather or @BotFather.
2. Note down the bot token that BotFather sends, it should be of the form `1234567890:qlwejlkmfsldfk-12klsd`
3. Verify that you can see the bot's info on this URL: `https://api.telegram.org/bot{BOT_TOKEN}/getMe`
E.g. `https://api.telegram.org/bot1234567890:qlwejlkmfsldfk-12klsd/getMe`
4. Create AWS Lambda function, note down the function url.
5. Copy the python files `main.py` and include a zip file containing all the required python libraries in `requirement.txt` in AWS Lambda layer.
6. Set webhook for the bot as the AWS Lambda function url, `https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={AWS_LAMBDA_FUNCTION_URL}`, e.g.
`https://api.telegram.org/bot1234567890:qlwejlkmfsldfk-12klsd/setWebhook?url=https://aklhdaklsnalskdmla.lambda-url.us-east-1.on.aws/`

Initial template of the lambda function for the bot is taken from: https://github.com/jojo786/Sample-Python-Telegram-Bot-AWS-Serverless-PTBv20/

There are two main libraries for developing telegram bots `python-telegram-bot` (https://github.com/python-telegram-bot/python-telegram-bot) and `pyTelegramBotAPI`(https://github.com/eternnoir/pyTelegramBotAPI). The library `python-telegram-bot` is chosen because the logical operations on the messages are a lot more comprehensive (check out Filters in `python-telegram-bot`). 

TODO:
- [x] Add unit tests to `./tests` to test the telegram bot.
- [x] Setup GitHub Actions to run all unit tests when code is pushed onto repo.
- [ ] Add integration tests to `./events/events.json` to test the lambda function.
- [ ] Add cronjob to bot such that Leetcode question of the day will be sent at GMT+0 everyday.
- [ ] Add cronjob to bot such that Monetary Authority of Singapore (MAS)'s T-Bills details will be sent when an auction closes.