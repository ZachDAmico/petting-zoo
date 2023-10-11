from datetime import date
from .animal import Animal


class Llama(Animal):

    # this is class definition
    def __init__(self, name, species, shift, food, chip_num):
        # Establish the properties of each animal
        # with a default value
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    # def feed(self):
    #     print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self) -> str:
        return f"{self.name} the {self.species}"
# The walking attribute was not added to Animal, but instead stays on Llama. Why? It's not unique to Llama, right? True, but because it's not a property shared by all critters in our system, it doesn't belong on Animal
