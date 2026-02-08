#Código estructurado EJ:
"""
def crear_cliente(nombre, edad):
    return {"nombre": nombre, "edad": edad}

def saludar(cliente):
    print(f"Hola, {cliente['nombre']}")

cliente = crear_cliente("Ana", 30)

saludar(cliente)
"""
#Código orientado a objetos EJ:

"""
class cliente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, {self.nombre}")

cliente = cliente("Ana", 30)
cliente.saludar()
"""
"""
class mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def saludar(self):
        print(f"Hola, soy {self.nombre}, un {self.raza} de {self.edad} años.")

mascota = mascota("Copito", 14, "Poodle")
mascota.saludar()
"""