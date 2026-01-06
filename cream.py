from cosmetic import Cosmetic

class Cream(Cosmetic):
    def __init__(self, name: str, viscosity: float):
        super().__init__(name)
        self.viscosity = viscosity

    def moisturize(self) -> str:
        return 'You apply the ' + self.name + ' with a viscosity value of ' + str(self.viscosity)
        