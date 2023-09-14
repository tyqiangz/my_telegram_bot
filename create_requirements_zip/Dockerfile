FROM python:3.9-slim

# intended name of zip file containing all packages in `requirements.txt`,
# will be used in `bash.sh`
ENV LAMBDA_LAYER_FILENAME=python_telegram_bot.zip

# prevent creation of .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# ignore warnings about installing packages as root user
ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update
RUN apt-get install zip -y
RUN apt-get -y install python3-pip
RUN pip install --upgrade pip
WORKDIR /src
COPY ./requirements.txt requirements.txt

CMD ["bash", "script.sh"]