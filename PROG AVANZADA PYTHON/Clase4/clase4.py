
#Ejercicio de Herencia y polimorfismo:
"""
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau"
    
class Pollito(Animal):
    def hacer_sonido(self):
        return "Pio pio"
    
def imprimir_sonidos(animales):
    print("--- Demostración de Polimorfismo ---")
    for animal in animales:
        print(f"{animal.nombre} dice: {animal.hacer_sonido()}")

def es_animal_valido(objeto):
    if isinstance(objeto, Animal):
        print(f"Confirmado: El objeto es un Animal (clase o subclase).")
        return True
    else:
        print("Error: El objeto NO pertenece a la jerarquía Animal.")

mis_mascotas = [
    Perro("Copito", 14),
    Gato("Panther", 3),
    Pollito("Zelda", 1)
]

imprimir_sonidos(mis_mascotas)

print("\nVerificación de clase:")
es_animal_valido(mis_mascotas[0])
"""

#Ejercicio en clase en vivo herencia simple:
"""
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice Guau")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice Miau")

mi_perro = Perro("Boby")
mi_perro.hablar()
mi_gato = Gato("Michi")
mi_gato.hablar()
"""
"""
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def mostrar_datos(self):
        print(f"Empleado: {self.nombre} - Sueldo: {self.sueldo}")

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, bono):
        super().__init__(nombre, sueldo)
        self.bono = bono

    def mostrar_datos(self):
        total = self.sueldo + self.bono
        print(f"Gerente: {self.nombre} - Sueldo total: {total}")

class Vendedor(Empleado):
    def __init__(self, nombre, sueldo, comision):
        super().__init__(nombre, sueldo)
        self.comision = comision

    def mostrar_datos(self):
        total = self.sueldo + self.comision
        print(f"Vendedor: {self.nombre} - Sueldo total: {total}")


pedro = Gerente("Pedro", 3000, 1500)
juan = Vendedor("Juan", 800, 1500)

pedro.mostrar_datos()
juan.mostrar_datos()

"""

'''
Crear:
Clase base (Padre) Vehiculo --> marca, modelo, descripcion()
Clase hija: Auto --> Agregar puertas
Clase hija: Moto --> Agregar cilindrada

'''
'''
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        print(f"Vehículo: {self.marca} {self.modelo}")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def descripcion(self):
        print(f"Auto {self.marca} {self.modelo} con {self.puertas} puertas")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def descripcion(self):
        print(f"Moto {self.marca} {self.modelo} de {self.cilindrada}CC")

mi_auto = Auto("Subaru", "Impreza", 5)
mi_moto = Moto("Kawasaki", "Ninja", 400)

mi_auto.descripcion()
mi_moto.descripcion()
'''

#Herencia múltiple:
'''
class Volador:
    def volar(self):
        print("Estoy volando")

class Nadador:
    def nadar(self):
        print("Estoy nadando")

class Pato(Volador, Nadador):
    pass

pato = Pato()
pato.volar()
pato.nadar()
'''
'''
class Audio:
    def reproducir_audio(self):
        print("Reproduciendo audio...")

class Video:
    def reproducir_video(self):
        print("Reproduciendo video...")

class SmartTV(Audio, Video):
    def encender(self):
        print("TV encendida")

qled = SmartTV()
qled.encender()
qled.reproducir_audio()
qled.reproducir_video()
'''
"""
Crear:
Clase Padre 1: Trabajador --> trabajar()
Clase Padre 2: Estudiante --> estudiar()
Clase hija: Heredar Trabajador y Estudiante
Instanciar y probar métodos

"""

#Polimorfismo clase en vivo:
#Polimorfismo por sobrecarga
"""
class Calculadora:
    def sumar(self, a, b, c = 0):
        return a + b + c
    
calculadora = Calculadora()
print(calculadora.sumar(1,2,))
print(calculadora.sumar(1,2,3))

"""
"""
class Operaciones:
    def multiplicar(self, *numeros): #*args
        resultado = 1
        for num in numeros:
            resultado *= num
        return resultado

op = Operaciones()

print(op.multiplicar(2,3))
print(op.multiplicar(2,3,4))
"""

