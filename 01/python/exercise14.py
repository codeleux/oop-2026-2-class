class Operations:
    @staticmethod
    def squared(num):
        return num**2

    @staticmethod
    def cubed(num):
        return num**3

input = int(input('Escriba un número: '))
squaredNum = Operations.squared(input)
cubedNum = Operations.cubed(input)

print(f'{input}^2 = {squaredNum}')
print(f'{input}^3 = {cubedNum}')

