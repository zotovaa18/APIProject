FROM python:3.8.2-slim-buster
WORKDIR /src
COPY . /src

RUN echo "Europe/Moscow" > /etc/timezone
RUN apt-get update
RUN apt-get -y install curl	
RUN apt-get -y install libpq-dev
RUN apt-get -y install gcc
RUN python3 -m pip install -r requirements.txt --no-cache-dir
