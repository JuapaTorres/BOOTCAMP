#MÓDULO DE PROCESOS
#Aquí se gestiona el almacenamiento y cálculo de los datos del sistema.

#Estructura de datos: Lista para almacenar diccionarios de productos
inventario = []

#Estructura de datos: Conjunto (set) para almacenar categorías sin duplicados
categorias_unicas = set()

def agregar_producto(nombre, stock, precio, categoria):
#Recibe los datos del producto, calcula el valor total y los guarda en un diccionario dentro de la lista de inventario.
#Creamos un diccionario para organizar la información del producto (Clave-Valor)
    producto = {
        "nombre": nombre,
        "stock": stock,
        "precio": precio,
        "categoria": categoria,
        "valor_total": stock * precio # Cálculo del subtotal
    }
    
    #Agregamos el producto a la lista global con la funciuón .append
    inventario.append(producto)
    
    #Agregamos la categoría al conjunto con .add
    categorias_unicas.add(categoria)
    
    print(f"\nProducto '{nombre}' registrado exitosamente en el sistema.")

def mostrar_inventario():
#Recorre la lista de productos y muestra la información formateada.
#Calcula el valor total acumulado del inventario.
#Verificamos si la lista está vacía usando la función len
    if len(inventario) == 0:
        print("\nNo hay datos registrados en el inventario actualmente.")
    else:
        print("\n--- REPORTE DE GESTIÓN TECNOLÓGICA ---")
        total_general = 0
        
        #Iteramos sobre la lista de productos
        for p in inventario:
            #Acumulamos el valor total de cada producto
            total_general += p["valor_total"]
            
            print(f"Producto: {p['nombre']} | Categoría: {p['categoria']} | Subtotal: ${p['valor_total']}")
        
        print("-" * 35)
        #Resumen final de datos
        print(f"VALOR TOTAL DEL INVENTARIO: ${total_general}")
        print(f"CATEGORÍAS PRESENTES: {categorias_unicas}")
        print("-" * 35)