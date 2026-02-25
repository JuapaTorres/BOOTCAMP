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
"""
def division_segura():
    try:
        n1 = input("Ingresa el primer número (dividiendo): ")
        n2 = input("Ingresa el segundo número (divisor): ")

        num1 = float(n1)
        num2 = float(n2)

        resultado = num1 / num2

    except ValueError:
        Print("Error: Debes ingresar valores numéricos. No se permiten letras o símbolos.")

    except ZeroDivisionError:
        print("Error: No es posible dividir un número entre cero.")

    else:
        print(f"Cálculo exitoso! El resultado es: {resultado:.2f}")

    finally:
        print("Proceso finalizado.")

division_segura()

"""

# CONVERSIÓN DE UNIDADES CON VALIDACIÓN
"""
def conversor_km_mi():
    FACTOR_CONVERSION = 0.621371
    while True:
        try:
            entrada = input("Ingresa la distancia en kilómetros: ")
            kilometros = float(entrada)
            if kilometros < 0:
                print("La distancia no puede ser negativa. Intenta de nuevo.")
                continue
            
            millas = kilometros * FACTOR_CONVERSION
            print(f"{kilometros} km equivalen a {millas:.2f} millas. ")
            break
        except ValueError:
            print("Error: Lo que ingresaste no es un número válido.")
            print("Por favor, usa solo números (ejemplo: 10 o 15.5).")
    print("Proceso finalizado con éxito.")

conversor_km_mi()
"""
# LANZAR EXCEPCIONES CON RAISE
#Validar edad y lanzar un error si es negativa.
"""
def validar_edad(edad):
    if edad < 0 :
        raise ValueError(f"La edad no puede ser negativa")
    print(f"Edad válida: {edad} años")

print("--- Iniciando pruebas de validación ---")
try:
    validar_edad(25)
    validar_edad(-3)
except ValueError as e:
    print(f"Error detectado: {e}")

"""

#EXCEPCIONES PERSONALIZADAS
"""
class EdadInvalidaError(Exception):
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa")
    print(f"Confirmación: La edad {edad} es válida.")

print("--- Iniciando validación de excepción personalizada ---")

valores_pruerba = [30, -5, 7, -99]

for valor in valores_pruerba:
    try:
        validar_edad(valor)
    except EdadInvalidaError as e:
        print(f"Se detectó un error personalizado: {e}")

"""
#JERARQUÍA DE EXCEPCIONES PROPIAS
#Crea y captura una jerarquía de errores personalizados.
"""
class ErrorAplicacion(Exception):
    pass

class ErrorValidacion(ErrorAplicacion):
    pass

class ErrorPermisos(ErrorAplicacion):
    pass

def verificar_usuario(rol):
    if rol == "visitante":
        raise ErrorPermisos("Acceso no autorizado")
    elif rol not in ["admin", "editor"]:
        raise ErrorValidacion("Rol inválido")
    
try:
    verificar_usuario("visitante")
except ErrorPermisos:
    print("Error: no tienes permisos suficientes")
except ErrorValidacion:
    print("Error: Datos inválidos")
except ErrorAplicacion:
    print("Otro error general de aplicación")

"""
#RE-LANZAMIENTO Y PROPAGACIÓN DE ERRORES:
#Ejemplo básico
"""
def procesar_pago(monto):
    if monto <= 0:
        raise ValueError("El monto debe ser mayor a cero.")

def ejecutar_pago():
    try:
        procesar_pago(-50)
    except ValueError as e:
        print("Error detectado en la función interna.")
        raise
"""

# Capturar un error en una función y re-lanzarlo hacia el exterior
"""
#Funciones simuladas:
def validar_email(email):
    if "@" not in email:
        raise ValueError("Email inválido")
    
def registrar_usuario(email):
    try:
        validar_email(email)
    except ValueError as e:
        print("Error interno:", e)
        raise

#código externo:

try:
    registrar_usuario("usuario_sin_arroba.com")
except ValueError:
    print("Error detectado en el sistema externo: reintenta con un email válido")
"""


#USO DEL BLOQUE FINALLY PARA LIMPIEZA Y CIERRE SEGURO:
"""
#Estructura completa:
try:
    # código que puede fallar
except:
    # manejo del error
else:
    # se ejecuta si no hubo error
finally:
    # se ejecuta siempre
"""
#Ejemplo:
"""
try:
    archivo = open("datos.txt")
    contenido = archivo.read()
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    archivo.close()
    print("Archivo cerrado")
"""

