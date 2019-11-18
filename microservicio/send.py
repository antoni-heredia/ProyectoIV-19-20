#!/usr/bin/env python
import pika
from flask import jsonify

def encolar(imagen, nombre):
    if not 'HEROKU' in os.environ:
        logging.basicConfig()
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    else:
        url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)    channel = connection.channel()

    channel.queue_declare(queue='colaImagenes')
    channel.basic_publish(exchange='', routing_key='colaImagenes', body=nombre+":"+imagen)

    connection.close()