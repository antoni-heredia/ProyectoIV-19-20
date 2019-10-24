
# content of test_expectation.py
import pytest
import mimetypes
import requests
import sys
from microservicio import manejoImagenes as db



@pytest.mark.parametrize("url", ["https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/f_auto,q_auto,w_1100/v1555285691/shape/mentalfloss/waldomain.png","https://miro.medium.com/max/1500/1*yO4EVVeBHYIrxKXDGY_-zw.jpeg"])
def test_imagen(url):
    response = requests.get(url, stream=True)
    assert response.headers['Content-Type'].split("/")[0] == "image"

@pytest.mark.parametrize("url", ["https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/f_auto,q_auto,w_1100/v1555285691/shape/mentalfloss/waldomain.png","https://miro.medium.com/max/1500/1*yO4EVVeBHYIrxKXDGY_-zw.jpeg"])
def test_guardarImagen(url):
    client = db.conectarMongo()
    response = requests.get(url, stream=True)
    db.guardarImagen(client,response.content,"Wally")

def test_eliminarTodasImagenes():
    client = db.conectarMongo()
    db.eliminarTodasImagenes(client)

def test_devolverUnaImagen():
    client = db.conectarMongo()
    imagen = db.devolverImagen(client,"Wally")
