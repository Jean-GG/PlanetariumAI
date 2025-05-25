from flask import Flask, render_template, request
from engine import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    tipo_consulta = ""
    
    if request.method == "POST":
        tipo_consulta = request.form.get("consulta")
        
        if tipo_consulta == "nombre":
            nombre = request.form.get("nombre", "").capitalize()
            resultado = obtener_info_planeta(nombre)

        elif tipo_consulta == "anillos":
            resultado = buscar_con_anillos()

        elif tipo_consulta == "tipo":
            tipo = request.form.get("tipo", "").lower() 
            resultado = buscar_por_tipo(tipo)

        elif tipo_consulta == "lunas":
            minimo = int(request.form.get("minimo_lunas", 0))
            resultado = buscar_por_lunas(minimo)

        elif tipo_consulta == "comparar":
            p1 = request.form.get("planeta1", "").capitalize()
            p2 = request.form.get("planeta2", "").capitalize()
            resultado = comparar_lunas(p1, p2)

    return render_template("index.html", resultado=resultado, consulta=tipo_consulta)

if __name__ == "__main__":
    app.run(debug=True)
