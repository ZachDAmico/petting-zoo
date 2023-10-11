# By default, if you set an attribute of an object instance in, say, the __init__ method, those values can be changed without restriction.

# class Product():

#     def __init__(self):
#         self.price = 0
#         self.title = ""
#         self.description = ""

# kite = Product()
# kite.price = 14.99
# kite.title = "A red kite"
# kite.description = "Flies up to 150 meters in the air. Made of nylon."

# # Since Python is a dynamically typed language, I can set
# # the value of those variable to anything
# kite.price = dict()  # No complaints here
# kite.description = 1024  # Python don't care
# Since Python is dynamically typed, simple attributes have no way of enforcing what value they accept. Fortunately, the language provides a way for you to check and enforce value restrictions - the @property decorator.

# Wait, what the heck is a 'decorator' you say? For now, focus on the concept of what is happening here and how to implement it. In an upcoming chapter your instructor will dive into the why/what/how of deocorators.

# class Product:

#     @property # The getter
#     def price(self):
#         try:
#             return self.__price # Note there are 2 underscores here
#         except AttributeError:
#             return 0

#     @price.setter # The setter
#     def price(self, new_price):
#         if type(new_price) is float:
#             self.__price = new_price
#         else:
#             raise TypeError('Please provide a floating point value for the price')
# Now you have set a type check on what the value of the price attribute can be.

# prod = Product()
# print(prod.price)
# # prints 0

# prod.price = 1
# In your terminal you'll see

# >>> TypeError: Please provide a floating point value for the price
# Now set the value to a floating point decimal.

# prod.price = 1.0 # Everything works ok
# Did you notice the added bonus of using @property? You simply access the property name with good old dot notation.

# prod.price
# It's like magic ✨

# "Private" Variables
# The self.__price is considered a privately scoped attribute and should not be accessed. It is obfuscated by Python to not show up as an attribute. There is a method in Python named dir(). It returns a list of valid attributes of the object. Look at what the valid attributes are for the object referenced by prod.

# print(dir(prod))

# ['__class__', '__delattr__', '__dict__', '__dir__',
#  '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__le__', '__lt__', '__module__',
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__setattr__', '__sizeof__', '__str__',
#  '__subclasshook__', '__weakref__', 'price']
# Note that price is in that list, but __price is not. Therefore, even though you, as the class designer, know that __price exists, you should not try to access it on an instance of the class.

# @property decorators can also be used to make a property essentially read-only. "Essentially" meaning there's no such thing as a truly unchangeable attribute, but as you saw above, the double underscore syntax helps hide a value from direct access via typical foo.attr syntax.

# Say a product, upon instantiation, can be given a serial number. This would typically never need to change, but would be something you would want to be able to output with a simple foo.serial_num.

# class Product:

#     def __init__(self, serial_num):
#         self.__serial_num = serial_num # setting the privately scoped attribute on instantiation

#     # BTW, when you see "..." in a code example, it just means "assume there's some other code here but we don't want to type it because it's irrelevant to the example"
#     ...

#     @property # The getter
#     def serial_num(self):
#         return self.__serial_num # now foo.serial_num will actually return the private value. There is no actual serial_num attribute. So sneaky of us.

#     @serial_num.setter # The setter
#     def serial_num(self, number):
#         pass # here, we simply tell the function to do nothing, effectively preventing the setting of a value for .serial_num. Without the setter, though, an attempt to assign a value to foo.serial_num would throw an Attribute Error and break stuff.


# Another helpful use for a getter is to create dynamic properties, meaning the ability to output a value as if it were an actual property on the object, but it's really calculated at the moment it's asked for.

# A common use case would be a person's name.

# There are a number of reasons why it makes sense to define a Person class with both first_name and last_name properties. Alphabetizing a whole collection of objects by last name is an obvious one. But, when using an object to output a human-readable name, it's a bit of a pain to concat person.first_name and person.last_name every time instead of person.full_name, right?

