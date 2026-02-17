#Atributos! 
"""
class Auto:
    def __init__(self, marca, modelo, anio):
        self.marca = marca #publico
        self._modelo = modelo #protegido_
        self.__anio = anio #privado__
"""
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad


#Accesadores o getters
    def obtener_edad(self):
        return self.__edad


#Mutadores o setters
def set_edad(self, edad_nueva):
    if edad_nueva > 0:
        self._edad = edad_nueva
    else:
        print("La edad no puede ser negativa")


juan_pablo = Persona("Juan Pablo", 37)
juan_pablo.set_edad(38)

print(juan_pablo.get_edad())
"""

#Crear una clase con sus respectivos atributos y métodos y crear instancias de esa clase y usar sus respectivos métodos
#crear en la clase aparte un getter y un setter
"""
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self._energia = 100

    def consultar_energia(self):
        return f"Energía actual de {self.nombre}: {self._energia}%"
    
    def modificar_energia(self, nueva_energia):
        if nueva_energia > 100:
            self._energia = 100
            print("Energía al máximo!")
        elif nueva_energia < 0:
            print("El jugador se ha quedado sin energía.")
        else:
            self._energia = nueva_energia
            print(f"Energía actualizada a {self._energia}")

    def saludar(self):
        print(f"Hola, soy {self.nombre} y estoy listo para jugar.")

player = Jugador("Link")

player.saludar()
print(player.consultar_energia())

player.modificar_energia(80)

player.modificar_energia(500)

print(player.consultar_energia())
"""

#Métodos de clase
"""
class CuentaBancaria:
    tasa_interes = 0.05

    def __init__(self, titular, saldo): #MÉTODO INSTANCIA
        self.titular = titular
        self.saldo = saldo

    @classmethod #MÉTODO DE CLASE
    def cambiar_interes(cls, nueva_tasa):
        cls.tasa_interes = nueva_tasa

    @staticmethod #MÉTODO ESTÁTICO
    def validar_monto(monto):
        return monto > 0

"""

#SOBRECARGA DE MÉTODOS
"""
class Calculadora:
    def sumar(self,*args):
        return sum(args)
    
calculadora = Calculadora()
print(calculadora.sumar(2,3))
print(calculadora.sumar(2,3,4))

"""

#COLABORACIÓN ENTRE OBJETOS
"""
class Motor:
    def encender(self):
        print("Motor encendido")

    def apagar(self):
        print("Motor apagado")

class Auto:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.encender()
        print("El auto está en marcha")

    def detener(self):
        self.motor.apagar()
        print("El auto está detenido")

mi_auto = Auto()
mi_auto.arrancar()
mi_auto.detener()

"""


#COMPOSICIÓN ENTRE OBJETOS:
"""
class Bateria:
    def __init__(self, capacidad):
        self.capacidad = capacidad

    def mostrar_capacidad(self):
        print(f"Capacidad de bateria: {self.capacidad}")

class Notebook:
    def __init__(self):
        self.bateria = Bateria(5000)

    def mostrar_info(self):
        print("Información de batería")
        self.bateria.mostrar_capacidad()

mi_notebook = Notebook()
mi_notebook.mostrar_info()
"""
"""
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print(f"Hola, soy {self.nombre}")

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

    def dar_clase(self):
        print(f"El profesor {self.nombre} está dando la clase.")

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor #Colaboración
        self.estudiantes = [] #Carga múltiple

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def iniciar_clase(self):
        print(f"Iniciando el curso: {self.nombre}")
        self.profesor.dar_clase()
        for estudiante in self.estudiantes:
            estudiante.presentarse()

juanpablo = Estudiante("Juan Pablo")
cesar = Profesor("Cesar Astorga")
python = Curso("Python", cesar)
python.agregar_estudiante(juanpablo)
python.iniciar_clase()
"""

