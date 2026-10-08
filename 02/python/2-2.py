from enum import Enum

class PlanetType(Enum):
    GASEOUS = "GASEOSO"
    TERRESTRIAL = "TERRESTRE"
    DWARF = "ENANO"

class Planet:
    def __init__(
            self,
            name: str = None,
            satellitesQuantity: int = 0,
            massKg: float = 0.0,
            volumeKm3: float = 0.0,
            diameterKm: int = 0,
            averageSunDistanceMkm: int = 0,
            planetType: PlanetType = None,
            isObservable: bool = False,
        ):

        self.name = name
        self.satellitesQuantity = satellitesQuantity
        self.massKg = massKg
        self.volumeKm3 = volumeKm3
        self.diameterKm = diameterKm
        self.averageSunDistanceMkm = averageSunDistanceMkm
        self.planetType = planetType
        self.isObservable = isObservable

    def calculateDensity(self):
        if self.volumeKm3 <= 0:
            return 0.0
        return self.massKg / self.volumeKm3

    def isOuterPlanet(self):
        distanceKm = self.averageSunDistanceMkm * 1000000
        outerLimitKm = 3.4 * 149597870
        return distanceKm > outerLimitKm

    def showInfo(self):
        print(f'Nombre: {self.name}')
        print(f'Cantidad de satélites: {self.satellitesQuantity}')
        print(f'Masa: {self.massKg} kg')
        print(f'Volumen: {self.volumeKm3} km³')
        print(f'Diámetro: {self.diameterKm} km')
        print(f'Distancia media al Sol: {self.averageSunDistanceMkm} millones de km')
        print(f'Tipo de planeta: {self.planetType.value if self.planetType else None}')
        print(f'Observable a simple vista: {"Sí" if self.isObservable else "No"}')
        print(f'Densidad: {self.calculateDensity()}')
        print(f'Es planeta exterior: {"Sí" if self.isOuterPlanet() else "No"}\n')


def main():
    planet1 = Planet(
        name = 'Tierra',
        satellitesQuantity = 1,
        massKg = 1,
        volumeKm3 = 2,
        diameterKm = 5,
        averageSunDistanceMkm = 7,
        planetType = PlanetType.TERRESTRIAL,
        isObservable = True,
    )

    planet2 = Planet(
        name = 'Júpiter',
        satellitesQuantity = 95,
        massKg = 1,
        volumeKm3 = 2,
        diameterKm = 3,
        averageSunDistanceMkm = 5,
        planetType = PlanetType.GASEOUS,
        isObservable = True,
    )
    # valores arbitrariamente escogidos lol
    planet1.showInfo()
    planet2.showInfo()


main()