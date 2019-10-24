import pymongo
import base64
import ruamel.yaml

yaml = ruamel.yaml.YAML()
data = yaml.load(open('microservicio/config_db.cfg'))

def conectarMongo():
    client = pymongo.MongoClient("mongodb+srv://"+data['db_user']+":"+data['db_password']+"@"+data['db_host']+"/"+data['db_name']+"?retryWrites=true&w=majority")
    return client

def guardarImagen(client,imagen,nombre):
    mydb = client["Wally"]
    mycol = mydb["imagenesEntrada"]
    mydict = { "nombre": nombre, "imagen": base64.b64encode(imagen)}
    x = mycol.insert_one(mydict)

def eliminarTodasImagenes(client):
    mydb = client["Wally"]
    mycol = mydb["imagenesEntrada"]
    x = mycol.delete_many({})


def devolverImagen(client,nombre):
    client = conectarMongo()
    mydb = client["Wally"]
    mycol = mydb["imagenesEntrada"]
    myquery = { "nombre": "wally" }
    return mycol.find(myquery) #por si hay mas de una imagen con el mismo nombre que pueda recibir todas

def devolverTodasImagenes(client):
    client = conectarMongo()
    mydb = client["Wally"]
    mycol = mydb["imagenesEntrada"]
    return mycol.find()

