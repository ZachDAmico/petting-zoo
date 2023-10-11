from datetime import date
from .animal import Animal


class Donkey(Animal):
    def __init__(self, name, species, shift, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    # def feed(self):
    #     print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self) -> str:
        return f"{self.name} the {self.species}"
