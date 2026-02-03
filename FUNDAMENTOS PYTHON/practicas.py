while True:

    edad = int(input("Ingresa tu edad: "))

    if edad < 0:
        print("Error: La edad no puede ser negativa. Intenta de nuevo.")
    else:
        break

if edad >= 18:
    print("Eres mayor de edad")

else:
    print("Eres menor de edad")

