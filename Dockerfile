FROM python:3.7

# Datos propios
LABEL maintainer="Antonio Jesús Heredia (a.heredia.castillo@@gmail.com)"

EXPOSE $PORT

COPY requirements.txt /tmp
RUN cd /tmp && pip install -r requirements.txt
RUN apt-get update && apt-get install rabbitmq-server -y
COPY . /app

WORKDIR /app
RUN python microservicio/receiver.py &

# Finalmente ejecutamos la app escuchando en el puerto definido en PORT
CMD gunicorn -b 0.0.0.0:${PORT} app:app
