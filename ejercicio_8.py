sueldobase = float(input("El sueldo base del vendedor es: "))
venta1 = float(input("La primera venta ha sido de: "))
venta2 = float(input("La segunda venta ha sido de: "))
venta3 = float(input("La tercera venta ha sido de: "))
comision = (venta1 + venta2 + venta3) * 0.10
sueldototal = sueldobase + comision
print(f"En comisiones, el vendedor ha ganado {comision}€, por lo que el sueldo total del vendedor es: {sueldototal}€")
