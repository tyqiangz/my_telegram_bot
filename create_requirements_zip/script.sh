pip install -r ./requirements.txt -t ./python
rm -rf ./python/*.dist-info
zip -r python_telegram_bot.zip ./python
rm -rf ./python