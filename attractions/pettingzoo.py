from .attraction import Attraction
from movements import Walking


class PettingZoo(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

        # self.attraction_name = name
        # self.description = "cute and fuzzy critters to cuddle"
        # self.animals = list()
    def add_animal_pythonic(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(
                f'{animal} doesn\'t like to be pet, so please do not put it in the {self.attraction_name} attraction.')

    @property
    def last_critter_added(self):
        if self.animals:
            return self.animals[-1]

        return None

    # def add_animal(self, animal):
    #     self.animals.append(animal)
