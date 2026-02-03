# MÓDULO DE VALIDACIONES
# Este módulo contiene funciones para verificar que las entradas del usuario sean del tipo correcto.

def leer_entero(mensaje):
#Solicita un número al usuario y valida que sea un entero positivo.
#Usa el método .isdigit() para evitar errores si el usuario ingresa letras.
    while True:
        valor = input(mensaje)
        # Verificamos si la cadena contiene solo dígitos numéricos
        if valor.isdigit():
            return int(valor)
        else:
            print(f"Error: '{valor}' no es un número entero válido. Intente de nuevo.")

