# motor_inferencia.py

from conocimiento import base_conocimiento

def buscar_planeta(nombre):
    for planeta in base_conocimiento:
        if planeta["nombre"].lower() == nombre.lower():
            return planeta
    return None

def planetas_tipo(tipo):
    return [p for p in base_conocimiento if p["tipo"] == tipo]

def planetas_con_anillos():
    return [p for p in base_conocimiento if p["anillos"]]

def planetas_con_mas_lunas(min_lunas):
    return [p for p in base_conocimiento if p["lunas"] >= min_lunas]

def planetas_habitables():
    return [p for p in base_conocimiento if p["habitabilidad"] in [True, "posible"]]

def comparar_lunas(p1, p2):
    planeta1 = buscar_planeta(p1)
    planeta2 = buscar_planeta(p2)
    if planeta1 and planeta2:
        if planeta1["lunas"] > planeta2["lunas"]:
            return f"{p1} tiene más lunas que {p2}."
        elif planeta1["lunas"] < planeta2["lunas"]:
            return f"{p2} tiene más lunas que {p1}."
        else:
            return f"{p1} y {p2} tienen la misma cantidad de lunas."
    return "Uno o ambos planetas no existen."

def mas_grande_que(p1, p2):
    planeta1 = buscar_planeta(p1)
    planeta2 = buscar_planeta(p2)
    if planeta1 and planeta2:
        if planeta1["diametro"] > planeta2["diametro"]:
            return f"{p1} es más grande que {p2}."
        elif planeta1["diametro"] < planeta2["diametro"]:
            return f"{p2} es más grande que {p1}."
        else:
            return f"{p1} y {p2} tienen el mismo tamaño."
    return "No se encontró información de los planetas."
