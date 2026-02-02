from validaciones import leer_entero
import procesos

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN TECNOLÓGICA ---")
    print("1. Registrar producto")
    print("2. Ver inventario")
    print("3. Salir")

def iniciar_programa():
    while True:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opción: ")

        if opcion == 1:
            nombre = input("Nombre del producto: ")
            stock = leer_entero("Cantidad en stock: ")
            precio = leer_entero("Precio por unidad: ")
            # Reutilizamos leer_entero o creamos leer_float después
            
            # Llamamos a la función del módulo procesos
            procesos.agregar_producto(nombre, stock, precio)
            
        elif opcion == 2:
            procesos.mostrar_inventario()
            
        elif opcion == 3:
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    iniciar_programa()