"""
Crear:
Clase Conversor --> convertir()
- Si se recibe un argumento --> Convertir a string
- Si se recibe dos argumentos --> Repetir el string n cantidad de veces
- Si hay más de dos argumentos, mostrar error
- Usar *args

"""
"""
class Conversor:
    def convertir(self, *args):
        cantidad = len(args)
        if cantidad == 1:
            print(f"Convertido: {str(args[0])}")
        elif cantidad == 2:
            print(f"Repetir: {str(args[0]) * args[1]}")
        else:
            print(f"Error: {cantidad} argumentos es mucho.")

mi_conversor = Conversor()
mi_conversor.convertir(123)
mi_conversor.convertir("Jamon", 4)
mi_conversor.convertir(1, 2, "Tres", "Cuatro")
"""

"""

class Conversor():
    def convertir(self, *args):
        if len(args[0])==1:
            return str(args[0])
        elif len(args==2):
            texto = str(args[0])
            cantidad = args[1]
            return texto * cantidad
        else:
            return "Error. Cantidad no válida de argumentos"

print(Conversor.convertir(100))
print(Conversor.convertir(100, 4))
print(Conversor.convertir(100, 4, 10))

"""

"""
class Forma:
    def area(self):
        print("Área genérica")

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        print(f"El área del cuadrado es: {self.lado ** 2}")

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        print(f"El área del triangulo es: {(self.base * self.altura)/2}")

class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        print(f"El area del rectangulo es: {(self.base * self.altura)}")

c = Cuadrado(2)
t = Triangulo(2,4)
r = Rectangulo(2,4)

c.area()
t.area()
r.area()
"""

"""
class MetodoPago:
    def pagar(self, monto):
        print("Porcesando pago...")

class TarjetaCredito(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando {monto} con tarjeta de credito")

class Transferencia(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando {monto} mediante transferencia")

pagos = [TarjetaCredito(), Transferencia()]

for metodo in pagos:
    metodo.pagar(1000)
"""

"""
Crear:
Clase Instrumento --> tocar()
Clases hijas: Guitarra, Piano, Bateria

Cada clase debe sobreescribir tocar
Probar con una lista de instrumentos

"""
"""
class Instrumento:
    def tocar(self):
        print("El instrumento está sonando.")

class Guitarra(Instrumento):
    def tocar(self):
        print("La Guitarra está sonando.")

class Piano(Instrumento):
    def tocar(self):
        print("Suenan las teclas del Piano")

class Bateria(Instrumento):
    def tocar(self):
        print("La Batería lleva el ritmo!")

banda = [Guitarra(), Piano(), Bateria()]
print("Comienza la música!")

for instrumento in banda:
    instrumento.tocar()

"""

#isistance() 
"""
class Animal:
    pass

class Gato(Animal):
    pass

class Perro(Animal):
    pass

gato = Gato()
perro = Perro()

print(isinstance(gato, Gato))
print(isinstance(gato, Animal))
print(isinstance(gato, Perro))

"""
"""


"""
"""
class CuentaBancaria:
    pass

class CuentaCorriente(CuentaBancaria):
    pass

class CuentaVista:
    pass

def procesar_cuenta(cuenta):
    if isinstance(cuenta, CuentaBancaria):
        print("Cuenta válida")
    else:
        print("Tipo de cuenta incorrecta")

cuenta_corriente = CuentaCorriente()
cuenta_vista = CuentaVista()

procesar_cuenta(cuenta_corriente)
procesar_cuenta(cuenta_vista)

"""

"""

Crear:
Clase Producto
Clase Libro hereda Producto
Clase Electronico hereda Producto

Crear una funcion mostrar_info(objeto)

Si es Libro --> Imprimir "Es un libro"
Si es electronico --> Imprimir "Es un electronico"
Si no es Producto --> Imprimir "No es producto válido"

"""

"""
class Producto:
    def __init__(self, nombre):
        self.nombre = nombre

class Libro(Producto):
    pass

class Electronico(Producto):
    pass

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar(self):
        print(self.nombre)

def mostrar_info(objeto):
    if isinstance(objeto, Libro):
        print("Es un libro.")
    elif isinstance(objeto, Electronico):
        print("Es un electrónico.")
    else:
        print("No es un producto válido.")

prod1 = Libro("El código Da Vinci")
prod2 = Electronico("Iphone 25 pro max turbo ultra")
prod3 = Perro("Boby")

mostrar_info(prod1)
mostrar_info(prod2)
mostrar_info(prod3)
"""

