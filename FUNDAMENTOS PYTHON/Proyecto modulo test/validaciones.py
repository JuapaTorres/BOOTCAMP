# MÓDULO DE VALIDACIONES
# Este módulo contiene funciones para verificar que las entradas del usuario sean del tipo correcto.

def leer_entero(mensaje):
#Solicita un número al usuario y valida que sea un entero positivo usando excepciones.
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
            if valor < 0:
                print("Error: El número no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print(f"Error: '{entrada}' no es un número válido. Ingrese solo dígitos.")
            continue

def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if not texto:
            print("Error: Este campo no puede quedar vacío.")
            continue
        return texto