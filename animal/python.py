from datetime import date
from .animal import Animal
from movements import Slithering


class Python(Animal, Slithering):
    def __init__(self, name, species, food, chip_num) -> None:
        # super().__init__(name, species, food, chip_num)
        # self.slithering = True
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def feed(self):
        print(f'{self.name} was fed {self.food} after laying on the heatin rock on {date.today().strftime("%m/%d/%Y")} ')

    # def feed(self):
    #     print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self) -> str:
        return f"{self.name} the {self.species}"
