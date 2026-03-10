"""
Crear una clase Animal con atributos nombre y edad
y un método hablar que muestre un sonido
Crear 2 objetos de clase e instanciar método

"""
""" 
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        print(f"El animal {self.nombre} está haciendo sonidos")

class Perro(Animal):
    def hablar(self):
        print("Guau!")

    def presentarse(self):
        print(f"Soy el perro {self.nombre} y tengo {self.edad} años.")

class Gato(Animal):
    def hablar(self):
        print("Miau!")

    def presentarse(self):
        print(f"Soy el gato {self.nombre} y tengo {self.edad} años.")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")

    def presentarse(self):
        print(f"Soy la vaca {self.nombre} y tengo {self.edad} años.")

perro = Perro("Boby", 7)
gato = Gato("Panther", 2)
vaca = Vaca("Lola", 9)

perro.presentarse()
perro.hablar()
gato.presentarse()
gato.hablar()
vaca.presentarse()
vaca.hablar()
"""

"""
Crear:
Una clase Persona con atributo nombre y edad "encapsulado"
Hacer uso de setter y getter para manejar atributos privados

"""
""" 
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad

personas = [
    Persona("Juan-Pablo", 37),
    Persona("Claudio", 28),
    Persona("Francisco", 40),
    Persona("Daniela", 35)
]

print("Lista Original:")
for p in personas:
    print(f"- {p.get_nombre()}: {p.get_edad()} años")


for p in personas:
    nueva_edad = p.get_edad() + 1
    p.set_edad(nueva_edad)

print("Lista actualizada:")
for p in personas:
    print(f"- {p.get_nombre()}: {p.get_edad()} años")
"""

"""
Con esa misma clase, crear una lista de personas y actualizar sus edades mediante un bucle.
"""

#Ejercicio herencia, encapsulación y polimorfia
""" 
class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    def get_nombre(self):
        return self.__nombre
    
    def set_salario(self, nuevo_salario):
        self.__salario = nuevo_salario

    def get_salario(self):
        return self.__salario

    def calcular_bono(self):
        return 0
    
class Gerente(Empleado):
    def calcular_bono(self):
        return self.get_salario() * 0.2
    
class Vendedor(Empleado):
    def calcular_bono(self):
        return self.get_salario() * 0.1

gerente = Gerente("Ana Pacheco", 1000)
vendedor = Vendedor("Luis Tapia", 600)

print(f"Bono gerente: {gerente.calcular_bono()}")
print(f"Bono vendedor: {vendedor.calcular_bono()}")

"""


