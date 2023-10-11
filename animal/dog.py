from datetime import date
from .animal import Animal
from movements import Walking


class Dog(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num) -> None:
        # super().__init__(name, species, food, chip_num)
        # self.walking = True
        # self.shift = shift
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)

    def feed(self):
        print(f'{self.name} was given butt scratches on {date.today().strftime("%m/%d/%Y")} before being fed {self.food}')

    # def feed(self):
    #     print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self) -> str:
        return f"{self.name} the {self.species}"
