from enum import Enum

class FuelType(Enum):
    gasoline = "Gasolina"
    bioethanol = "Bioetanol"
    diesel = "Diésel"
    biodiesel = "Biodiésel"
    natural_gas = "Gas natural"


class CarType(Enum):
    city_car = "Carro de ciudad"
    subcompact = "Subcompacto"
    compact = "Compacto"
    family = "Familiar"
    executive = "Ejecutivo"
    suv = "SUV"


class Color(Enum):
    white = "Blanco"
    black = "Negro"
    red = "Rojo"
    orange = "Naranja"
    yellow = "Amarillo"
    green = "Verde"
    blue = "Azul"
    violet = "Violeta"


class Car:
    def __init__(
        self,
        brand: str,
        model: int,
        engineSize: float,
        fuelType: FuelType,
        carType: CarType,
        doorsQuantity: int,
        seatsQuantity: int,
        maxSpeed: int,
        color: Color,
        currentSpeed: int = 0,
    ):
        self.brand = brand
        self.model = model
        self.engineSize = engineSize
        self.fuelType = fuelType
        self.carType = carType
        self.doorsQuantity = doorsQuantity
        self.seatsQuantity = seatsQuantity
        self.maxSpeed = maxSpeed
        self.color = color
        self.currentSpeed = currentSpeed

    def getBrand(self):
        return self.brand

    def setBrand(self, brand: str):
        self.brand = brand

    def getModel(self):
        return self.model

    def setModel(self, model: int):
        self.model = model

    def getEngineSize(self):
        return self.engineSize

    def setEngineSize(self, engineSize: float):
        self.engineSize = engineSize

    def getFuelType(self):
        return self.fuelType

    def setFuelType(self, fuelType: FuelType):
        self.fuelType = fuelType

    def getCarType(self):
        return self.carType

    def setCarType(self, carType: CarType):
        self.carType = carType

    def getDoorsQuantity(self):
        return self.doorsQuantity

    def setDoorsQuantity(self, doorsQuantity: int):
        self.doorsQuantity = doorsQuantity

    def getSeatsQuantity(self):
        return self.seatsQuantity

    def setSeatsQuantity(self, seatsQuantity: int):
        self.seatsQuantity = seatsQuantity

    def getMaxSpeed(self):
        return self.maxSpeed

    def setMaxSpeed(self, maxSpeed: int):
        self.maxSpeed = maxSpeed

    def getColor(self):
        return self.color

    def setColor(self, color: Color):
        self.color = color

    def getCurrentSpeed(self):
        return self.currentSpeed

    def setCurrentSpeed(self, currentSpeed: int):
        if currentSpeed < 0:
            print('No se puede colocar una velocidad negativa.')
        elif currentSpeed > self.maxSpeed:
            print('No se puede superar la velocidad máxima del automóvil.')
        else:
            self.currentSpeed = currentSpeed

    def accelerate(self, speedIncrement: int):
        if self.currentSpeed + speedIncrement > self.maxSpeed:
            print(f'No se puede acelerar a {self.currentSpeed + speedIncrement} km/h. Supera la velocidad máxima permitida de {self.maxSpeed} km/h.')
        else:
            self.currentSpeed += speedIncrement

    def decelerate(self, speedDecrement: int):
        if self.currentSpeed - speedDecrement < 0:
            print('No se puede desacelerar a una velocidad negativa.')
        else:
            self.currentSpeed -= speedDecrement

    def brake(self):
        self.currentSpeed = 0

    def calculateEstimatedTime(self, distanceKm: float):
        if self.currentSpeed == 0:
            print('El automóvil está detenido. No se puede calcular el tiempo de llegada.')
            return 0.0
        return distanceKm / self.currentSpeed

    def showInfo(self):
        print(f'Marca: {self.brand}')
        print(f'Modelo: {self.model}')
        print(f'Motor: {self.engineSize} L')
        print(f'Tipo de combustible: {self.fuelType.value}')
        print(f'Tipo de automóvil: {self.carType.value}')
        print(f'Número de puertas: {self.doorsQuantity}')
        print(f'Cantidad de asientos: {self.seatsQuantity}')
        print(f'Velocidad máxima: {self.maxSpeed} km/h')
        print(f'Color: {self.color.value}')
        print(f'Velocidad actual: {self.currentSpeed} km/h\n')

def main():
    car = Car(
        brand='Toyota',
        model=2023,
        engineSize=2.0,
        fuelType=FuelType.gasoline,
        carType=CarType.compact,
        doorsQuantity=4,
        seatsQuantity=5,
        maxSpeed=180,
        color=Color.red,
    )

    car.showInfo()

    car.setCurrentSpeed(100)
    print(f'Velocidad actual tras fijar en 100 km/h: {car.getCurrentSpeed()} km/h')

    car.accelerate(20)
    print(f'Velocidad actual tras acelerar 20 km/h: {car.getCurrentSpeed()} km/h')

    car.decelerate(50)
    print(f'Velocidad actual tras desacelerar 50 km/h: {car.getCurrentSpeed()} km/h')

    car.brake()
    print(f'Velocidad actual tras frenar: {car.getCurrentSpeed()} km/h')

main()