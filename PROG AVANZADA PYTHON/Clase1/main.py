#La programación orientada a objetos busca representar objetos del mundo real y busca facilitar la reutilización del código.
#Un objeto es una instancia de una clase
#Las clases tienen atributos y métodos / Caracteristicas y funcionalidades.
#
"""
numero1 = 20 (Esta es una variable global)

def dato():
    numero1 = 10 (Esta es una variable)

print(numero1)
"""
#Evitar trabajar con variables globales!!


#Ahora vamos a ver las clases y cómo definir
#Las clases se usan con la palabra reservada "Class"
"""
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura / 2
    
Triangulo1 = Triangulo(10, 5)
Triangulo2 = Triangulo(20, 10)
print(f"El área del triangulo 1 es {Triangulo1.calcular_area()}")
print(f"El área del Triangulo 2 es {Triangulo2.calcular_area()}")

"""
"""
class automovil:
    def __init__(self, marca, modelo, anio, color, transmision, combustible):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.transmision = transmision
        self.combustible = combustible

    def acelerar(self):
        print(f"{self.marca} - {self.modelo} está acelerando")
        
    def frenar(self):
        print(f"{self.marca} - {self.modelo} está frenando")

auto_felipe = automovil("Nissan", "Qashqai", 2009, "gris", "Automatica", "Bencina")

auto_cristian = automovil("Toyota", "Corolla", 2020, "Plata", "Mecanico", "Bencina")
auto_felipe.acelerar()
auto_cristian.acelerar()

"""

#Un objeto es una instancia de una clase
# def __init__ es un constructor, contruye el objeto
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

persona1 = Persona("Carlos", 31)
persona2 = Persona("Cesar", 40)
persona3 = Persona("Diego", 32)

persona3.presentarse()
"""
#Clase es el molde
#Objeto es lo que produce la instancia
#Instancia es el proceso de crear el objeto

"""
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

perro1 = Perro("Bailey", "Kiltroberman")
perro2 = Perro("Max", "Husky siberiano")

perro1.ladrar()
"""

"""
class Auto:
    def __init__(self, marca, color, velocidad):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        self.velocidad -= 10

mi_auto = Auto("Toyota", "Plata", 0)
print(f"Velocidad actual: {mi_auto.velocidad} km/h")

mi_auto.acelerar()
print(f"Velocidad actual: {mi_auto.velocidad} km/h")
mi_auto.frenar()
print(f"Velocidad actual: {mi_auto.velocidad} km/h")
"""
"""
class Auto:
    def __init__(self, marca, color, velocidad):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad

    def acelerar(self, factor=1):
        self.velocidad += 10*factor


    def frenar(self, factor =1):
        self.velocidad -= 10 * factor

mi_auto = Auto("Toyota", "Plata", 0)
print(f"Velocidad actual: {mi_auto.velocidad} km/h")

mi_auto.acelerar(4)

print(f"Velocidad actual: {mi_auto.velocidad} km/h")
mi_auto.frenar(2)
print(f"Velocidad actual: {mi_auto.velocidad} km/h")
"""


#El atributo es la propiedad definidad de la clase
#El estado es el valor en un momento determinado


#Abstracción permite representar solamente las caracteristicas escenciales del objeto, 
#ignorando detalles internos que no son importantes al momento de crear la instancia.

#Encapsulamiento: Restringir el acceso a ciertos atributos o métodos de una clase
#Ejemplo de encapsulamiento:
"""
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, cantidad):
        if cantidad < 0:
        self.__saldo += cantidad
        print(f"Deposito exitoso. Nuevo saldo {self.__saldo}")
        else:
        print("La cantidad debe ser mayor a cero")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
        self.__saldo -= cantidad
    else:
    print("Fondos insuficientes")

    def mostar_saldo(self):
    print(f"Saldo actual: {self.__saldo}")

cuenta_profe = CuentaBancaria("Cesar", 1000)
cuenta_profe.mostar_saldo()
"""
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Juan Pablo", 36)
persona2 = Persona("Cesar", 40)

print(f"Persona 1: {persona1.nombre} y tiene {persona1.edad} años.")
print(f"Persona 2: {persona2.nombre} y tiene {persona2.edad} años.")

persona1.edad = 37

print(f"Persona 1: {persona1.nombre} y tiene {persona1.edad} años.")
print(f"Persona 2: {persona2.nombre} y tiene {persona2.edad} años.")

persona1.profesion = "DJ"
persona2.profesion = "Programador"

print(f"{persona1.nombre} es {persona1.profesion}")
print(f"{persona2.nombre} es {persona2.profesion}")
"""
#Crear una clase Termostato que permita aumentar o disminuir la temperatura ambiente
#Si está activado el modo ahorro, no permitir aumentar a más de 20 grados celsius
"""
class Termostato:
    def __init__(self, marca):
        self.marca = marca
        self.temperatura = 21
        self.modo = "Normal"

    def cambiar_modo(self, nuevo_modo):
        self.modo = nuevo_modo
        print(f"Modo cambiado a: {self.modo}")

    def subir_temperatura(self):
        if self.modo == "Ahorro" and self.temperatura >= 25:
            print("Alerta, no se puede subir más la temperatura en modo Ahorro")
        else:
            self.temperatura += 1
            print(f"Temperatura actual: {self.temperatura} grados")

    def bajar_temperatura(self):
        self.temperatura -= 1
        print(f"Temperatura actual: {self.temperatura} grados")

dormitorio = Termostato("EcoCool")
dormitorio.cambiar_modo("Ahorro")

for temp in range(7):
    dormitorio.subir_temperatura()

"""
"""
class Celular:
    def __init__(self, marca, modelo, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento

    def encender(self):
        print(f"Prendiendo {self.marca} {self.modelo}")

    def ver_info(self):
        print("Info del celular..")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"AlmacenamientoÑ: {self.almacenamiento} TB")

mi_celu = Celular("Iphone", "23 Pro Max Turbo", 128)

mi_celu.encender()
mi_celu.ver_info()

"""

