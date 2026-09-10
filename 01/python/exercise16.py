import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def circumferenceLenght(self):
        return math.pi * 2 * self.radius

input = int(input("Ingrese el radio del circulo: "))
circle = Circle(input)

print(f'El área del circulo de radio {input} es de {circle.area()}')
print(f'La longitud de la circunferencia del circulo de radio {input} es de {circle.circumferenceLenght()}')