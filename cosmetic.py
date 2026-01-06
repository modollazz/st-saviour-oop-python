
class Cosmetic:
    def __init__(self, name: str):
        self.name = name
        self.applied = False

    def apply(self, location: str) -> str:
        if not self.applied:
            self.applied = True
            return 'You apply the ' + self.name + ' to the ' + location + '!'
        else:
            return 'You have already applied the ' + self.name + '!'
        
    def remove(self) -> str:
        if self.applied:
            self.applied = False
            return 'You remove the ' + self.name + '!'
        else:
            return 'You cannot remove the ' + self.name + ' without applying it first!'
    
