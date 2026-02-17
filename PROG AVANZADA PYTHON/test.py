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
    
class Pajaro(Animal):
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
    Pajaro("Zelda", 1)
]

imprimir_sonidos(mis_mascotas)

print("\nVerificación de clase:")
es_animal_valido(mis_mascotas[0])
"""

#Ejercicio de errores y excepciones:

#DEMO:
"""
numero = int(input("Ingresa un número: "))
resultado = 10 / numero
print("Resultado:", resultado)
"""
#DEMO try/except:
"""
def solicitar_numero():
    try:
        entrada = input("Por favor, ingrese un número entero: ")
        numero = int(entrada)
        print(f"Éxito! El número {numero} es válido.")

    except ValueError:
        print("Error: Lo que ingresaste no es un número entero válido.")
        print("Asegúrate de no usar letras ni puntos decimales (ej. usa '10' en lugar de '10.5').")

solicitar_numero()
"""

# CONVERSIÓN DE UNIDADES CON VALIDACIÓN
