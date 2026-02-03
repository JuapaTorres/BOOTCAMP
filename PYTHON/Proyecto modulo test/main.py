#ARCHIVO PRINCIPAL
#Punto de entrada del Sistema de Gestión de Datos.

#Importación de funciones desde los módulos personalizados
from validaciones import leer_entero
import procesos

def mostrar_menu():
#Muestra las opciones disponibles en la consola.
    print("--- MENÚ PRINCIPAL DEL SISTEMA ---")
    print("1. Registrar nuevo producto")
    print("2. Visualizar inventario")
    print("3. Salir del programa")

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
            
            #Procesamiento de la información
            procesos.agregar_producto(nombre, stock, precio, categoria)
            
        elif opcion == 2:
            #Visualización de datos procesados
            procesos.mostrar_inventario()
            
        elif opcion == 3:
            #Detiene el ciclo usando break
            print("Saliendo del sistema... ¡Gracias por utilizar nuestra gestión!")
            break
        else:
            #En caso de que se ingrese una opción no válida, mensaje para vovler a elegir.
            print(f"La opción {opcion} no es válida. Por favor, elija entre 1 y 3.")

#Asegura que el programa solo se ejecute si este archivo es el principal.
if __name__ == "__main__":
    iniciar_programa()