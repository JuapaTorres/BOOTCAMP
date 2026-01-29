def leer_entero(mensaje):
#Función para validar que el usuario ingrese un número entero.
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: Por favor ingresa un número positivo.")
                continue
            return valor
        except ValueError:
            print("Error: Debes ingresar un número válido (no letras).")

def leer_float(mensaje):
#Valida que el usuario ingrese un número decimal (float) positivo.
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Error: Debes ingresar un número (ejemplo: 10.5).")
