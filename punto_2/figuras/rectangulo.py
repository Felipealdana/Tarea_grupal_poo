class Rectangulo:
    def __init__(self, base, altura):
        """
        Constructor de la clase Rectangulo
        :param base: Parámetro que define la base de un rectángulo
        :param altura: Parámetro que define la altura de un rectángulo
        """
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """
        Método que calcula y devuelve el área de un rectángulo
        :return: Área de un rectángulo
        """
        return self.base * self.altura

    def calcular_perimetro(self):
        """
        Método que calcula y devuelve el perímetro de un rectángulo
        :return: Perímetro de un rectángulo
        """
        return (2 * self.base) + (2 * self.altura)
