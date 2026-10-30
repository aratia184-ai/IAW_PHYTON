import random

numero_secreto = random.randint(1, 100)
intentos_maximos = 10
intentos = 0

print("Se ha generado un número del 1 al 100, 10 intentos para adivinarlo.")

while intentos < intentos_maximos:
    try:
        numero = int(input("Introduce un número: "))
    except ValueError:
        print("Debes introducir un número entero.")
        continue

    if numero < 1 or numero > 100:
        print("El número debe estar entre 1 y 100.")
        continue

    intentos += 1

    if numero == numero_secreto:
        print(f"¡Correcto! Has acertado en {intentos} intento/s.")
        break

    if numero < numero_secreto:
        print("El número que tienes que adivinar es mayor.")
    else:
        print("El número que tienes que adivinar es menor.")

    intentos_restantes = intentos_maximos - intentos
    print(f"Te quedan {intentos_restantes} intento(s).")
else:
    print(f"Se han agotado los intentos. El número era {numero_secreto}.")
