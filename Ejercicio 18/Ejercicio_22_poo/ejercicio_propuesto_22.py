nombre = input("Ingrese su Nombre ")
salario_basic = float(input("Ingrese su Salario "))
horas_trabajadas = float(input("Ingrese las horas trabajadas en el mes "))
salario_mensual = salario_basic * horas_trabajadas


if salario_mensual > 450000:
  print("Su nombre es " + nombre + " y su salario mensual es " + str(salario_mensual))
else:
  print ("Su nombre es " + nombre)