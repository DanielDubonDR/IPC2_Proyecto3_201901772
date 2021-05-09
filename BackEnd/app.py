from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from extraerDatos import Analizar

app = Flask(__name__)
cors = CORS(app, resources={r"/*":{"origin":"*"}})

def generarDatos():
    datos=Analizar()
    datos.getDatos()
    datos.generarEstadisticas()

@app.route('/Archivo', methods=['POST', 'GET'])
def RecibirArchivo():
    if request.method == 'POST':
        txt = request.data.decode('utf-8')
        archivo=open("Database/Archivo.xml", 'w', encoding='utf8')
        archivo.write(txt)
        archivo.close()
        generarDatos()
        return jsonify({'Message':'Se recibió el archivo'})
    else:
        return jsonify({'Error':'No se admite esa petición'})

@app.route('/VerArchivo', methods=['GET', 'POST'])
def MostrarArchivo():
    if request.method == 'GET':
        archivo=open("DataBase/Archivo.xml",'r', encoding='utf8')
        contenido=archivo.read()
        archivo.close()
        return(contenido)
    else:
        return jsonify({'Error':'No se admite esa petición'})

@app.route('/Estadisticas', methods=['GET', 'POST'])
def MostrarEstadisticas():
    if request.method == 'GET':
        archivo=open("DataBase/Estadisticas.xml",'r', encoding='utf8')
        contenido=archivo.read()
        archivo.close()
        return(contenido)
    else:
        return jsonify({'Error':'No se admite esa petición'})

@app.route('/filtro1', methods=['GET', 'POST'])
def fl():
    if request.method == 'POST':
        fecha=request.json['fecha']
        Datos=[]
        datos=Analizar()
        datos.getDatos()
        Usuarios=datos.getUsers()
        for i in Usuarios:
            if i.fecha==fecha:
                Dato={'usuario': i.usuario, 'cantidad': i.cantidad }
                Datos.append(Dato)
        return jsonify(Datos)
        # return jsonify({"country": "Daniel", "lifeExpectancy": 84 }, {"country": "Reinald", "lifeExpectancy": 100 },{"country": "Funciona", "lifeExpectancy": 85 })
    else:
        return jsonify({'Error':'No se admite esa petición'})

@app.route('/Fechas', methods=['GET', 'POST'])
def Fechas():
    if request.method == 'GET':
        Datos=[]
        datos=Analizar()
        datos.getDatos()
        Usuarios=datos.getDates()
        for i in Usuarios:
            Dato={'fecha': i }
            Datos.append(Dato)
        return jsonify(Datos)
    else:
        return jsonify({'Error':'No se admite esa petición'})

@app.route('/reset', methods=['GET', 'POST'])
def Resetear():
    if request.method == 'GET':
        archivo=open("Database/Archivo.xml", 'w', encoding='utf8')
        archivo.write("")
        archivo.close()
        archivo2=open("Database/Estadisticas.xml", 'w', encoding='utf8')
        archivo2.write("")
        archivo2.close()
        return jsonify({'Message':'Se eliminaron los datos'})
    else:
        return jsonify({'Error':'No se admite esa petición'})

'''
@app.route('/Archivo', methods=['POST'])
def RecibirArchivo():
    txt = request.json['texto']
    print(txt)
    return jsonify({'message':'Se recibio el archivo'}, {'contenido': txt})
'''

if __name__=='__main__':
    app.run(debug=True, port=4000)