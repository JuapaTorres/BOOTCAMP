#numero = 0

#while True:
#    print(f"Número: {numero}")
#    numero += 1
#    if numero == 12855:
#        print("Por fin detuve el bucle infinito")
#        break

#Crear un programa que cuente del 1 al 100 usando while


#numero = 1
#
#while True:
#    print(numero)
#    if numero == 100:
#        print("Llegamos al 100")
#        break
#    numero += 1

#Crear un programa que pida constantemente al usuario un número, sumar cada número ingresado por el usuario, finalizar el programa cuando el usuario ingrese 0. Mostrar la suma total al finalizar el programa

#suma_total = 0
#while True:
#    numero = int(input("ingresa un número, ingresa 0 para terminar: "))
#    if numero == 0:
#        break
#    suma_total += numero
#print(f"Fin, la suma total es: {suma_total}")

#Crear un programa que pida al usuario una contraseña, tiene 3 intentos, al tercer intento bloquear las credenciales (Mostrar un mensaje de bloqueo). Indicarle al usuario cuántos intentos quedan.


#password = "pistacho"
#intentos_restantes = 3
#
#while True:
#    intento = input(f"Introduce la contraseña: ")
#    if intento == password:
#        print("Acceso correcto")
#        break
#
#    intentos_restantes -= 1
#    if intentos_restantes > 0:
#        print(f"Esa no es la palabra mágica. Te quedan {intentos_restantes} intentos.")
#    else:
#        print("Acceso bloqueado, agotaste tus 3 intentos.")
#        break



# Bucle for se usa para iterar

#nombres = ["Felipe", "Fernanda", "Juan Pablo"]
#
#for nombre in nombres:
#    print(nombre)
#
#range muestra hasta el fin -1 
#range es numérico


#for i in range(0, 101, 2):
#    print(i)
#
#Crear un programa que muestre el rango de números ingresado por el usuario.
#(Inicio y un fin -1)
#

#inicio = int(input("Ingresa un número de inicio: "))
#fin = int(input("ingresa un número final: "))

#for i in range(inicio, fin + 1):
#    print(i)

#print(f"El rango va desde {inicio} hasta {fin}")

#Crear un programa que itere sobre una frase ingresada por el usuario y muestre la cantidad de caractéres que tiene esa frase

#frase = input("Ingresa una frase: ").lower

#cantidad_de_caracteres = 0
#vocales = 0
#for caracter in frase:
#    cantidad_de_caracteres += 1
#    if caracter in "aeiou":
#        vocales += 1
#
#print(f"La frase tiene {cantidad_de_caracteres} caracteres.")
#print(f"La frase tiene {vocales} vocales.")

# Iterar en números del 1 al 100 y sumar la cantidad de números pares y mostrar el resultado

#suma_pares = 0
#
#for numero in range(0, 101, 2):
#    suma_pares += numero
#
#print(f"La suma de los pares entre el 1 al 100 es: {suma_pares}")

# Crear un programa que permita registrar y sumar "n" cantidad de ventas, también debe permitir ver el total de ventas y salir del programa.

total_ventas = 0

while True:
    print("\n### REGISTRO DE VENTAS ###")
    print("1. Agregar ventas")
    print("2. Mostrar total de ventas")
    print("3. Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        cantidad = int(input("¿Cuántas ventas desea registrar?: "))
        
        if cantidad > 0:
            for i in range(1, cantidad + 1):
                monto = float(input(f"Ingrese el monto de la venta {i}: "))
                
                if monto > 0:
                    total_ventas += monto
                else:
                    print("Monto es inválido, no se puede sumar")
        else:
            print("La cantidad debe ser mayor a cero")

    elif opcion == "2":
        print(f"\nTotal vendido: ${total_ventas:.2f}")

    elif opcion == "3":
        print("Gracias por usar el programa. Saliendo...")
        break

    else:
        print("\nOpción no válida, intente nuevamente")

