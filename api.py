from flask import Flask, url_for, request, render_template
import requests, json
import model
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/modelo.html')
def modelo():
    return render_template('modelo.html')

@app.route('/result', methods=['POST'])
def result():
    resp = request.form
    #Traer datos del formulario
    precio = resp['precio']
    man = resp['mantenimiento']
    puerta = resp['puertas']
    persona = resp['personas']
    cajuela = resp['cajuela']
    seguridad = resp['seguridad']

    prediccion = model.decision(precio, man,puerta,
    persona, cajuela,seguridad )

    return render_template("resultado.html", n=prediccion[0])



if __name__ == '__main__':
    app.run(debug=True)