from flask import Flask ,jsonify ,request, render_template, send_from_directory
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend

# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://eli24177x:claveeli@eli24177x.mysql.pythonanywhere-services.com/eli24177x$default'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none

db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow

# Ruta para servir archivos estáticos desde la carpeta img
@app.route('/img/<path:filename>')
def custom_static(filename):
    return send_from_directory('img', filename)

@app.route('/')
def index():
    return render_template('productos.html')

if __name__ == '__main__':
    app.run(debug=True)

from controladores.producto_controlador import *
from controladores.usuario_controlador import *


# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True)   # ejecuta el servidor Flask en el puerto 5000
