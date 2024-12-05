import math

class Circulo:
    def __init__(self, radio):
        """
        Constructor de la clase Circulo
        :param radio: Parámetro que define el radio de un círculo
        """
        self.radio = radio

    def calcular_area(self):
        """
        Método que calcula y devuelve el área de un círculo como pi
        multiplicado por el radio al cuadrado
        :return: Área de un círculo
        """
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        """
        Método que calcula y devuelve el perímetro de un círculo como la
        multiplicación de pi por el radio por 2
        :return: Perímetro de un círculo
        """
        return 2 * math.pi * self.radio
