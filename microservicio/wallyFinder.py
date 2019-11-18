from flask import Flask, send_from_directory
import base64
from microservicio import Imagenes as img
from flask_restplus import Resource, Api,fields
from flask import Flask, make_response, request, redirect, url_for, jsonify
from werkzeug.datastructures import FileStorage

from .send import encolar
app = Flask(__name__)



api = Api(app, doc='/doc/')
status = api.namespace('Status', path="/")
wally = api.namespace('WallyFinder', path="/")
app.config.from_pyfile('./config_file.cfg')



@status.route('/status')
class CheckStatus(Resource):
    def get(self):
        return {'status': "OK"}, 200



@wally.route('/imagen')
class recibirImagen(Resource):
    @wally.response(200, 'Devuelve una lista con todas las imagenes disponibles')
    def get(self):
        db = img.Imagenes()
        db.conectarMongo()

        return db.devolverTodasImagenesNombre(),200

    @wally.response(200, 'Eliminadas todas las imagenes')
    def delete(self):
        db = img.Imagenes()
        db.conectarMongo()
        db.eliminarTodasImagenes()
        return {'Imagenes eliminada': 'true'},200

parser = api.parser()
parser.add_argument('image', type=FileStorage, location='files', required=True)


@wally.route('/imagen/<nombre>')
class downloadFile (Resource):
    @wally.response(404, 'Imagen encontrada: false')
    @wally.response(200, 'Imagen encontrada: true')
    @api.doc(params={"nombre": "Nombre de la imagen"})
    def get(self,nombre):
        db = img.Imagenes()
        db.conectarMongo()
        imagenBase64 = db.devolverImagen(nombre)
        if not imagenBase64:
            return {'Imagen encontrada':'False'},404
        image_binary = base64.b64decode(imagenBase64[0]["imagen"])
        
        response = make_response(image_binary)
        response.headers.set('Content-Type', 'image/jpeg')
        response.headers.set(
            'Content-Disposition', 'attachment', filename='%s.jpg' % nombre)
        return response

    @wally.response(404, 'Imagen recibida: false')
    @wally.response(200, 'Imagen recibida: true')
    @wally.expect(parser, validate=True)
    def post(self,nombre):
        if 'image' not in request.files:
            return {'Imagen recibida': 'false'},404

        image = request.files['image'].read()
        image = base64.b64encode(image)

        encolar(image.decode("utf-8"), nombre)
        return {'Imagen recibida': str(nombre)},200

    def delete(self,nombre):
        db = img.Imagenes()
        db.conectarMongo()
        db.eliminarImagen(nombre)
        return {'Imagen eliminada': 'true'},200
@app.errorhandler(404)
def error_404(error):
    return "Pagina no encontrada. Error 404", 404

if __name__ == "__main__":
    app.run(host=app.config["HOST"],debug=app.config["DEBUG"])