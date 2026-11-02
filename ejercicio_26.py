numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

menor = min(numero1, numero2)
mayor = max(numero1, numero2)

for numero in range(menor, mayor + 1):
    if numero % 2 == 0:
        print(numero)
