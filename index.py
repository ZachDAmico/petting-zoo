
# from slithering import Anaconda, Boa, Cobra, Python, Snake
# from swimming import Clownfish, Dolphin, Goldfish, Penguin, Sea_Turtle
# from walking import Cat, Dog, Donkey, Llama, Rabbit
from animal import Anaconda, Boa, Cobra, Python, Snake, Clownfish, Dolphin, Goldfish, Penguin, Sea_Turtle, Cat, Dog, Donkey, Llama, Rabbit, Goose
from attractions import PettingZoo, SnakePit, Wetlands

varmint_village = PettingZoo(
    "Varmint Village", "critters that like to dig and scurry")
slither_inn = SnakePit(
    "Slither Inn", "where you'll find stupendous snakes of all sizes, like")
serene_swamp = Wetlands(
    "Serene Swamp", "a serene habitat showcasing a variety of wetland creatures, including")


ice_cube = Anaconda("Ice Cube", "jungle anaconda", "humans", 8675309)
# print(ice_cube.feed())
# print(ice_cube)


slither_inn.add_animal(ice_cube)


# move all the instances to index?
bob = Boa("Bob", "boa constrictor", "mice", 890874)
# print(bob.feed())
# print(bob)
slither_inn.add_animal(bob)


johnny = Cobra("Johnny", "king cobra", "mice", 869503)
# print(johnny.feed())
# print(johnny)
slither_inn.add_animal(johnny)


cassis = Python("Cassis", "python", "mice", 660043)
# print(cassis.feed())
# print(cassis)
slither_inn.add_animal(cassis)

sprinkles = Snake("Sprinkles", "garter snake", "mice", 549987)
# print(sprinkles.feed())
# print(sprinkles)
slither_inn.add_animal(sprinkles)


nemo = Clownfish("Nemo", "clownfish", "fish food", 77809)
# print(nemo.feed())
# print(nemo)
serene_swamp.add_animal(nemo)

debbie = Dolphin("Debbie", "dolphin", "fish", 22134)
# print(debbie.feed())
# print(debbie)
serene_swamp.add_animal(debbie)


bubbles = Goldfish("Bubbles", "goldfish", "fish flakes", 89983)
# print(bubbles.feed())
# print(bubbles)

oswald = Penguin("Oswald", "penguin", "fish", 56564)
# print(oswald.feed())
# print(oswald)
serene_swamp.add_animal(oswald)
# oswald.run()
# oswald.swim()


crush = Sea_Turtle("Crush", "sea turtle", "turtle food", 67834)
# print(crush.feed())
# print(crush)
serene_swamp.add_animal(crush)

gerard = Goose("Gerard", "Canadian Goose", "bread", 45672)
varmint_village.add_animal(gerard)
# gerard.run()
# gerard.swim()

klaus = Cat("Klaus", "house cat", "morning", "cat food", 663344)
# print(f'{klaus.name} the {klaus.species} is available to pet during the {klaus.shift} shift')
# print(klaus.feed())
# print(klaus)
varmint_village.add_animal(klaus)

lydi = Dog("Lydi", "pitbull", "midday", "dog food", 21334)
# print(f'{lydi.name} the {lydi.species} is available to pet during the {lydi.shift} shift')
# print(lydi.feed())
# print(lydi)
varmint_village.add_animal(lydi)

eddie = Donkey("Eddie", "talking donkey", "afternoon", "donkey food", 443554)
# print(f'{eddie.name} the {eddie.species} is available to pet during the {eddie.shift} shift')
# print(eddie.feed())
# print(eddie)
varmint_village.add_animal(eddie)

# You should always store the object instance in a variable
miss_fuzz = Llama("Miss Fuzz", "domestic llama",
                  "morning", "llama crunch", 776655)
# print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift')
# print(miss_fuzz.feed())
# print(miss_fuzz)
varmint_village.add_animal(miss_fuzz)

peter = Rabbit("Peter", "rabbit", "midday", "rabbit pellets", 11234)
# print(f'{peter.name} the {peter.species} is available to pet during the {peter.shift} shift')
# print(peter.feed())
# print(peter)
varmint_village.add_animal(peter)

# print(f"{slither_inn.attraction_name} is {slither_inn.description}")
# for animal in slither_inn.animals:
#     print(f"    * {animal.name} the {animal.species}")

# print(f"{serene_swamp.attraction_name} is {serene_swamp.description}")
# for animal in serene_swamp.animals:
#     print(f"    * {animal.name} the {animal.species}")

# print(f"{varmint_village.attraction_name} is {varmint_village.description}")
# for animal in varmint_village.animals:
#     print(f"    * {animal.name} the {animal.species}")

# print(serene_swamp.last_critter_added)

# print(varmint_village.last_critter_added)

# print(slither_inn.last_critter_added)

# print(lydi.feed())
# print(oswald.feed())
# print(cassis.feed())


for animal in varmint_village.animals:
    print(animal)

# for animal in slither_inn.animals:
#     print(animal)

# for animal in serene_swamp.animals:
#     print(animal)

varmint_village.add_animal_pythonic(lydi)
varmint_village.add_animal_pythonic(bubbles)
serene_swamp.add_animal_wetlands(bubbles)
slither_inn.add_animal_snake_pit(cassis)
serene_swamp.add_animal_wetlands(lydi)
slither_inn.add_animal_snake_pit(bubbles)
