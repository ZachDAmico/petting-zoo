from datetime import date
from .animal import Animal


class Anaconda(Animal):
    def __init__(self, name, species, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    # @property
    # def chip_number(self):
    #     return self.__chip_number

    # @chip_number.setter
    # def chip_number(self, number):
    #     pass

    # def feed(self):
    #     print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self) -> str:
        return f"{self.name} the {self.species}"
