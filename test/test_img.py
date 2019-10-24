
# content of test_expectation.py
import pytest
import mimetypes
import requests
import sys
from microservicio import manejoImagenes as db
import ruamel.yaml


@pytest.mark.parametrize("url", ["https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/f_auto,q_auto,w_1100/v1555285691/shape/mentalfloss/waldomain.png","https://miro.medium.com/max/1500/1*yO4EVVeBHYIrxKXDGY_-zw.jpeg"])
def test_imagen(url):
    response = requests.get(url, stream=True)
    assert response.headers['Content-Type'].split("/")[0] == "image"

@pytest.mark.parametrize("url", ["https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/f_auto,q_auto,w_1100/v1555285691/shape/mentalfloss/waldomain.png","https://miro.medium.com/max/1500/1*yO4EVVeBHYIrxKXDGY_-zw.jpeg"])
def test_guardarImagen(url):
    yaml = ruamel.yaml.YAML()
    data = yaml.load(open('microservicio/config_db_ci.cfg'))
    client = db.conectarMongo(data)
    response = requests.get(url, stream=True)
    db.guardarImagen(client,response.content,"Wally")

def test_eliminarTodasImagenes():
    yaml = ruamel.yaml.YAML()
    data = yaml.load(open('microservicio/config_db_ci.cfg'))
    client = db.conectarMongo(data)    
    db.eliminarTodasImagenes(client)

def test_devolverUnaImagen():
    yaml = ruamel.yaml.YAML()
    data = yaml.load(open('microservicio/config_db_ci.cfg'))
    client = db.conectarMongo(data)
    imagen = db.devolverImagen(client,"Wally")
