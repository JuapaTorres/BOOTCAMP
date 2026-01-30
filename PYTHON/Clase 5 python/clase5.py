"""
nombre = "Juan Pablo"
nombre2 = "Cesar"
nombre3 = "Alonso"
nombre4 = "Miguel"
"""
# Para las listas usamos []
# Tipo de colección que guarda datos
# Las listas son ordenadas y mutables. 
# Mutables se refieren a que se pueden modificar.
# Ordenada se refiere a que tienen un índice o index.
# indice = n elemento -1, el indice comienza por cero (0)
# Números positivos de izq a der y números negativos de der a izq
# Las listas pueden ser anidadas

#nombres = ["Juan Pablo", "Cesar", "Alonso", "Miguel"] 
#notas = [7.0, 6.5, 3.0, 4,5]
#datos = [True, 10, "Cadena", 10.0]

#print(len(nombres)) para saber la cantidad de elementos
#print(nombres[-1]) para saber el último elemento (de orden positivo de izq a der)

# Agregar elementos a la lista
"""
nombres = ["Cesar"]
nuevos_nombres = ["Alonso", "Juan Pablo", "Fernanda"]
#print(nombres)
#Agregar
nombres.append("Alonso")
nombres.append("Luis")
nombres.append("Mariana")
#print(nombres)
nombres.insert(3, "Kalev")
#print(nombres)
nombres.extend(nuevos_nombres)
print(nombres)
#Append agrega a la derecha, insert a la izquierda y extend agrega a la izquierda en grupo

# Editar
nombres[0] = "Carolina"
print(nombres)

# Eliminar con pop: 
# pop sin argumento elimina el último elemento, para eliminar el deseado se asigna un número
nombres.pop()
print(nombres)

#Otro metodo para eliminar es usando remove, se debe ingresar el dato correcto 
nombres.remove("Mariana")
print(nombres)

#Y la instrucción "del" para eliminar un elemento en base a su indice
del nombres[4]
print(nombres)
"""

# Crear un programa que tome la asistencia de los alumnos:
# Si el alumno está presente, agregarlo a la lista de presentes
# Si el alumno está ausente, agregarlo a la lista de ausentes
# Si el alumno llega tarde, agregarlo a la lista de presentes
# Si el alumno se retira, agregarlo a la lista de ausentes
# (Mover entre listas)


"""
alumnos = [
"ABBY ARAYA",
"ALONSO TAPIA",
"CAROLINA PÁEZ",
"CATALINA BRAVO",
"CRISTIAN RIQUELME",
"FABIOLA ARRATIA",
"FELIPE VÁSQUEZ",
"FELIPE LEÓN",
"FERNANDA ERICES",
"HERVIN PRADINES",
"JAIRO SANCHEZ",
"JOSÉ RODRÍGUEZ",
"JUANPABLO TORRES",
"KALEV YULES",
"LILIANA ZABALAGA",
"MARIANA COX",
"MIGUEL HERNÁNDEZ",
"MILENE JAUREGUI",
"NATALIA ",
"PEDRO PAVEZ",
"RODRIGO ALFARO",
"VIVIAN ROA"
]

presentes = []
ausentes = []

while True:
print('''
###### REGISTRO DE ASISTENCIA #####
1.- Pasar asistencia
2.- Marcar un alumno como presente
3.- Marcar un alumno como ausente
4.- Ver lista de presentes
5.- Ver lista de ausentes
6.- Salir
''')

opcion = input("Ingrese una opción: ")

if opcion == "1":
for alumno in alumnos:
if alumno in presentes or alumno in ausentes:
continue

while True:
respuesta = input(f"¿{alumno} esta presente? (s/n): ")

if respuesta == "s":
presentes.append(alumno)
break
elif respuesta == "n":
ausentes.append(alumno)
break
else:
print("❌ Respuesta no válida")
elif opcion == "2":
nombre = input("¿Ingrese el nombre y apellido del alumno: ").upper()

if nombre in alumnos:
if nombre in ausentes:
ausentes.remove(nombre)
if nombre not in presentes:
presentes.append(nombre)

print(f"✅ {nombre} maracdo como presente")
else:
print("❌ No existe el alumno")
elif opcion == "3":
nombre = input("¿Ingrese el nombre y apellido del alumno: ").upper()

if nombre in alumnos:
if nombre in presentes:
presentes.remove(nombre)
if nombre not in ausentes:
ausentes.append(nombre)

print(f"❌ {nombre} marcado como ausente")
else:
print("❌ No existe el alumno")
elif opcion == "4":
print("PRESENTES:")
presentes.sort()
for alumno in presentes:
print(alumno)
elif opcion == "5":
print("AUSENTES:")
ausentes.sort()
for alumno in ausentes:
print(alumno)
elif opcion == "6":
print(f'''
#####📃RESUMEN#####
Presentes: {presentes}
Ausentes: {ausentes}
Total de alumnos: {len(alumnos)}
Saliendo del sistema...
''')
break
else:
print("❌ La opcion ingresada no es válida")
"""