# Yet, physically adding a full_name property is redundant. You wouldn't ask someone filling out a form to type both their first, last, and full name. And think about how much space in a database that duplicate data would take up!

# Fortunately, we can have the best of both worlds by defining a getter that returns both values combined for us.

# class Person:
#     def __init__(self, first, last):
#         self.first_name = first
#         self.last_name = last

#     @property
#     def full_name():
#         return f'{self.first_name} {self.last_name}'

# wanda = Person("Wanda", "Patterbaum")
# print(wanda.full_name)
# # prints Wanda Patterbaum

# In object-oriented programming, a getter is a method that allows you to retrieve the value of a private attribute of an object. It provides a way to access the attribute's value without directly exposing the attribute itself.One common use case for a getter is to create dynamic properties. A dynamic property is a property that is calculated or derived at the moment it is accessed, rather than being stored as a fixed value. This allows you to have properties that appear as if they are actual attributes on the object, but their values are determined dynamically.
# One common use case for a getter is to create dynamic properties. A dynamic property is a property that is calculated or derived at the moment it is accessed, rather than being stored as a fixed value. This allows you to have properties that appear as if they are actual attributes on the object, but their values are determined dynamically.
# For example, let's say you have a Rectangle class with private attributes width and height. You can define a getter method called area that calculates and returns the area of the rectangle when accessed:

# class Rectangle:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height

#     @property
#     def area(self):
#         return self.__width * self.__height

# Now, when you create an instance of the Rectangle class and access the area property, it will calculate and return the area of the rectangle:

# rectangle = Rectangle(5, 10)
# print(rectangle.area)  # Output: 50
# In this example, the area property is dynamic because it is calculated at the moment it is accessed. If you change the width or height of the rectangle, the area property will automatically recalculate and return the updated area.

# Dynamic properties can be useful when you want to provide a convenient way to access calculated or derived values without exposing the underlying implementation details.


# Another helpful use for a getter is to create dynamic properties, meaning the ability to output a value as if it were an actual property on the object, but it's really calculated at the moment it's asked for.

# A common use case would be a person's name.

# There are a number of reasons why it makes sense to define a Person class with both first_name and last_name properties. Alphabetizing a whole collection of objects by last name is an obvious one. But, when using an object to output a human-readable name, it's a bit of a pain to concat person.first_name and person.last_name every time instead of person.full_name, right?

# Yet, physically adding a full_name property is redundant. You wouldn't ask someone filling out a form to type both their first, last, and full name. And think about how much space in a database that duplicate data would take up!

# Fortunately, we can have the best of both worlds by defining a getter that returns both values combined for us.

# class Person:
#     def __init__(self, first, last):
#         self.first_name = first
#         self.last_name = last

#     @property
#     def full_name():
#         return f'{self.first_name} {self.last_name}'

# wanda = Person("Wanda", "Patterbaum")
# print(wanda.full_name)
# # prints Wanda Patterbaum


#  you don't need a setter for the last_critter_added property. The purpose of a setter is to allow you to modify the value of an attribute, but in the case of last_critter_added, it is a dynamic property that is calculated based on the state of the animals list.

# The last_critter_added property is defined as a getter using the @property decorator, which means it is read-only. It retrieves the last item in the animals list and returns it. Since it is a calculated value, there is no need for a setter.


# You will use inheritance to reduce the amount of duplicated code that can arise in a system with dozens of types that all share the exact same properties and/or methods. It's one of the mechanisms to introduce polymorphism into a program.


# *****You will likely be asked about inheritance during the interview process and should be able to describe it in one of the following ways.

# 1 Allows one type to include all of the public properties and methods of another type.
# 2 It reduces duplicated code when many types in a program all have the same properties and methods.


# class Zero:
#     def __init__(self):
#         self.battery_kwh = 0
#         self.main_color = 0
#         self.maximum_occupancy = 0

