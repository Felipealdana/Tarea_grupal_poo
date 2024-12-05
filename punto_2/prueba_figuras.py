from figuras import *

def main():
    figura1 = Circulo(2)
    figura2 = Rectangulo(1, 2)
    figura3 = Cuadrado(3)
    figura4 = TrianguloRectangulo(3, 5)

    print(f"El área del círculo es = {figura1.calcular_area()}")
    print(f"El perímetro del círculo es = {figura1.calcular_perimetro()}")
    print()

    print(f"El área del rectángulo es = {figura2.calcular_area()}")
    print(f"El perímetro del rectángulo es = {figura2.calcular_perimetro()}")
    print()

    print(f"El área del cuadrado es = {figura3.calcular_area()}")
    print(f"El perímetro del cuadrado es = {figura3.calcular_perimetro()}")
    print()

    print(f"El área del triángulo es = {figura4.calcular_area()}")
    print(f"El perímetro del triángulo es = {figura4.calcular_perimetro()}")
    figura4.determinar_tipo_triangulo()

if __name__ == "__main__":
    main()
