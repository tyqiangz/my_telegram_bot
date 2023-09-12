# My Telegram Bot

A telegram bot that gives me information I require about things that I care about, e.g. weather, food recommendations.

The telegram bot is deployed on AWS Lambda.

## Setup
1. Create a telegram bot on Telegram by messaging BotFather at https://t.me/BotFather or @BotFather.
2. Note down the bot token that BotFather sends, it should be of the form `1234567890:qlwejlkmfsldfk-12klsd`
3. Verify that you can see the bot's info on this URL: `https://api.telegram.org/bot{BOT_TOKEN}/getMe`
E.g. `https://api.telegram.org/bot1234567890:qlwejlkmfsldfk-12klsd/getMe`
4. Create AWS Lambda function, note down the function url.
5. Copy the python files `main.py` and include a zip file containing all the required python libraries in `requirement.txt` in AWS Lambda layer.
6. Set webhook for the bot as the AWS Lambda function url, `https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={AWS_LAMBDA_FUNCTION_URL}`, e.g.
`https://api.telegram.org/bot1234567890:qlwejlkmfsldfk-12klsd/setWebhook?url= https://aklhdaklsnalskdmla.lambda-url.us-east-1.on.aws/`