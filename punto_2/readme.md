# Proyecto Figuras Geométricas

Este proyecto contiene una librería de Python llamada `figuras`, que incluye clases para representar diferentes figuras geométricas: Círculo, Cuadrado, Rectángulo y Triángulo Rectángulo. Cada clase tiene métodos para calcular el área y el perímetro de la figura correspondiente.

Además, se incluye un archivo de prueba `prueba_figuras.py` donde se testean las funcionalidades de cada clase.

## Estructura del Proyecto

La estructura de carpetas del proyecto es la siguiente:

figuras/ │ ├── init.py # Archivo de inicialización para el paquete ├── circulo.py # Clase para representar un círculo ├── cuadrado.py # Clase para representar un cuadrado ├── rectangulo.py # Clase para representar un rectángulo └── triangulo_rectangulo.py # Clase para representar un triángulo rectángulo │ prueba_figuras.py # Archivo de prueba para testear las clases


### Descripción de los Archivos

#### `figuras/__init__.py`
Este archivo marca el directorio `figuras` como un paquete de Python, permitiendo importar las clases y utilizarlas en otros scripts.

#### `figuras/circulo.py`
Contiene la clase `Círculo`, que tiene un atributo `radio` y métodos para calcular el área y el perímetro del círculo.

#### `figuras/cuadrado.py`
Contiene la clase `Cuadrado`, que tiene un atributo `lado` y métodos para calcular el área y el perímetro del cuadrado.

#### `figuras/rectangulo.py`
Contiene la clase `Rectángulo`, que tiene los atributos `base` y `altura`, y métodos para calcular el área y el perímetro del rectángulo.

#### `figuras/triangulo_rectangulo.py`
Contiene la clase `TriánguloRectángulo`, que tiene los atributos `base` y `altura`, y métodos para calcular el área, el perímetro y determinar el tipo de triángulo (equilátero, isósceles o escaleno).

#### `prueba_figuras.py`
Este archivo sirve para probar el funcionamiento de las clases definidas en el paquete `figuras`. En él se crean instancias de las diferentes figuras y se llaman a sus métodos para comprobar que devuelven los resultados esperados.

## Instalación

Clona o descarga este repositorio en tu máquina local.

