parcial1 = float(input("Nota del primer parcial: "))
parcial2 = float(input("Nota del segundo parcial: "))
parcial3 = float(input("Nota del tercer parcial: "))
examenFinal = float(input("Nota del examen final: "))
trabajoFinal = float(input("Nota del trabajo final: "))
promedioParciales = (parcial1 + parcial2 + parcial3) / 3
notaFinal = (promedioParciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
print("La calificación final es:", round(notaFinal, 2))