#     def charge_battery(self):
#         ...
# # Propellor light aircraft
# class Cessna:
#     def __init__(self):
#         self.fuel_capacity = 0
#         self.main_color = 0
#         self.maximum_occupancy = 0

#     def refuel_tank(self):
#         ...
# # Electric car
# class Tesla:
#     def __init__(self):
#         self.battery_kwh = 0
#         self.main_color = 0
#         self.maximum_occupancy = 0

#     def charge_battery(self):
#         ...
# # Gas powered truck
# class Ram:
#     def __init__(self):
#         self.fuel_capacity = 0
#         self.main_color = 0
#         self.maximum_occupancy = 0

#     def refuel_tank(self):
#         ...
# That's right. They all share main_color and maximum_occupancy.

# As you add more vehicle types to your system, it would get very tedious to keep defining those properties in each of those classes. It would also increase the possibililty of bugs being introduced. If your team decided to rename the main_color property to base_color, all of the classes would need to be changed. Since human beings are highly prone to error, a class could be missed during refactoring.

# To avoid these kinds of problems, you can to create a more general type in your system and then have all vehicles inherit from it.

# Vehicle Class
# Since all of the types are vehicles, a good name for this new type would be Vehicle. It contains the properties that were determined to be common to all vehicles in this system. Vehicle is now the base, or parent, class.

# class Vehicle:
#     def __init__(self):
#         self.main_color = ""
#         self.maximum_occupancy = ""
# Then each of the other, more specific, types would inherit from it. The syntax for inheritance is dead simple: Simply specify the parent class in parenthesis after the class definition.

# class Tesla(Vehicle):
#     def __init__(self):
#         self.battery_kwh = 0

#     def charge_battery(self):
#         ...
# Now any instance of Tesla will have both of the properties from Vehicle on it automatically. Tesla is now a derived, or child, class because it inherits the properties of Vehicle.

# model_3 = Tesla()
# model_3.main_color = "red"

# print(model_3.main_color)
# #prints red

# set the parent so have self parameter only here because all the child vehicles will have those properties, but will fill them when they are instantiated, not passed down from the parent


# NOTE: When a class inherits from two parents you have to discard using the super().__init__() syntax and explicitly invoke the initialization method of both by name. You also need to pass self as an argument - something that is not needed when you use the super() abstraction.


# duck typing vs type checking

# from . import Attraction
# from movements import Walking

# class PettingZoo(Attraction):

#     def __init__(self, name, description):
#         super().__init__(name, description)

#     # Number 1: Duck typing check
#     def add_animal_pythonic(self, animal):
#         try:
#             if animal.walk_speed > -1:
#                 self.animals.append(animal)
#                 print(f"{animal} now lives in {self.attraction_name}")
#         except AttributeError as ex:
#             print(f'{animal} doesn\'t like to be petted, so please do not put it in the {self.name} attraction.')

#     # Number 2: Actual typing check
#     def add_animal_type_check(self, animal):
#         if isinstance(animal, Walking):
#             self.animals.append(animal)
#             print(f"{animal} now lives in {self.attraction_name}")
#         else:
#             print(f'{animal} doesn\'t like to be petted, so please do not try to put it in the {self.name} attraction.')

# Both methods stop an alligator from being added to a petting_zoo. One is more Pythonic than the other, but both are effective. Our recommendation is to follow the guidance of the Python community and use duck typing, and exceptions to determine if an object can be used for any specific purpose.

# Duck Typing
# "If it looks like a duck, sounds like a duck, acts like a duck, and smells like a duck, then it can do all the things we want a duck to do. It's a duck."

# The idea is that it doesn't actually matter what type my data is - just whether or not I can do what I want with it.


# ------------SELF ASSESSMENT NOTES-----------

