from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/Archivo', methods=['POST'])
def RecibirArchivo():
    txt = request.json['texto']
    print(txt)
    return jsonify({'message':'Se recibio el archivo'}, {'contenido': txt})

if __name__=='__main__':
    app.run(debug=True, port=4000)