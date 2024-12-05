import math

class TrianguloRectangulo:
    def __init__(self, base, altura):
        """
        Constructor de la clase TrianguloRectangulo
        :param base: Parámetro que define la base de un triángulo rectángulo
        :param altura: Parámetro que define la altura de un triángulo rectángulo
        """
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """
        Método que calcula y devuelve el área de un triángulo rectángulo
        :return: Área de un triángulo rectángulo
        """
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        """
        Método que calcula y devuelve la hipotenusa de un triángulo rectángulo
        usando el teorema de Pitágoras
        :return: Hipotenusa del triángulo rectángulo
        """
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def calcular_perimetro(self):
        """
        Método que calcula y devuelve el perímetro de un triángulo rectángulo
        como la suma de la base, la altura y la hipotenusa
        :return: Perímetro de un triángulo rectángulo
        """
        return self.base + self.altura + self.calcular_hipotenusa()
    
    def determinar_tipo_triangulo(self):
        """
        Método que determina el tipo de triángulo rectángulo en función de sus lados.
        Determina si el triángulo es equilátero, escaleno o isósceles.
        """
        hipotenusa = self.calcular_hipotenusa()

        # Verifica si el triángulo es equilátero (aunque esto no es común para triángulos rectángulos)
        if self.base == self.altura == hipotenusa:
            print("Es un triángulo equilátero")  # Todos sus lados son iguales
        # Verifica si el triángulo es escaleno (todos sus lados son diferentes)
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            print("Es un triángulo escaleno")  # Todos sus lados son diferentes
        else:
            # Si no es equilátero ni escaleno, es isósceles
            print("Es un triángulo isósceles")  # Tiene dos lados iguales
