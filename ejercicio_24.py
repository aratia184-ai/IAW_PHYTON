cantidad = int(input("¿Qué números quieres saber? "))

mayores_que_cero = 0
menores_que_cero = 0
iguales_a_cero = 0

for i in range(cantidad):
    numero = int(input("Introduce un número: "))

    if numero > 0:
        mayores_que_cero += 1
    elif numero < 0:
        menores_que_cero += 1
    else:
        iguales_a_cero += 1

print("Números mayores que 0:", mayores_que_cero)
print("Números menores que 0:", menores_que_cero)
print("Números iguales a 0:", iguales_a_cero)
