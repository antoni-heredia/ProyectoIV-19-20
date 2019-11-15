#!/usr/bin/env python
import pika
from flask import jsonify

def encolar(imagen, nombre):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='colaImagenes')
    channel.basic_publish(exchange='', routing_key='colaImagenes', body=nombre+":"+imagen)

    connection.close()