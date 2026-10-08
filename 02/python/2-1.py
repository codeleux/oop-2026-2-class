class Person: 
    def __init__(self, name: str, lastName: str, id: str, birthYear: int):
        self.name = name
        self.lastName = lastName
        self.id = id
        self.birthYear = birthYear

    def showInfo(self):
        print(f'Nombre: {self.name}')
        print(f'Apellido: {self.lastName}')
        print(f'Documento: {self.id}')
        print(f'Año de nacimiento: {self.birthYear}\n')

def main():
    person1 = Person('Juan', 'Rodriguez', '1839012803', 2002)
    person2 = Person('Ana', 'Rodriguez', '102938190', 2006)

    person1.showInfo()
    person2.showInfo()

main()