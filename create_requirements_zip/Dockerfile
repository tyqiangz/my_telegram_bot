FROM python:3.9-slim

RUN apt-get update
RUN apt-get install zip -y
RUN apt-get -y install python3-pip
RUN mkdir python
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt -t ./python
RUN rm -rf ./python/*.dist-info
RUN zip -r python_telegram_bot.zip ./python