#LEER UN ARCHIVO Y CERRARLO SIEMPRE CON FINALLY
#Ejercicio:
"""
#estructura esperada:
try:
    archivo = open("info.txt", "r")
    print(archivo.read())
except FileNotFoundError:
    print("Archivo no encontrado.")
finally:
    print("Cerrando recursos...")
    archivo.close() # si fue abierto con éxito
"""
"""
archivo = None

try:
    archivo = open("info.txt", "r")
    print("Contenido del archivo:")
    print(archivo.read())

except FileNotFoundError:
    print("Error: El archivo 'info.txt' no fue encontrado.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    if archivo:
        archivo.close()
        print("Archivo cerrado correctamente.")

    print("Finalizando proceso de lectrua.")
"""

#Registro de usuario con validaciones y errores personalizados

#Ejercicio:
"""
#Definimos jerarquía de errores
class ErrorRegistro(Exception):
    pass
class NombreInvalidoError(ErrorRegistro):
    pass
class EdadInvalidaError(ErrorRegistro):
    pass
class EmailInvalidoError(ErrorRegistro):
    pass

#Implementación de sistema de registro
def registrar_usuario():
    try:
        print("-- Formulario de Registro ---")
        nombre = input("Nombre: ").strip()
        edad_str = input("Edad: ")
        email = input("Email: ").strip()

        if not nombre:
            raise NombreInvalidoError("El nombre no puede quedar vacío.")
        
        try:
            edad = int(edad_str)
        except ValueError:
            raise EdadInvalidaError("La edad debe ser un número entero.")
        
        if edad <= 0:
            raise EdadInvalidaError("La edad debe ser mayor a 0.")
        
        if "@" not in email:
            raise EmailInvalidoError("El email ingresado no tiene formato válido.")
        
        print(f"\n Usuario {nombre} registrado con éxito!")

    except NombreInvalidoError as e:
        print(f"Error en el nombre: {e}")
    except EdadInvalidaError as e:
        print(f"Error en la edad: {e}")
    except EmailInvalidoError as e:
        print(f"Error en el email: {e}")
    except ErrorRegistro as e:
        print(f"Error general de registro: {e}")
    except Exception as e:
        print(f"Error inesperado del sistema: {e}")

    finally:
        print("fin del proceso de registro.")

registrar_usuario()

"""

#MANEJANDO ARCHIVOS CON PYTHON

#Ejercicio L6 AE6:

#Ejercicio 1: Crear y Escribir
"""
try:
    with open("datos.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Bienvenido al sistema de persistencia de datos!\n")
        archivo.write("Este es un mensaje de prueba.\n")
    print("Ejercicio 1: archivo creado y escrito con éxito.")

#Ejercicio 2: Lectura línea por línea

    with open("datos.txt", "r", encoding="utf-8") as archivo:
        print("\n Contenido de datos.txt:")
        linea = archivo.readline()
        while linea:
            print(f"- {linea.strip()}")
            linea = archivo.readline()
except FileNotFoundError:
    print("Error: El archivo no existe.")

#Ejercicio 3: Obtención de Atributos

import os
from datetime import datetime

def obtener_info_archivo(nombre_archivo):
    try:
        stats = os.stat(nombre_archivo)

        print(f"Atributos de {nombre_archivo}")
        print(f"    •   Tamaño: {stats.st_size} bytes")

        fecha_mod = datetime.fromtimestamp(stats.st_atime)
        print(f"    •   Última modificación: {fecha_mod.strftime('%d/%m/%Y %H:%M:%S')}")

    except FileNotFoundError:
        print("No se pudo obtener info: El archivo no existe.")

obtener_info_archivo("datos.txt")

#Ejercicio 4 y 5: Modificación, Renombrado y Movimiento
#Ejercicio 4: Agregar contenido (Append)
import shutil

with open("datos.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Esta es una linea agregada posteriormente.\n")

#Ejercicio 5: Renombrar y Mover
try:
    if not os.path.exists("backup"):
        os.makedirs("backup")
        print("\n Carpeta 'backup' creada.")
    
    os.rename("datos.txt", "archivo_modificado.txt")

    shutil.move("archivo_modificado.txt", "backup/archivo_modificado.txt")
    print("Archivo renombrado y movido a 'backup/' con éxito.")

except FileNotFoundError:
    print("Error: No se encontró el archivo para mover.")

#Ejercicio 6: Cierre seguro y manejo de Excepciones
def proceso_final_seguro(ruta):
    archivo = None
    try:
        archivo = open(ruta, "r")
        print(archivo.read())

    except FileNotFoundError:
        print(f"Error crítico: El archivo en '{ruta}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para leer '{ruta}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    finally:
        if archivo and not archivo.closed:
            archivo.close()
            print("Recurso liberado correctamente.")
        print("Proceso finalizado.")

proceso_final_seguro("backup/archivo_modificado.txt")

"""




