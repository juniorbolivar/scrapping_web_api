from flask import Flask, Response,jsonify
#from flask_pymongo import PyMongo
#from bson import json_util
## genere un archivo json offline para recrear la fuente
from noticias import Noticias

app = Flask(__name__)
#app.config['MONGO_URI'] = 'mongodb://junior:18168188@cluster0.iugq2.mongodb.net/Noticias?retryWrites=true&w=majority'
#mongo = PyMongo(app)
## problemas con mi computadora para generar la conexion con el  mongo cloud

## prueba get todas las noticias 
@app.route('/Noticias')
def getnoticias():
    return jsonify({"noticias":Noticias,"Message":"Lista de Noticias"})

## buscar por campo fuente- si no existe la fuente da un mensaje de fuente no encontrada
@app.route('/Noticias/<string:fuente>')
def getfuente(fuente):
    fuenteFound= [Fuente for Fuente in Noticias if Fuente['Fuente']==fuente]
    if (len(fuenteFound) > 0):
     return jsonify({"fuente":fuenteFound[0]})
    return jsonify({"message":"Fuente no encontrada"})


app.run(port=4000, debug=True)

## puerto: http://127.0.0.1:4000/noticias