"""
# Crear un programa que separe números pares e impares ingresados por el usuario.
# El usuario debe determinar cuántos números ingresar.
# Ir sumando los números pares y sumar los números impares.
# Al finalizar el programa debe mostrar los números pares e impares ingresados, así cómo la suma de los mismos.
# Finalizar con 0

pares = []
impares = []

suma_pares = 0
suma_impares = 0

print('''
Separemos y contemos números!
ingresa números enteros!
Para finalizar presiona 0
''')

while True:
    numero = int(input("ingresa un número: "))
    if numero == 0:
        break #Loop infinito aqui hasta q ponga 0
    
    if numero % 2 == 0:
        pares.append(numero)
        suma_pares += numero
    else:
        impares.append(numero)
        suma_impares += numero

print("Números pares:", pares)
print(f"Suma de números pares: {suma_pares}")
print("Números impares:", impares)
print(f"Suma de números impares: {suma_impares}")
"""

#TUPLAS
#Para definir una tupla se usa () en vez de [] cómo en las otras listas.
#Las tuplas no pueden ser modificables, inmutables. Sólo son de lectura.
#De momento no vamos a trabajar con tuplas

#DICCIONARIOS
#Para diccionarios se usa {} en formato clave:valor
#Las keys(Claves) son únicas en cada diccionario, no se pueden repetir.

#datos = {
#    "nombre": "cesar",
#    "edad":40,
#    "curso": "python"
#    }
"""
#Para ver datos usamos []
print(datos["nombre"])
#Modificar
datos["nombre"] = "miguel"
#Agregar
datos["apellido"] = "Hernandez"
#Eliminar
del datos["curso"]
print(datos)
"""
#Formas de buscar tuplas

# for dato in datos:
#    print(f"{dato}: {datos[dato]} ")

# for key, valor in datos.items():
#    print(f"{key}: {valor}")

# Crear un programa que permita comprar determinados items.
# El usuario podrá consultar por un item y el programa deberá informar si existe o no existe (Operador de pertenencia in).
# Si existe, agregar al carrito.
# Si no existe, informar que no hay stock.
# Cada producto debe ser sumado al total de la compra.
# Cuando el usuario finalice su compra, mostrar el carrito de compras con su total a pagar.

productos = {
"leche": 1200,
"mantequilla": 1800,
"yerba-mate": 4800,
"arroz": 2400,
"fideos": 1200,
"aceite": 2400,
"atun": 2000
}

carrito = []
total = 0

print("ALMACÉN LAS TUPLAS")
while True:
    print("Productos: Leche, Mantequilla, Yerba mate, Arroz, Fideos, Aceite, Atun")
    item = input("Ingrese producto para comprar. (Escribe (salir) para finalizar)").lower()

    if item == "salir":
        break
    if item in productos:
        carrito.append(item)

        total += productos[item] 
        print(f"{item} agregado.")
    else:
        print(f"No tenemos stock de {item}.")

print("Resumen de compra")
print("Carrito de compra:")
for producto in carrito:
    print(f"{producto.capitalize()}: ${productos[producto]}")
print(f"Total a pagar: ${total}")
print("Gracias por su compra!")

