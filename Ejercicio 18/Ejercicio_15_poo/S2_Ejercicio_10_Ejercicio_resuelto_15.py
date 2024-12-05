#S2_Ejercicio_10_Ejercicio_resuelto_15

PESO1 = int(input("Ingrese el peso de la esfera A: "))
PESO2 = int(input("Ingrese el peso de la esfera B: "))
PESO3 = int(input("Ingrese el peso de la esfera C: "))
PESO4 = int(input("Ingrese el peso de la esfera D: "))


if (PESO1 == PESO2) and (PESO1 == PESO3):
    if PESO4 > PESO1:
        print("LA ESFERA D ES LA DIFERENTE Y ES DE MAYOR PESO")
    else:
        print("LA ESFERA D ES LA DIFERENTE Y ES DE MENOR PESO")
elif (PESO1 == PESO2) and (PESO1 == PESO4):
    print("LA ESFERA C ES LA DIFERENTE")
    if PESO3 > PESO1:
        print("Y ES DE MAYOR PESO")
    else:
        print("Y ES DE MENOR PESO")
elif (PESO1 == PESO3) and (PESO1 == PESO4):
    print("LA ESFERA B ES LA DIFERENTE")
    if PESO2 > PESO4:
        print("Y ES DE MAYOR PESO")
    else:
        print("Y ES DE MENOR PESO")
else:
    print("LA ESFERA A ES LA DIFERENTE")
    if PESO1 > PESO2:
        print("Y ES DE MAYOR PESO")
    else:
        print("Y ES DE MENOR PESO")