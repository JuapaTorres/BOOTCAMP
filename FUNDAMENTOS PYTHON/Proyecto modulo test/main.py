#ARCHIVO PRINCIPAL
#Punto de entrada del Sistema de Gestión de Datos.

#Importación de funciones desde los módulos personalizados
from validaciones import leer_entero, leer_texto
import procesos

def mostrar_menu():
#Muestra las opciones disponibles en la consola para el usuario.
    print("\n" + "="*30)
    print("--- MENÚ PRINCIPAL DEL SISTEMA ---")
    print("="*30)
    print("1. Registrar nuevo producto")
    print("2. Visualizar inventario")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir del programa")

def iniciar_programa():
#Controla el flujo principal mediante un bucle infinito hasta que el usuario decida salir.
    while True:
        mostrar_menu()
        #Validación de la opción elegida
        opcion = leer_entero("Seleccione una opción: ")

        if opcion == 1:
            #Captura de información del usuario
            nombre = input("Ingrese nombre del producto: ")
            categoria = input("Ingrese categoría: ")
            stock = leer_entero("Ingrese cantidad de stock: ")
            precio = leer_entero("Ingrese precio unitario (CLP): ")
            procesos.agregar_producto(nombre, stock, precio, categoria) #Procesamiento de la información
            
        elif opcion == 2:
            #Visualización de datos procesados
            procesos.mostrar_inventario()
            
        elif opcion == 3:
            nombre_b = leer_texto("Ingrese nombre a buscar: ")
            procesos.buscar_producto(nombre_b)

        elif opcion == 4:
            nombre_e = leer_texto("Ingrese nombre a eliminar: ")
            procesos.eliminar_producto(nombre_e)

        elif opcion == 5:
            #Detiene el ciclo usando break
            print("Saliendo del sistema... ¡Gracias por utilizar nuestra gestión!")
            break
        else:
            #En caso de que se ingrese una opción no válida, mensaje para vovler a elegir.
            print(f"La opción {opcion} no es válida. Por favor, elija entre 1 y 5.")

#Asegura que el programa solo se ejecute si este archivo es el principal.
if __name__ == "__main__":
    iniciar_programa()