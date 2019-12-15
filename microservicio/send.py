#!/usr/bin/env python
import pika
from flask import jsonify
import os
def encolar(imagen, nombre):
    if not 'HEROKU' in os.environ:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    else:
        print("encolado")
        url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue='colaImagenes')
    channel.basic_publish(exchange='', routing_key='colaImagenes', body=nombre+":"+imagen)

    connection.close()