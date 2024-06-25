class Dog:
    def __init__(self, name: str, is_wild: bool, is_puppy: bool) -> None:
        self.name = name
        self.is_wild = is_wild
        self.is_puppy = is_puppy

    def Pet(self) -> str:
        return self.name + "is wild or is puppy?"