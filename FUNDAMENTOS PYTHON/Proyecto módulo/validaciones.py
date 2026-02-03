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

def leer_float(mensaje):
#Valida que la entrada sea un número decimal positivo.
#Reemplaza temporalmente el punto para permitir la validación con .isdigit().
    while True:
        valor = input(mensaje)
        # Validamos decimales permitiendo un solo punto en la cadena
        if valor.replace(".", "", 1).isdigit():
            return float(valor)
        else:
            print(f"Error: '{valor}' no es un número decimal válido.")