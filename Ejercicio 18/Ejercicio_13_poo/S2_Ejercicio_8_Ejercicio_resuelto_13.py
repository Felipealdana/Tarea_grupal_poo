
#S2_Ejercicio_8_Ejercicio_resuelto_13
VALORCOMP = float(input("Ingrese el valor de la compra: "))
COLOR = input("Ingrese el color de la bolita (BLANCO, VERDE, AMARILLO, AZUL): ").upper() #el upper() sirve por si la persona ingresa el valor en minúscula cambie a mayúscula. 
# Inicializar el porcentaje de descuento
PDESC = 0
# Calcular el porcentaje de descuento según el color de la bolita
if COLOR == "BLANCO":
    PDESC = 0
elif COLOR == "VERDE":
    PDESC = 10
elif COLOR == "AMARILLO":
    PDESC = 25
elif COLOR == "AZUL":
    PDESC = 50
else:
    PDESC = 100
VALORPAG = VALORCOMP - (PDESC * VALORCOMP / 100) # Calcular el valor a pagar con el descuento
print(f"EL CLIENTE DEBE PAGAR: ${VALORPAG}")