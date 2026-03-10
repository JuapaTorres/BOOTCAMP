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
"""
class libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio}")
        print("-" * 30)

libro1 = libro("100 años de soledad", "Gabriel Garcia Marquez", 1967)
libro2 = libro("El código Da Vinci", "Dan Brown", 2003)

print("Información del libro 1:")
libro1.mostrar_info()

print("Información del libro 2:")
libro2.mostrar_info()
"""
#Sobrecarga en python usando método *args:
"""
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self, *args):
        cantidad = len(args)

        if cantidad == 0:
            print("Hola")
        elif cantidad == 1:
            print(f"Hola, {args[0]}")
        elif cantidad == 2:
            print(f"Hola, {args[0]} de {args[1]}")
        else:
            print(f"Hola a todos, especialmente a {args[0]}")

usuario = Persona("Admin")

usuario.saludar()
usuario.saludar("Juan Pablo")
usuario.saludar("Juan Pablo", "Santiago")
usuario.saludar("Juan Pablo", "Santiago", "Chile", "Planeta tierra")

"""
#Sobrecarga de python usando método **kwargs:
"""
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self, **kwargs):
        nombre = kwargs.get("nombre")
        ciudad = kwargs.get("ciudad")

        if nombre and ciudad:
            print(f"Hola, {nombre} de {ciudad}")
        elif nombre:
            print(f"Hola, {nombre}")
        else:
            print("Hola")

usuario = Persona("Admin")

usuario.saludar()
usuario.saludar(nombre = "Juan Pablo")
usuario.saludar(ciudad = "Santiago", nombre = "Juan Pablo")
"""
#Método especial __str__() para personalizar la salida de objetos:
"""
class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f"Título: {self.titulo} - Autor: {self.autor} - Año: {self.anio}"

libro1 = Libro("El Aleph", "Jorge Luis Borges", 1949)
libro2 = Libro("1984", "George Orwell", 1949)

print("Presentación clara y profesional:")
print(libro1)
print(libro2)
"""
#Colaboración entre objetos: ejem de Coche y Motor:
"""
class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def encender(self):
        return f"Motor {self.tipo} de {self.potencia} caballos de fuerza encendido."
    
class Coche:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def arrancar(self):
        print(f"Iniciando el {self.marca} {self.modelo}...")
        mensaje_motor = self.motor.encender()
        print(mensaje_motor)
        print("El coche está listo para circular.")

mi_motor_v8 = Motor("V8", 450)
mi_coche = Coche("Ford", "Mustang", mi_motor_v8)

mi_coche.arrancar()
"""
#Composición entre objetos: 
"""
class Procesador:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad

    def __str__(self):
        return f"{self.marca} a {self.velocidad}Ghz"
    
class MemoriaRAM:
    def __init__(self, capacidad, tipo):
        self.capacidad = capacidad
        self.tipo = tipo

    def __str__(self):
        return f"{self.capacidad}GB {self.tipo}"
    
class DiscoDuro:
    def __init__(self, capacidad, tipo):
        self.capacidad = capacidad
        self.tipo = tipo

    def __str__(self):
        return f"{self.capacidad}GB {self.tipo}"
    
class Computadora:
    def __init__(self, marca, procesador, ram, disco):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.disco = disco

    def mostrar_info(self):
        print(f"--- Ficha técnica Computadora {self.marca} ---")
        print(f"Procesador: {self.procesador}")
        print(f"Memoria RAM: {self.ram}")
        print(f"Almacenamiento: {self.disco}")
        print("." * 35)

intel_i7 = Procesador("Intel Core i7", 3.8)
corsair_ram = MemoriaRAM(16, "DDR4")
samsung_ssd = DiscoDuro(512, "SSD NVMe")

mi_pc = Computadora("Dell XPS", intel_i7, corsair_ram, samsung_ssd)

mi_pc.mostrar_info()
"""

