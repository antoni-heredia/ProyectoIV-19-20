import base64
from tinydb import TinyDB, Query
class Imagenes:
    client = None

    def __init__(self):
        self.client = None

    def conectarMongo(self):
        db = TinyDB('baseDatos/imagenes.json')
        self.client = db
    def guardarImagen(self,imagen,nombre):
        mydb = self.client.table('entrada')
        imagen = base64.b64encode(imagen)
        mydict = { "nombre": nombre, "imagen": str(imagen)}
        x = mydb.insert(mydict)

    def guardarImagenString(self,imagen,nombre):
        mydb = self.client.table('entrada')
        mydict = { "nombre": nombre, "imagen": imagen}
        x = mydb.insert(mydict)
        print("imagen insertada")
    def eliminarTodasImagenes(self):
        mydb = self.client.table('entrada')
        x = mydb.purge()

    def eliminarImagen(self,nombre):
        mydb = self.client.table('entrada')
        Imagen = Query()
        mydb.remove(Imagen.nombre == nombre)

    def devolverImagen(self,nombre):
        mydb = self.client.table('entrada')
        Imagen = Query()
        return  mydb.search(Imagen.nombre == nombre)


    def devolverTodasImagenes(self):
        mydb = self.client.table('entrada')
        return mydb.all()
        
    def devolverTodasImagenesNombre(self):
        mydb = self.client.table('entrada')
        return  [r['nombre'] for r in mydb]
