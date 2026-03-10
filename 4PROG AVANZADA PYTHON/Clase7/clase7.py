

"""
archivo = open("datos.txt", "r")

print(archivo.read())

archivo.close()
"""

"""
#Leer
with open("datos.txt", "r") as archivo:
    print(archivo.deadlines())

"""
"""
ruta_absoluta = "C://PROYECTOS/BOOTCAMP/PROG AVANZADA PYTHON/Clase7/datos.txt"

with open(ruta_absoluta, "r") as archivo:
    print(archivo.read())
"""

"""
#Escribir

"""
"""
ruta_absoluta = "C://PROYECTOS/BOOTCAMP/PROG AVANZADA PYTHON/Clase7/datos.txt"

alumnos = ["Juan\n", "Pedro\n", "Diego\n"]

with open(ruta_absoluta, "w") as archivo:
    archivo.writelines(alumnos)

"""
"""
ruta_notas = "C://PROYECTOS/BOOTCAMP/PROG AVANZADA PYTHON/Clase7/notas.txt"

suma = 0
contador = 0

with open(ruta_notas, "r") as notas:
    for linea in notas:
        nota = float(linea.strip())
        suma += nota
        contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"Promedio: {promedio:.1f}")
else:
    print("No hay notas a promediar")

"""
#Contar cuantas líneas tiene el poema
#Contar cuantas caracteres tiene el poema
#Encontrar cuál es la linea más larga
"""
ruta_poema = "poema.txt"

total_lineas = 0
total_caracteres = 0
linea_mas_larga = ""

with open(ruta_poema, "r") as archivo:
    for linea in archivo:
        total_lineas += 1
        contenido_linea = linea.strip()
        total_caracteres += len(contenido_linea)
        if len(contenido_linea) > len(linea_mas_larga):
            linea_mas_larga = contenido_linea


print(f"Cantidad de líneas: {total_lineas}")
print(f"Cantidad de caracteres: {total_caracteres}")
print(f"Línea más larga es: {linea_mas_larga} y tiene {len(linea_mas_larga)} caracteres")

"""
""" 
try:
    archivo = open("noas.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe")
finally:
    try:
        archivo.close()
    except:
        pass
"""


import csv

""" with open("modulo/ventas.csv", newline="", encoding="utf-8") as archivo:
    lectura = csv.reader(archivo)
    for fila in lectura:
        print(fila)
"""
"""
total_general_ventas = 0
producto_estrella = ""
cantidad_mas_vendida = 0


with open("modulo/ventas.csv", newline="", encoding="utf-8") as archivo:
    reader = csv.reader(archivo)
    next(ventas)

    for venta in reader:
        nombre_producto = venta[0]
        precio = int(venta[2])
        cantidad = int(venta[3])

        total_venta = precio * cantidad
        total_general_ventas += total_venta

        if cantidad > cantidad_mas_vendida:
            cantidad_mas_vendida = cantidad
            producto_estrella = nombre_producto

        print(f"Producto: {nombre_producto} - total ventas: ${total_venta}")

print(f"Total general de ventas: ${total_general_ventas}")
print(f"Producto más vendido: {producto_estrella} ({cantidad_mas_vendida} unidades)")
"""

"""
Calcular el total de ventas
Encontrar el produto que más se vendió

"""

"""
total_general = 0
totales_por_producto = {}

with open("modulo/ventas.csv", newline="", encoding="utf-8") as archivo:
    reader = csv.reader(archivo)
    next(reader)

    for venta in reader:
        nombre_producto = venta[0]
        precio = int(venta[2])
        cantidad = int(venta[3])

        total_venta = precio * cantidad
        totales_por_producto[nombre_producto] = total_venta
        total_general += total_venta

    print(f"Total general: {total_general}")

    producto_mayor = max(totales_por_producto, key=totales_por_producto.get)
    print(f"Producto que más genero dinero: {producto_mayor}")

    with open("resumen_ventas.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["producto", "total"])

        for producto, total in totales_por_producto.items():
            writer.writerow([producto, total])
"""


import json

with open("estudiantes.json", "r", encoding="utf-8") as archivo:
    estudiantes = json.load(archivo)

    def obtener_nota(e):
        return e["nota"]
    
    mejor_nota = max(estudiantes, key=obtener_nota)

    print(f"Mejor evaluado: {mejor_nota["nombre"]} - Nota {mejor_nota["nota"]}")

#metodos "w" dump()



