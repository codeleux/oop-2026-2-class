class FamilyAges:
    def __init__(self, juan_age):
        self.juan_age = juan_age

    def alberto_age(self):
        return (2 / 3) * self.juan_age

    def ana_age(self):
        return (4 / 3) * self.juan_age

    def mother_age(self):
        return self.juan_age + self.alberto_age() + self.ana_age()


edad_juan = float(input("Ingrese la edad de Juan: "))

familia = FamilyAges(edad_juan)

print(f"La edad de Juan es: {familia.juan_age}")
print(f"La edad de Alberto es: {familia.alberto_age()}")
print(f"La edad de Ana es: {familia.ana_age()}")
print(f"La edad de la mamá es: {familia.mother_age()}")