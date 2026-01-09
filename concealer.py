from makeup import Makeup 
class Concealer(Makeup):   
    def __init__( self, name: str, shade: str, brightness : int  ):
        super().__init__(name, shade) 
        self.brightness = brightness 
