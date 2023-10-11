from .attraction import Attraction


class SnakePit(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)
        # self.attraction_name = name
        # self.description = "where you'll find stupendous snakes of all sizes, like"
        # self.animals = list()

    def add_animal_snake_pit(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f"{animal} doesn't belong in the {self.attraction_name} attraction")

    @property
    def last_critter_added(self):
        if self.animals:
            return self.animals[-1]

        return None

    # def add_animal(self, animal):
    #     self.animals.append(animal)
