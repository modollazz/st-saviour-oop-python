from cream import Cream 
class Sunscreen(Cream): 
    def __init__(self,name: str, viscosity: float, spf: int): 
        super().__init__(name, viscosity ) 
        self.spf = spf 