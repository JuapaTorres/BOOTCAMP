def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b != 0:
        return a/b
    else:
        return "No se puede dividir por cero"
    

import random

def numero_secreto(a, b):
    return random.randint(1, 20)

def comprobar_intento(intento, secreto):

    if intento == secreto:
        print("Adivinaste!")
    elif intento < secreto:
        print("El número secreto es mayor!")
    else:
        print("El número secreto es menor!")