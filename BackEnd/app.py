from flask import Flask, jsonify, request, Response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*":{"origin":"*"}})

@app.route('/Archivo', methods=['POST'])
def RecibirArchivo():
    txt = request.data.decode('utf-8')
    archivo=open("Database/Archivo.xml", 'w', encoding='utf8')
    archivo.write(txt)
    archivo.close()
    return jsonify({'message':'Se recibió el archivo'})

@app.route('/VerArchivo', methods=['GET'])
def MostrarArchivo():
    archivo=open("DataBase/Archivo.xml",'r', encoding='utf8')
    contenido=archivo.read()
    archivo.close()
    return(contenido)

'''
@app.route('/Archivo', methods=['POST'])
def RecibirArchivo():
    txt = request.json['texto']
    print(txt)
    return jsonify({'message':'Se recibio el archivo'}, {'contenido': txt})
'''

if __name__=='__main__':
    app.run(debug=True, port=4000)