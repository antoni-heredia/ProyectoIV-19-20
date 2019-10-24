from flask import Flask, send_from_directory

from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('config_file.cfg')

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    filename = "./img/wally.png"
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"])