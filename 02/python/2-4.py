import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculateArea(self):
        return math.pi * (self.radius ** 2)

    def calculatePerimeter(self):
        return 2 * math.pi * self.radius

    def showInfo(self):
        print(f'Círculo - Radio: {self.radius} cm')
        print(f'Área: {self.calculateArea():.2f} cm^2')
        print(f'Perímetro: {self.calculatePerimeter():.2f} cm\n')

class Rectangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def calculateArea(self):
        return self.base * self.height

    def calculatePerimeter(self):
        return 2 * (self.base + self.height)

    def showInfo(self):
        print(f'Rectángulo - Base: {self.base} cm, Altura: {self.height} cm')
        print(f'Área: {self.calculateArea():.2f} cm^2')
        print(f'Perímetro: {self.calculatePerimeter():.2f} cm\n')

class Square:
    def __init__(self, side: float):
        self.side = side

    def calculateArea(self):
        return self.side ** 2

    def calculatePerimeter(self):
        return 4 * self.side

    def showInfo(self):
        print(f'Cuadrado - Lado: {self.side} cm')
        print(f'Área: {self.calculateArea():.2f} cm^2')
        print(f'Perímetro: {self.calculatePerimeter():.2f} cm\n')

class RightTriangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def calculateArea(self):
        return (self.base * self.height) / 2

    def calculateHypotenuse(self):
        return math.sqrt(self.base ** 2 + self.height ** 2)

    def calculatePerimeter(self):
        return self.base + self.height + self.calculateHypotenuse()

    def getTriangleType(self):
        hypotenuse = self.calculateHypotenuse()
        if self.base == self.height == hypotenuse:
            return 'Equilátero'
        elif self.base == self.height or self.base == hypotenuse or self.height == hypotenuse:
            return 'Isósceles'
        else:
            return 'Escaleno'

    def showInfo(self):
        print(f'Triángulo Rectángulo - Base: {self.base} cm, Altura: {self.height} cm')
        print(f'Hipotenusa: {self.calculateHypotenuse():.2f} cm')
        print(f'Área: {self.calculateArea():.2f} cm^2')
        print(f'Perímetro: {self.calculatePerimeter():.2f} cm')
        print(f'Tipo de triángulo: {self.getTriangleType()}\n')

def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    square = Square(4)
    triangle = RightTriangle(3, 4)

    circle.showInfo()
    rectangle.showInfo()
    square.showInfo()
    triangle.showInfo()

main()