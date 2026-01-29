# Lista global que almacenará los diccionarios de productos
inventario = []

def agregar_producto(nombre, cantidad, precio):
    #Crea un diccionario con la información del producto y lo guarda en la lista.
    nuevo_producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
        "total_valor": cantidad * precio
    }
    inventario.append(nuevo_producto)
    print(f"Producto '{nombre}' agregado exitosamente.")

def mostrar_inventario():
    #Recorre la lista y muestra los datos formateados con f-strings.
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\n--- LISTA DE PRODUCTOS ---")
        for p in inventario:
            print(f"Item: {p['nombre']} | Stock: {p['cantidad']} | Precio: ${p['precio']:.2f}")

def calcular_total_recursivo(lista_productos, n):
#Suma el total_valor de todos los productos de forma recursiva.
#n es el número de elementos a procesar.
# Caso base: si no hay más elementos, la suma es 0
    if n == 0:
        return 0
# Caso recursivo: suma el valor del producto actual + el resultado de la función con el resto
    else:
        actual = lista_productos[n-1]["total_valor"]
        return actual + calcular_total_recursivo(lista_productos, n-1)
    
