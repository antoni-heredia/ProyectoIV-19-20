#!/usr/bin/env python
import pika,os,urlparse
import Imagenes as img
import find_wally_pretty as fw
import base64
import os
from PIL import Image
from io import BytesIO

if not 'HEROKU' in os.environ:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

else:
    url_str = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost//')
    url = urlparse.urlparse(url_str)
    params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],
    credentials=pika.PlainCredentials(url.username, url.password))
    connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='colaImagenes')



def callback(ch, method, properties, body):
    db = img.Imagenes()
    db.conectarMongo()

    imagen = body.decode().split(":")[1]
    nombre = body.decode().split(":")[0]

    imagen = base64.b64decode(imagen)

    imagen = fw.buscarWally(imagen)

    pil_img = Image.fromarray(imagen)
    buff = BytesIO()
    pil_img.save(buff, format="JPEG")
    new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")

    db.guardarImagenString(new_image_string,nombre)


channel.basic_consume(queue='colaImagenes', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()