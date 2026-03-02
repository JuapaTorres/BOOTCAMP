#MÓDULO DE PROCESOS
#Aquí se gestiona el almacenamiento y cálculo de los datos del sistema.
#Estructura de datos: Lista para almacenar diccionarios de productos
inventario = []
categorias_unicas = set() 

def calcular_valor_recursivo(cantidad, precio): #Acá vemos recursividad para el cálculo
    if cantidad == 0:
        return 0
    return precio + calcular_valor_recursivo(cantidad - 1, precio)

def agregar_producto(nombre, stock, precio, categoria):
    nombre_f = nombre.strip().title()
    cat_f = categoria.strip().title()

    datos_fijos = (nombre_f, cat_f)

    total = calcular_valor_recursivo(stock, precio)

    producto = {
        "identidad": datos_fijos, # Tupla guardada aquí
        "nombre": nombre_f,
        "stock": stock,
        "precio": precio,
        "categoria": cat_f,
        "valor_total": total
    }
    
    inventario.append(producto)
    categorias_unicas.add(cat_f)
    print(f"\n✅ Producto '{nombre_f}' registrado exitosamente.")

def mostrar_inventario():
    if not inventario:
        print("\nInventario vacío.")
        return
    
    print("\n--- REPORTE DE EXISTENCIAS ---")
    total_general = 0
    for p in inventario:
        total_general += p["valor_total"]
        n, c = p["identidad"]
        print(f"Item: {n} ({c}) | Cant: {p['stock']} | Subtotal: ${p['valor_total']:,}")
    
    print(f"\nVALOR TOTAL: ${total_general:,} CLP")
    print(f"CATEGORÍAS ÚNICAS: {categorias_unicas}")