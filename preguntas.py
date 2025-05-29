# preguntas.py

from motor_inferencia import *

def procesar_pregunta(pregunta):
    pregunta = pregunta.lower()

    if "¿cuántas lunas" in pregunta or "cuantas lunas" in pregunta:
        for planeta in base_conocimiento:
            if planeta["nombre"].lower() in pregunta:
                return f"{planeta['nombre']} tiene {planeta['lunas']} lunas."

    if "tiene anillos" in pregunta:
        for planeta in base_conocimiento:
            if planeta["nombre"].lower() in pregunta:
                return f"{planeta['nombre']} {'tiene' if planeta['anillos'] else 'no tiene'} anillos."

    if "planetas rocosos" in pregunta:
        planetas = planetas_tipo("rocoso")
        return "Planetas rocosos: " + ", ".join(p["nombre"] for p in planetas)

    if "planetas con anillos" in pregunta:
        planetas = planetas_con_anillos()
        return "Planetas con anillos: " + ", ".join(p["nombre"] for p in planetas)

    if "mayor número de lunas" in pregunta or "más lunas" in pregunta:
        planetas = sorted(base_conocimiento, key=lambda p: p["lunas"], reverse=True)
        top = planetas[0]
        return f"{top['nombre']} tiene la mayor cantidad de lunas: {top['lunas']}."

    if "más grande que" in pregunta:
        partes = pregunta.split("más grande que")
        if len(partes) == 2:
            p1 = partes[0].split()[-1].capitalize()
            p2 = partes[1].strip().capitalize()
            return mas_grande_que(p1, p2)

    if "más lunas que" in pregunta:
        partes = pregunta.split("más lunas que")
        if len(partes) == 2:
            p1 = partes[0].split()[-1].capitalize()
            p2 = partes[1].strip().capitalize()
            return comparar_lunas(p1, p2)

    if "habitables" in pregunta or "vida" in pregunta:
        planetas = planetas_habitables()
        return "Planetas potencialmente habitables: " + ", ".join(p["nombre"] for p in planetas)

    return "No entendí tu pregunta. Intenta con otra relacionada a los planetas."
