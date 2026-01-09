from cosmetic import Cosmetic 

class Makeup(Cosmetic): 
    def __init__(self, name: str, shade: str):
        super().__init__(name)
        self.shade = shade

    def blend(self) -> str:
        return f'you blend the {self.name} with {self.shade} shade!' 