#S2_Ejercicio_12_Ejercicio_propuesto_23
import math
# Ingrese los coeficientes de la ecuación cuadrática
a = float(input("Ingrese el coeficiente A: "))
b = float(input("Ingrese el coeficiente B: "))
c = float(input("Ingrese el coeficiente C: "))
# Calcular el discriminante (d)
d = b**2 - 4*a*c
# Calcular las soluciones de la ecuación
if d > 0:
    # Dos soluciones reales distintas
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Las soluciones son:")
    print("x1 =", x1)
    print("x2 =", x2)
elif d == 0:
    # Una solución real única
    x1 = -b / (2*a)
    print("La solución única es:")
    print("x1 =", x1)
else:
    # Soluciones complejas
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(-d) / (2*a)
    print("No tiene soluciones reales y las soluciones complejas son:")
    print(f"x1 = {realPart} + {imaginaryPart}i")
    print(f"x2 = {realPart} - {imaginaryPart}i")