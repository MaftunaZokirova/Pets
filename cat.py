class Cat:
    def __init__(self, name: str, age: int, color: str) -> None:
        self.name = name
        self.age = age
        self.color = color

    def Pet(self) -> str:
        return self.name + " meows"