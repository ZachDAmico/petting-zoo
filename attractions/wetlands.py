from .attraction import Attraction


class Wetlands(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)
        # self.attraction_name = name
        # self.description = "a serene habitat showcasing a variety of wetland creatures, including"
        # self.animals = list()

    def add_animal_wetlands(self, animal):
        try:
            if animal.swim_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f"{animal} doesn't belong in {self.attraction_name}")

    @property
    def last_critter_added(self):
        if self.animals:
            return self.animals[-1]

        return None

#     @property: This is a decorator in Python that allows you to define a method as a property. In this case, it is used to define the last_critter_added method as a property getter.
# def last_critter_added(self):: This is the definition of the last_critter_added method. It takes one parameter, self, which refers to the instance of the class.
# if self.animals:: This line checks if the animals list of the instance is not empty. The self.animals expression accesses the animals attribute of the instance.
# return self.animals[-1]: If the animals list is not empty, this line returns the last item in the list using negative indexing ([-1]). Negative indexing allows you to access elements from the end of the list. For example, [-1] refers to the last element, [-2] refers to the second-to-last element, and so on.
# else: return None: If the animals list is empty, this line returns None to indicate that no critters have been added yet.
# To summarize, the last_critter_added method is a property getter that returns the last critter added to the animals list of the instance. If the animals list is not empty, it returns the last item in the list. If the animals list is empty, it returns None.

    # def add_animal(self, animal):
    #     self.animals.append(animal)
