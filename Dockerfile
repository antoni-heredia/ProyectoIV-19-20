FROM python:3.7

# Datos propios
LABEL maintainer="Antonio Jesús Heredia (a.heredia.castillo@gmail.com)"

EXPOSE $PORT

COPY requirements.txt /tmp
RUN cd /tmp && pip install -r requirements.txt
RUN apt-get update && apt-get install rabbitmq-server -y
COPY . /app

WORKDIR /app


CMD rabbitmq-server &  ( sleep 5 &&  python microservicio/recieve.py  ) & gunicorn -b 0.0.0.0:${PORT} app:app
