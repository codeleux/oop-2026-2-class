class ExpressionCalculator:
    def __init__(self, initial_x, initial_y):
        self.suma = 0
        self.x = initial_x
        self.y = initial_y

    def calculate(self):
        self.suma = self.suma + self.x
        self.x = self.x + self.y**2
        self.suma = self.suma + self.x / self.y
        return self.suma


calc = ExpressionCalculator(20, 40)
resultado = calc.calculate()

print(f"El valor de la suma es:ç {resultado}")