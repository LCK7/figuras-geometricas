"""
Módulo que define una jerarquía de clases para representar figuras geométricas
y calcular sus áreas. Incluye figuras como el rectángulo, triángulo y círculo.
"""

from abc import ABC, abstractmethod
import math


class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para figuras geométricas."""

    @abstractmethod
    def calcular_area(self):
        """Calcula el área de la figura."""

    @abstractmethod
    def describir(self):
        """Devuelve una descripción de la figura."""


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo."""

    def __init__(self, base, altura):
        """Inicializa las dimensiones del rectángulo."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura

    def describir(self):
        """Devuelve una descripción del rectángulo."""
        return f"Rectángulo de base {self.base} y altura {self.altura}"

    def es_cuadrado(self):
        """Determina si el rectángulo es un cuadrado."""
        return self.base == self.altura


class Triangulo(FiguraGeometrica):
    """Clase que representa un triángulo."""

    def __init__(self, base, altura):
        """Inicializa las dimensiones del triángulo."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2

    def describir(self):
        """Devuelve una descripción del triángulo."""
        return f"Triángulo de base {self.base} y altura {self.altura}"


class Circulo(FiguraGeometrica):
    """Clase que representa un círculo."""

    def __init__(self, radio):
        """Inicializa el radio del círculo."""
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return math.pi * (self.radio ** 2)

    def describir(self):
        """Devuelve una descripción del círculo."""
        return f"Círculo de radio {self.radio}"

    def calcular_circunferencia(self):
        """Calcula la circunferencia del círculo."""
        return 2 * math.pi * self.radio


# Constantes para las figuras de ejemplo
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3

if __name__ == "__main__":
    # Crear instancias de figuras
    figuras = [
        Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO),
        Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO),
        Circulo(RADIO_CIRCULO)
    ]

    # Mostrar información de cada figura
    for figura in figuras:
        print(figura.describir())
        print(f"Área: {figura.calcular_area():.2f}")

        print()