# Classes
# 1. What is the purpose of a class in object-oriented programming (OOP)?
#     classes provide template of shared attributes for creating object(can contain data(attributes) and behavior(methods))
#     helps minimize amount of code
#     It also defines the behavior and functionality of objects created from that class. In other words,
#     a class not only describes the attributes of an object but also the actions that the object can perform.
# So, to summarize, the purpose of a class in OOP is to define a blueprint for creating objects, encapsulate data and behavior,
# promote code reusability, and provide a structure for organizing and managing code.

# 2. How does defining a class differ from instantiating an object of that class?
#     defining a class is only a template, doesn't contain any actual data or behaviors
#     instances contain the actual data for that specific object

# 3. Can you describe a real-world analogy for classes and objects?
#         class is a drum manufacturing process - contains blueprint for creation
#         includes all shared attributes for each model(can have sub class for different series of drums)
#         things like color, model, year created, and behaviors like tone
#         each drum made is instance of that class and each drum object will have own specific values for attributes defined in template
#         (and can have separate attributes unique to it if needed)

# Class Constructors
# 1. What is the role of a class constructor?
#             class contructor is special method called automatically when
#             object of that class is created (__init__ , __new__, __call__, __str__, __repr__)
#         roles of constructor are
#             Initializing the object's attributes or properties with default values.
#             Accepting parameters to set initial values for the object's attributes.
#             Performing any necessary setup or initialization tasks before the object is ready to be used.
#             Allocating any required resources or memory for the object.
#             Executing any additional logic or operations that need to be performed during object creation.

# 2. How does the __init__ method in Python differ from regular methods?
# serves as constructor - automatically called when object created
# purpose is to initialize object's attributes
# always takes self parameter first
# doesn't return anything, regular methods can return values

# Inheritance
# 1. How does inheritance promote code reusability?
#         allows multiple classes(child) to contain properties and behaviors from another class (parent class)
# Reusing Code: Inheritance allows you to define common attributes and methods in a parent class, which can be reused by multiple child classes.
# This avoids duplicating code and promotes a more efficient and organized codebase.
# Extending Functionality: Child classes can add additional attributes and methods to the inherited ones from the parent class.
# This allows you to extend the functionality of the parent class without modifying the parent
# Modifying Behavior: Child classes can override methods inherited from the parent class to modify their behavior.
# This allows you to customize the functionality of specific methods in the child class while still access parent attributes and methods

# 2. What is the difference between a base (or parent) class and a derived (or child) class?
# parent/base class contains attributes and methods that can be shared among multiple derived/child classes

# 3. Can you think of a situation where inheritance might not be the best solution?
# when there aren't shared attributes among multiple clases
# or when no clear heirarchy among classes

# Getters and Setters
# 1. Why are getters and setters used in OOP?
# way for you to check and enforce value restrictions
# getters and setters are like the guards of your castle (object).
# They control access to your treasures (data), check the quality of new treasures (data validation),
# allow you to rearrange your treasures without bothering people outside (flexibility), and can calculate the value of complex treasures for you (encapsulation of complex logic).

# 2. How do they promote data encapsulation?
# hide internal state of object - controls how internal state is accessed and modified

# 3. Can you think of a scenario where direct access to an attribute might be problematic?
#         changing a serial number?

# Composition
# 1. How does composition differ from inheritance?
#         inheritance -  mechanism that allows a class to inherit the properties and methods of another class.
# This is often described as an "is-a" relationship. For example, if you have a class "Animal" with a method "eat", and a class "Dog" that inherits from "Animal",
# you're saying that a "Dog" is an "Animal" and therefore, it can also "eat".
# Inheritance is typically used when there is a clear hierarchical relationship between classes.
# Inheritance is about extending the functionality of a class,
# and is best used when there is a clear, hierarchical "is-a" relationship between two classes.

# example class Animal:
#     def eat(self):
#         pass

# class Dog(Animal):
#     pass

# d = Dog()
# d.eat()

