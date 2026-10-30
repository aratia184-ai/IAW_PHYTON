numero = int(input("Pon un número (0 para terminar): "))
suma = 0
cantidad = 0

while numero != 0:
    suma += numero
    cantidad += 1
    numero = int(input("Pon un número (0 para terminar): "))

print("La suma es:", suma)

if cantidad > 0:
    media = suma / cantidad
    print("La media es:", media)
else:
    print("No hay números para calcular la media.")
