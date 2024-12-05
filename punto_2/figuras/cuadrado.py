class Cuadrado:
    def __init__(self, lado):
        """
        Constructor de la clase Cuadrado
        :param lado: Parámetro que define la longitud del lado de un cuadrado
        """
        self.lado = lado

    def calcular_area(self):
        """
        Método que calcula y devuelve el área de un cuadrado
        :return: Área de un cuadrado (lado elevado al cuadrado)
        """
        return self.lado ** 2

    def calcular_perimetro(self):
        """
        Método que calcula y devuelve el perímetro de un cuadrado
        :return: Perímetro de un cuadrado (cuatro veces el lado)
        """
        return 4 * self.lado