# composition - way to combine simple objects or data types into more complex ones.
# This is often described as a "has-a" relationship. For example, if you have a class "Car" and a class "Engine",
# you might say that a "Car" has an "Engine". In this case, you would use composition to add an Engine instance to a Car instance.
# example class Engine:
#     pass

# class Car:
#     def __init__(self):
#         self.engine = Engine()  # Car has an Engine

# Composition is about combining simpler objects to form more complex ones,
# and is best used when there is a "has-a" relationship between two classes,
# where one class is composed of one or more instances of other classes.


# 2. Why might you choose composition over inheritance in certain scenarios?
#         composition when not a clear heirarchy relationhip - might draw from multiple parent classes
#         composition can provide more flexibility
#         example Let's say you're modeling a zoo. You might have classes like Bird, Fish, and Mammal. Now, you want to add a Penguin class.
# Penguins are birds, but they also swim like fish. In this case,
# it's not clear whether Penguin should inherit from Bird or Fish.
# But with composition, Penguin can be composed of a Bird part (for bird-like behavior) and a Fish part (for swimming behavior), solving the problem.

# 3. Can you provide an example from the project where composition was particularly useful?
# when animals could have multiple methods of movement

# Multiple inheritance

# 1. What challenges might arise from using multiple inheritance?
#         potential ambiguity - same method present in multiple parent classes
# can increase complexity unnessecarily
# if child inheriting from multiple parents, changes to either parent could affect child

# 2. How does Python's method resolution order (MRO) help in resolving ambiguities in multiple inheritance?
# MRO is order in which methods resolved during multiple inheritance -
# determines sequence of base classes searched for particular method or attribute
#         example class A:
#     def method(self):
#         print("In class A")

# class B(A):
#     def method(self):
#         print("In class B")

# class C(A):
#     def method(self):
#         print("In class C")

# class D(B, C):
#     pass

# d = D()
# d.method()

# In this example, class D inherits from classes B and C, both of which inherit from class A.
# The MRO for class D is calculated as D -> B -> C -> A -> object.
# When the method() is called on an instance of class D,
#      it will first check for the method in class D, then in class B, then in class C, and finally in class A.
#      In this case, the method from class B would be called, resulting in the output "In class B".

# 3. Can you think of an alternative to multiple inheritance to achieve similar functionality?
# composition, mixin classes,interfaces, delegation - look up

# Duck Typing
# 1. How would you explain the phrase "If it looks like a duck, swims like a duck, and quacks like a duck,
# then it probably is a duck" in the context of programming?
#  doesn't matter what the type my data is - just whether i can do what i want with it or not
# In programming, duck typing is a dynamic typing concept where the type or class of an object is less important than the behavior it exhibits.
# It focuses on the presence of certain methods or attributes rather than the specific type of the object.

# The phrase suggests that if an object behaves like a certain type, it can be treated as that type, regardless of its actual class or type.
# In other words, if an object has the same methods or attributes as a particular type, it can be considered an instance of that type.

# 2. How does duck typing differ from strict type checking?
# In summary, duck typing focuses on the behavior of an object and allows for more flexibility and generic code,
# it determines the suitability of an object based on whether it has the necessary methods or attributes to perform a certain operation
# while strict type checking enforces explicit type declarations and ensures that operations are performed on objects of the correct type.
#  is a static typing concept where the types of variables and objects are explicitly declared and enforced by the programming language.
# In strict type checking, the compiler or interpreter checks that the types of variables
# and objects are compatible and that the operations performed on them are valid

# 3. Can you provide an example from the project where duck typing was beneficial?
# when placing animals in attractions based on walking, swimming, slithering attributes

# Python Packages
# 1. Why are packages important in Python programming?
# modularity and organization - allows you to organize into logical units, grouping related modules together
# prevents name clash between modules
# 2. How do packages help in organizing and modularizing code
# allows you to group similar modules together - hierarchy structure of directories and subdirectories
# 3. Can you name a few Python packages you used in the project and explain their purpose?
# animals directory with .py modules to store related animal modules
