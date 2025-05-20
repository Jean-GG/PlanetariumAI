from experta import *

# Base de conocimientos (simplificada)
datos_planetas = {
    "Mercurio": {"tipo": "rocoso", "anillos": False, "lunas": 0},
    "Venus": {"tipo": "rocoso", "anillos": False, "lunas": 0},
    "Tierra": {"tipo": "rocoso", "anillos": False, "lunas": 1},
    "Marte": {"tipo": "rocoso", "anillos": False, "lunas": 2},
    "Jupiter": {"tipo": "gaseoso", "anillos": True, "lunas": 95},
    "Saturno": {"tipo": "gaseoso", "anillos": True, "lunas": 274},
    "Urano": {"tipo": "gaseoso", "anillos": True, "lunas": 28},
    "Neptuno": {"tipo": "gaseoso", "anillos": True, "lunas": 16}
}

# Definimos los hechos
class Planeta(Fact):
    nombre: str
    pass

# Motor del sistema experto
class SistemaEspacial(KnowledgeEngine):

    @Rule(Planeta(nombre=MATCH.nombre))
    def describir_planeta(self, nombre):
        if nombre in datos_planetas:
            datos = datos_planetas[nombre]
            print(f"\n📡 Información sobre {nombre}:")
            print(f"🔸 Tipo: {datos['tipo']}")
            print(f"🔸 ¿Tiene anillos?: {'Sí' if datos['anillos'] else 'No'}")
            print(f"🔸 Número de lunas: {datos['lunas']}")
        else:
            print(f"🚫 No tengo información sobre el planeta '{nombre}'.")

# Interfaz por consola
def iniciar_sistema():
    print("🌌 Bienvenido al Sistema Experto del Espacio Exterior 🌌")
    print("Escribe el nombre de un planeta para obtener información, o 'salir' para terminar.\n")

    engine = SistemaEspacial()
    engine.reset()

    while True:
        pregunta = input("🔭 Pregunta: ¿Qué quieres saber? ").strip().capitalize()
        if pregunta == "Salir":
            print("👋 ¡Hasta pronto, explorador del cosmos!")
            break
        engine.declare(Planeta(nombre=pregunta))
        engine.run()

# Ejecutar
if __name__ == "__main__":
    iniciar_sistema()
