cantidadMinutos = int(input("Escribe la cantidad de minutos que deseas convertir: "))
cantidadHoras = cantidadMinutos // 60
cantidadMinutosRestantes = cantidadMinutos % 60
print(f"{cantidadMinutos} minutos son {cantidadHoras} horas y {cantidadMinutosRestantes} minutos.")
