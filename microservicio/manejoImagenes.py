import base64
from tinydb import TinyDB, Query

def conectarMongo():
    db = TinyDB('baseDatos/imagenes.json')
    return db

def guardarImagen(client,imagen,nombre):
    mydb = client.table('entrada')
    imagen = base64.b64encode(imagen)
    mydict = { "nombre": nombre, "imagen": str(imagen)}
    x = mydb.insert(mydict)

def eliminarTodasImagenes(client):
    mydb = client.table('entrada')
    x = mydb.purge()

def eliminarImagen(client,nombre):
    mydb = client.table('entrada')
    Imagen = Query()
    mydb.remove(Imagen.nombre == nombre)

def devolverImagen(client,nombre):
    mydb = client.table('entrada')
    Imagen = Query()
    return  mydb.search(Imagen.nombre == nombre)


def devolverTodasImagenes(client):
    mydb = client.table('entrada')
    return mydb.all()
