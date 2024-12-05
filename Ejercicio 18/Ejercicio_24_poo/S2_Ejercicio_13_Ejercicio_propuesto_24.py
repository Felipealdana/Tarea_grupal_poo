#S2_Ejercicio_13_Ejercicio_propuesto_24
# Ingrese los pesos de las esferas
pesoa = float(input("Ingrese el peso de la esfera A: "))
pesob = float(input("Ingrese el peso de la esfera B: "))
pesoc = float(input("Ingrese el peso de la esfera C: "))
# Inicializar una variable para almacenar el peso máximo
peso_maximo = 0
# Comparar los pesos de las esferas para encontrar la más pesada
if pesoa > pesob and pesoa > pesoc:
    peso_maximo = pesoa
    esfera_maxima = "A"
elif pesob > pesoa and pesob > pesoc:
    peso_maximo = pesob
    esfera_maxima = "B"
else:
    peso_maximo = pesoc
    esfera_maxima = "C"
# Va a mostrar en pantalla la respuesta de la esfera de mayor peso
print(f"La esfera de mayor peso es la esfera {esfera_maxima} con un peso de {peso_maximo} unidades.")