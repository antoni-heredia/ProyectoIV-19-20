from flask import Flask, send_from_directory
import base64

from flask_restful import Resource, Api
from flask import Flask, render_template, request, redirect, url_for, jsonify

from .send import encolar
app = Flask(__name__)
api = Api(app)

app.config.from_pyfile('./config_file.cfg')


class recibirImagen(Resource):
    def get(self):
        return {'Use el metodo POST para enviar una imagen':""}
    
    def post(self):

        if 'image' not in request.files:
            flash('No hay image en el envio')
            return {'Imagen recibida': 'false'},200

        image = request.files['image'].read()
        image = base64.b64encode(image)

        nombre = request.form['name']

        encolar(image.decode("utf-8"), nombre)
        return {'Imagen recibida': str(nombre)},200

class CheckStatus(Resource):
    def get(self):
        return {'status': "OK"}, 200


@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    filename = "./img/wally.png"
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)

@app.errorhandler(404)
def error_404(error):
    return "Pagina no encontrada. Error 404", 404

api.add_resource(recibirImagen, '/')
api.add_resource(CheckStatus, '/status')

if __name__ == "__main__":
    app.run(host=app.config["HOST"],debug=app.config["DEBUG"])