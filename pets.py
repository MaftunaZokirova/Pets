
# Zokirova Maftuna

from bird import Bird
from cat import Cat
from dog import Dog




class Pets:
    def __init__(self) -> None:
        pass

    def Run(self) -> None:
        my_dog = Dog( "Dollar", True, False)
        my_cat = Cat("Gibby", 6, "Black and White")
        my_bird = Bird("Owel","Scooter", True)
        print(my_dog.Pet())
        print(my_cat.Pet())
        print(my_bird.Pet())

        
    




if __name__ == '__main__': 
    my_pets = Pets()
    my_pets.Run()