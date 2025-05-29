# app.py

from flask import Flask, render_template, request
from preguntas import procesar_pregunta
from nasa_api import obtener_apod

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    respuesta = ""
    if request.method == "POST":
        pregunta = request.form.get("pregunta")
        if pregunta:
            respuesta = procesar_pregunta(pregunta)

    apod = obtener_apod()
    return render_template("index.html", respuesta=respuesta, apod=apod)

if __name__ == "__main__":
    app.run(debug=True)
