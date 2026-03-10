#Manejo de excepciones

#ZeroDivisionError
""" 
try:
    resultado = 10/0
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir un número por cero")

print("El programa se sigue ejecutando")
"""

#IndexError: Para los índices fuera de rango.
#KeyError: Para las claves inexistentes.
#TypeError: Para operaciones inválidas entre tipos de datos incompatibles.
#ValueError: Valor de argumento inválido en una función.
#ZeroDividionError: División con divisor cero.

"""

Crear una función con dos parámetros(a) y (b)
Esa función debe dividir dos números ingresados por el usuario
Usar excepciones para capturar el error en caso de dividir por cero

"""
""" 
def dividir(a, b):
    try:
        resultado = a/b
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Error, no se puede dividir por cero.")

try:
    n1 = float(input("ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))
    dividir(n1, n2)

except ValueError:
    print("Error: ingresa sólo valor numérico.")
    
"""

"""
Crear una variable que tome un dato ingresado por el usuario
Convertir ese dato a entero
Primeramente ingresar un número
Luego ingresar un caracter

"""
""" 
dato = input("Ingresa algo:")
numero = int(dato)
print(f"El número es: {numero}")
"""

"""
Pedir 3 números separados por coma (1,2,3)
Convertir a int, capturar errores y agregar a una lista

"""
"""
lista_numeros = []

ingreso = input("Ingresa 3 números separados por coma (ej: 1,2,3):")
partes = ingreso.split(",")
print(" --Procesanding-- ")

for item in partes:
    try:
        numero = int(item.stip())
        lista_numeros.append(numero)
        print(f"'{item.strip()}' convertido y agregado.")

    except ValueError:
        print(f"Error: {item.strip()} no es un número válido.")

print(f"Lista final de enteros: {lista_numeros}")
"""
"""
datos = input("Ingrese 3 números separados por una coma:")

try:
    lista = datos.split(",")
    numeros = []

    for dato in lista:
        numeros.append(int(dato))

    suma_entero = sum(numeros)
    print(f"La suma total de los números es: {suma_entero}")

except ValueError as e:
    print(f"Error de conversion: {e}")

"""

#Raise
""" 
def verificar_edad(edad):
    if edad < 18:
        raise ValueError("Debe ser mayor de edad para continuar")
    return "Acceso permitido"

try:
    print(verificar_edad(18))
except ValueError:
    print("Error")
"""
""" 
def validar_edad(edad):
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un entero")
    
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    
    if edad < 18:
        raise ValueError("Debe ser mayor de edad")
    
    return True

try:
    edad = int(input("Ingrese la edad:"))
    validar_edad(edad)
    print("Edad válida")

except(TypeError, ValueError) as e:
    print(f"Ha ocurrido un error. {e}")
"""
#Ejercicio para después
"""
Crear un programa que valide una contraseña
-Debe tener cómo mímino 8 caracteres
-Debe contener al menos un número isdigit()
-Debe contener al menos una mayúscula isupper()

"""

"""
Crear una clase cuenta
atributo saldo
método retirar
validar si el monto a retirar es mayor a cero
validar los fondos, si hay fondos insuficientes informar al usuario

"""

""" class Cuenta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("Error: El monto a retirar debe ser mayor a cero.")

        if monto > self.saldo:
            raise Exception(f"Fondo insuficiente, tu saldo es {self.saldo}.")

        else:
            self.saldo -= monto 
            print(f"Retiro exitoso. Saldo restante: ${self.saldo}")

mi_cuenta = Cuenta(1000)
print("Saldo inicial: ${mi_cuenta.saldo}")

while True:
    try:
        entrada = input("Ingrese monto a retirar (o escriba 'salir' para finalizar.): ")
        if entrada.lower() == 'salir':
            break

        monto_usuario = float(entrada)
        mi_cuenta.retirar(monto_usuario)
        print(f"Saldo actual: ${mi_cuenta.saldo}")

    except ValueError as e:
        print(f"Error: Entrada no válida. {e}")

    except Exception as e:
        print(f"Transacciónn rechazada: {e}")

print(f"Gracias por preferirnos. Saldo final: ${mi_cuenta.saldo}") """

""" class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes")
        
        self.saldo -= monto
        return self.saldo
    
cuenta = Cuenta(1000)

try:
    monto = float(input("Ingrese el monto a retirar: "))
    saldo = cuenta.retirar(monto)
    print(f"Nuevo saldo: ${saldo}")
except ValueError as e:
    print(f"Error: {e}") """

"""
Crear un programa que valide una contraseña
-Debe tener cómo mímino 8 caracteres len()
-Debe contener al menos un número isdigit()
-Debe contener al menos una mayúscula isupper()
#pista: Tienen que iterar sobre la contraseña ingresada
#pass
#len(pass)
#if pass.isdigit() # cada caracter
#if pass.isupper() # cada caracter
"""
"""

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    
    tiene_numero =  False
    tiene_mayuscula = False

    for caracter in contraseña:
        if caracter.isdigit():
            tiene_numero = True
        if caracter.isupper():
            tiene_mayuscula = True
        
    if not tiene_mayuscula:
        raise ValueError("La contraseña debe tener al menos una letra mayúscola.")
    
    if not tiene_numero:
        raise ValueError("La contraseña debe tener al menos un número.")
    
    return "Contraseña válida"

while True:
    try:
        pass_usuario = input("Crea una contraseña: ")
        resultado = validar_contraseña(pass_usuario)
        print(resultado)
        break
    except ValueError as e:
        print(f"Error de validación: {e}")

"""


#EJEMPLO PROFE




"""
#EJEMPLO EXCEPCIONES PERSONALIZADAS:
class ErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

def verificar_usuario(usuario):
    usuarios = ["admin", "root", "user"]

    if usuario not in usuarios:
        raise ErrorPersonalizado("Usuario no autorizado")
    return "Acceso concedido"

try:
    print(verificar_usuario("root"))

except ErrorPersonalizado as e:
    print(f"Se detectó un error: {e}")
"""

"""
import tkinter as tk
from tkinter import messagebox


def validar_password(password):
    if len(password) < 8:
        raise ValueError("Debe tener como minimo 8 caracteres")
    
    es_numero = False
    for letra in password:
        if letra.isdigit():
            es_numero = True
    
    if es_numero == False:
        raise ValueError("Debe contener al menos un numero")
    
    es_mayuscula = False
    for letra in password:
        if letra.isupper():
            es_mayuscula = True
    
    if es_mayuscula == False:
        raise ValueError("Debe contener al menos una mayuscula")
    
    return True

def verificar():
    try:
        password = entrada_pass.get()
        validar_password(password)
        messagebox.showinfo("Validado", "Contraseña segura")
    except ValueError as e:
        messagebox.showinfo("Error", f"{e}")





ventana = tk.Tk()
ventana.title("Password Security Validator")
ventana.geometry("350x250")

#Reglas
longitud = tk.Label(ventana, text="1. Debe tener cómo mínimo 8 caracteres")
longitud.place(x=10,y=20)

numero = tk.Label(ventana, text="2. Debe contener al menos un número")
numero.place(x=10,y=40)

mayuscula = tk.Label(ventana, text="3. Debe contener al menos una mayuscula")
mayuscula.place(x=10,y=60)


#Validador
label = tk.Label(ventana, text="Ingrese la contraseña a validar:")
label.place(x=80, y=110)

entrada_pass = tk.Entry(ventana, show="*")
entrada_pass.place(x=80, y=130, width=180)

boton = tk.Button(ventana, text="Verificar", command=verificar)
boton.place(x=130, y=160)

ventana.mainloop()
"""

