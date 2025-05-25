# engine.py

datos_planetas = {
    "Mercurio": {"tipo": "rocoso", "anillos": False, "lunas": 0},
    "Venus": {"tipo": "rocoso", "anillos": False, "lunas": 0},
    "Tierra": {"tipo": "rocoso", "anillos": False, "lunas": 1},
    "Marte": {"tipo": "rocoso", "anillos": False, "lunas": 2},
    "Júpiter": {"tipo": "gaseoso", "anillos": True, "lunas": 79},
    "Saturno": {"tipo": "gaseoso", "anillos": True, "lunas": 83},
    "Urano": {"tipo": "gaseoso", "anillos": True, "lunas": 27},
    "Neptuno": {"tipo": "gaseoso", "anillos": True, "lunas": 14}
}

def obtener_info_planeta(nombre):
    planeta = datos_planetas.get(nombre)
    if planeta:
        return {"nombre": nombre, **planeta}
    return None

def buscar_por_tipo(tipo):
    return [{ "nombre": k, **v } for k, v in datos_planetas.items() if v["tipo"] == tipo]

def buscar_con_anillos():
    return [{ "nombre": k, **v } for k, v in datos_planetas.items() if v["anillos"]]

def buscar_por_lunas(minimo):
    return [{ "nombre": k, **v } for k, v in datos_planetas.items() if v["lunas"] >= minimo]

def comparar_lunas(planeta1, planeta2):
    p1 = datos_planetas.get(planeta1)
    p2 = datos_planetas.get(planeta2)
    if p1 and p2:
        if p1["lunas"] > p2["lunas"]:
            return f"{planeta1} tiene más lunas ({p1['lunas']}) que {planeta2} ({p2['lunas']})"
        elif p2["lunas"] > p1["lunas"]:
            return f"{planeta2} tiene más lunas ({p2['lunas']}) que {planeta1} ({p1['lunas']})"
        else:
            return f"Ambos planetas tienen la misma cantidad de lunas ({p1['lunas']})"
    return "Uno o ambos planetas no existen."
