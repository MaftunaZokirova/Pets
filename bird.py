class Bird:
    def __init__(self, type: str, name: str, can_fly: bool) -> None:
        self.type = type
        self.name = name
        self.can_fly = can_fly


    def Pet(self) -> str:
        return self.name + " Kuu Kuu"
        
    