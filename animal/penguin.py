from datetime import date
from .animal import Animal
from movements import Walking, Swimming


class Penguin(Animal, Walking, Swimming):
    # def __init__(self, name, species, food, chip_num) -> None:
    #     super().__init__(name, species, food, chip_num)
    #     self.swimming = True
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)

    def run(self):
        print(f"{self} waddles")

    def swim(self):
        print(f"{self} darts through the water")

    def feed(self):
        print(f'{self.name} was slow danced with before being fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    # def feed(self):
    #     print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self) -> str:
        return f"{self.name} the {self.species}"
