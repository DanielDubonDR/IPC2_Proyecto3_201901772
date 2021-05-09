from flask import Flask, jsonify, request, Response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*":{"origin":"*"}})

@app.route('/Archivo', methods=['POST', 'GET'])
def RecibirArchivo():
    if request.method == 'POST':
        txt = request.data.decode('utf-8')
        archivo=open("Database/Archivo.xml", 'w', encoding='utf8')
        archivo.write(txt)
        archivo.close()
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

'''
@app.route('/Archivo', methods=['POST'])
def RecibirArchivo():
    txt = request.json['texto']
    print(txt)
    return jsonify({'message':'Se recibio el archivo'}, {'contenido': txt})
'''

if __name__=='__main__':
    app.run(debug=True, port=4000)