#Tipos de datos

#entero = 10 #Pueden ser positivos o negativos (int)
#flotante = 10.0 #Pueden ser positivos o negativos (float)
#booleanos = True o False (binario 0 y 1) (bool)
#cadena = '' o "" cadena o string entre comillas, puede ser texto, símbolos y números. siempre dentro de las comillas. (str)

#Para confirmar el tipo de dato se usa type ej: print(type(insertar variable)) En terminal.

#Cadenas
# nombre = "Juan-Pablo"
# apellido = "Torres"
# nombre_completo = nombre + " " + apellido #concatenación
# print(nombre_completo)

# Variables
# suma = 10 + 20 #Expresión
# resta = 10 - 10 
# print(id(suma))
# print(id(resta))
# id para ver el identificador
# las variables se pueden reasignar


#Operadores aritméticos
# suma = 10 + 20
# resta = 10 - 20
# division = 10 / 2
# multiplicacion = 10 * 3
# division_entera = 10 // 2
# modulo = 10 % 2 #Resultado del resto o lo que sobra de una división
# potenciacion = 10 ** 2

# resultado = 10 + 6 / 2 * (3 + 7)
# print(resultado)


#Operadores de comparación
# numero1 = 20
# numero2 = 30
# print(numero1 == numero2)  < menor > mayor


#Operadores lógicos
# numero1 = 10
# numero2 = 20
# numero3 = 30

#print(numero1<numero2 and numero2>numero3 ) # Operador and, todas las comparaciones deben ser true para que devuelva true
#print(numero1<numero2 or numero2>numero3 ) # Operador or, al menos una debe ser true para que devuelva true

#Operadores de asignación
# edad = 18 
# print("Tienes", edad, "años")
# print("Ha pasado un año")
#edad = edad + 1
# edad += 1
# print("Tienes", edad, "años")
# print("Nos volvemos un año")
# edad -= 1
# print("Tienes", edad, "años")

# nombre = input("Ingrese su nombre:")
# print("Hola",nombre)


#Conversión o casteo

# edad = input("Ingrese su edad:")
# edad = int(edad)
# print("Tu edad es:",edad)

# Casteo implicito, lo realiza python
# Casteo explicito, lo realiza el programador


#print("Vamos a calcular el promedio")
#nota1 = input("Ingrese nota 1:")
#nota1 = int(nota1)
#nota2 = input("ingrese nota 2:")
#nota2 = int(nota2)
#nota3 = input("Ingrese nota 3:")
#nota3 = int(nota3)
#promedio = nota1 + nota2 + nota3
#promedio_final = promedio / 3
#print(f"El promedio es, {promedio_final:.2f}")


#Calcular el área de un cuadrado, triangulo y círculo ... TAREA SÁBADO
# triangulo = base * altura / 2
# cuadrado = lado**2
# circulo = pi * r**2


print("Vamos a calcular el área de varias figuras: ")
print("Empezamos por el triángulo,")
base_triangulo = input("Cuánto mide la base?, Ingresalo: ")
base_triangulo = int(base_triangulo)
altura_triangulo = input("Ahora, cuánto mide la altura?, Ingresalo: ")
altura_triangulo = int(altura_triangulo)
area_triangulo = base_triangulo * altura_triangulo / 2
print(f"El área del triangulo es: {area_triangulo:.2f}")
print("Ahora vamos por el cuadrado,")
lado_cuadrado = input("Cuánto mide el lado del cuadrado?, Ingresalo: ")
lado_cuadrado = int(lado_cuadrado)
area_cuadrado = lado_cuadrado ** 2
print(f"El área del cuadrado es: {area_cuadrado:.2f}")
print("Finalmente vamos por el círculo,")
radio_circulo = input("Cuánto es el radio del círculo?, Ingresalo: ")
radio_circulo = int(radio_circulo)
area_circulo = 3.14 * radio_circulo ** 2
print(f"El área del círculo es: {area_circulo:.2f}")

