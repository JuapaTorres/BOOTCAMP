#Crear sistema de reservas de cine con:
# tipos de clientes: 
#regular 10% descuento
#estudiante 20% descuento
#jubilado 30% descuento
#normal no hay descuento
#Cuantas condiciones evalua el problema?
#Que estructura condicional ayudara?
#Cómo evito repetir código?
#Que pasara si el usuario no es valido?


#print("Reserva de cine")
#precio_base = 100
#tipo_cliente = input("Ingrese tipo de cliente:(Regular, Estudiante, Jubilado, Normal): ").lower()

#if tipo_cliente == "regular":
#    descuento = precio_base - (precio_base*0.10)
#    print(f"El monto a pagar es: {descuento}")
#elif tipo_cliente == "estudiante":
#    descuento = precio_base - (precio_base*0.20) 
#    print(f"El monto a pagar es: {descuento}")
#elif tipo_cliente == "jubilado":
#    descuento = precio_base - (precio_base*0.30)
#    print(f"El monto a pagar es: {descuento}") 
#elif tipo_cliente == "normal":
#    print(f"El monto a pagar es: {precio_base}")
#else:
#    print("Cliente no reconocido")

# =====Condicional anidado=====
#entrada = input("Desea comprar entrada? si/no: ").lower()
#precio = 5000

#if entrada == "si":
#print(f"Precio de la entrada: {precio}")
#comprar = input("Desea comprar la entrada? si/no?").lower()
#if comprar == "si":
#   print("La entrada ha sido comprada")
#else:
#   print("Se ha cancelado la compra")
#else:
#   print("Gracias por su visita")
#===============

#opcion = input("Ingrese un animal: ").lower()

#match opcion:
#    case "perro":
#        print("guau")
#    case "gato":
#        print("miau")
#    case "pato":
#        print("cuak")
#    case _:
#        print("No se que sonido hace ese animal")


#Crear un programa que evalua el precio de un producto y devuelva el monto:
#1. Precio del producto con iva
#2. Precio del producto con iva más descuento
#3. Mostrar solo el iva


# precio_base = float(input("Ingrese precio de producto: "))

# print("Opciones")
# print("1. Precio con IVA")
# print("2. Precio con IVA y descuento")
# print("3. Sólo el IVA")

# iva = 0.19
# descuento = 0.15

# opcion = input("Seleccione una opción (1,2 o 3):")

# match opcion:
#    case "1":
#        resultado = precio_base * (1 + iva)
#        print(f"El precio con IVA es: {resultado:.2f}")
#
#    case "2":
#        precio_iva = precio_base *(1 + iva)
#        resultado = precio_iva * (1 - descuento)
#        print(f"El precio con IVA y descuento es: {resultado:.2f}")
#
#    case "3":
#        resultado = precio_base * iva
#        print(f"El monto IVA es de: {resultado:.2f}")
#
#    case _:
#        print("Error opción inválida!")








