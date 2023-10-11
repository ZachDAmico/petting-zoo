from datetime import date
from .animal import Animal
from movements import Swimming


class Goldfish(Animal, Swimming):
    # def __init__(self, name, species, food, chip_num) -> None:
    #     super().__init__(name, species, food, chip_num)
    #     self.swimming = True

    def __init__(self, name, species, food, chip_num) -> None:
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)

    # def feed(self):
    #     print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self) -> str:
        return f"{self.name} the {self.species}"
