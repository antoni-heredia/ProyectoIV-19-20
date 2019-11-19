
# content of test_expectation.py
import pytest
import mimetypes
import requests
import sys
from microservicio import Imagenes as img


@pytest.mark.parametrize("url", ["https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/f_auto,q_auto,w_1100/v1555285691/shape/mentalfloss/waldomain.png","https://miro.medium.com/max/1500/1*yO4EVVeBHYIrxKXDGY_-zw.jpeg"])
def test_imagen(url):
    response = requests.get(url, stream=True)
    assert response.headers['Content-Type'].split("/")[0] == "image"

def test_eliminarTodasImagenes():
    db = img.Imagenes()
    db.conectarMongo()
    response = requests.get("https://miro.medium.com/max/1500/1*yO4EVVeBHYIrxKXDGY_-zw.jpeg", stream=True)
    db.guardarImagen(response.content,"Wally")      
    db.eliminarTodasImagenes()
    imagenes = db.devolverTodasImagenes()
    assert len(imagenes) == 0

def test_eliminarUnaImagen():
    db = img.Imagenes()
    db.conectarMongo()
    response = requests.get("https://miro.medium.com/max/1500/1*yO4EVVeBHYIrxKXDGY_-zw.jpeg", stream=True)
    db.guardarImagen(response.content,"Wally")  
    db.eliminarImagen("Wally")
    imagen = db.devolverImagen("Wally")
    assert len(imagen) == 0

def test_devolverUnaImagen():
    db = img.Imagenes()
    db.conectarMongo()
    response = requests.get("https://miro.medium.com/max/1500/1*yO4EVVeBHYIrxKXDGY_-zw.jpeg", stream=True)
    db.guardarImagen(response.content,"Wally")
    imagen = db.devolverImagen("Wally")
    assert len(imagen) != 0
    db.eliminarImagen("Wally")



@pytest.mark.parametrize("url", ["https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/f_auto,q_auto,w_1100/v1555285691/shape/mentalfloss/waldomain.png","https://miro.medium.com/max/1500/1*yO4EVVeBHYIrxKXDGY_-zw.jpeg"])
def test_guardarImagen(url):
    db = img.Imagenes()
    db.conectarMongo()
    response = requests.get(url, stream=True)
    db.guardarImagen(response.content,"prueba")
    imagen = db.devolverImagen("prueba")
    assert len(imagen) != 0
