#MÓDULO DE PROCESOS
#Aquí se gestiona el almacenamiento y cálculo de los datos del sistema.

#Estructura de datos: Lista para almacenar diccionarios de productos
inventario = []

#Estructura de datos: Conjunto (set) para almacenar categorías sin duplicados
categorias_unicas = set()

def agregar_producto(nombre, stock, precio, categoria):
#Recibe los datos del producto, calcula el valor total y los guarda en un diccionario dentro de la lista de inventario.
#Creamos un diccionario para organizar la información del producto (Clave-Valor)
#Usamos formato para el ingreso y salida de la info (.strip y .title)
    nombre_formateado = nombre.strip().title()
    categoria_formateada = categoria.strip().title()

    producto = {
        "nombre": nombre_formateado,
        "stock": stock,
        "precio": precio,
        "categoria": categoria_formateada,
        "valor_total": stock * precio # Cálculo del subtotal
    }
    
    #Agregamos el producto a la lista global con la funciuón .append
    inventario.append(producto)
    
    #Agregamos la categoría al conjunto con .add
    categorias_unicas.add(categoria_formateada)
    print(f"\nProducto '{nombre_formateado}' registrado exitosamente en el sistema.")

def mostrar_inventario():  #Se verifica si la lista está vacía con len
    if len(inventario) == 0:
        print("\nInventario vacío.")
    else:
        print("\n--- REPORTE DE EXISTENCIAS (CLP) ---")
        total_general = 0
        #Iteramos sobre la lista de productos
        for p in inventario:
            total_general += p["valor_total"]

            print(f"Item: {p['nombre']} | Cant: {p['stock']} | Subtotal: ${p['valor_total']:,}")
        
        print("-" * 40)
        #Resumen final
        print(f"VALOR TOTAL INVENTARIO: ${total_general:,} CLP")
        print(f"CATEGORÍAS: {categorias_unicas}")
        print("-" * 40)