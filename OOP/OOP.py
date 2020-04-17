"""
Script to show main points of OOP in Python
"""

# defining a class
class Example(): # name by convention starts with capital letters
    pass

instance_1 = Example() # instance of an Example class

###############################################################################

class NBA(): # parent class
    # class attribute
    profession = "player"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # example of a method
    def change_age(self, new_age):
        self.age = new_age

# instantiate the NBA class
leBron = NBA("Lebron James", 35)

# access the class attributes
print("Lebron is also a {}".format(leBron.__class__.profession)) # 1st method
print("Lebron James is also a {}".format(leBron.profession)) # 2nd method

# access the instance attributes
print("{} is {} years old".format(leBron.name, leBron.age))

# calling a method with 'dot notation'
leBron.change_age(40)
print("{} is {} years old\n".format(leBron.name, leBron.age))

leBron.profession = "SuperHero"     # doesn't change class attribute
garnett = NBA("Kevin Garnett", 40)
print("Lebron James is also a {}".format(leBron.profession))
print("Kevin Garnett is also a {}".format(garnett.profession)) # player
print("Class attribute didn't change = {0}".format(NBA.profession))

NBA.profession = "lazy boy" # possible to directly change class attribute
print("------------")
print("Lebron James is also a {}".format(leBron.profession))
print("Kevin Garnett is also a {}".format(garnett.profession))
print("Class attribute didn't change = {0}".format(NBA.profession))

###############################################################################

# example of 'inheritance'

class Raptors(NBA): # child class
    # function 'super' to inherit from other class
    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number

    def get_number(self):
        print("Player number is {}\n".format(self.number))

lowry = Raptors("Lowry", 29, 0)
lowry.change_age(18)
print("{} is {} years old".format(lowry.name, lowry.age))
lowry.get_number()


###############################################################################
"""
_name - proteceted attribute
__name - private attribute

However it's possible to modify them
"""

# example of 'Encapsulation'
class Computer:

    def __init__(self):
        self.__maxprice = 900
        self._minprice = 100

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def sellMin(self):
        print("Selling Price shouldn't be lower than {}".format(self._minprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

    def setMinPrice(self, price):
        self._minprice = price

print("\nInitial settings")
c = Computer()
c.sell()
c.sellMin()

# change the price
print("\nChanging function manually")
c.__maxprice = 1000 # it doesn't work !!!
c._minprice = 200
c.sell()
c.sellMin()

# using setter function
print("\nChanging function using setter function")
c.setMaxPrice(1100)
c.setMinPrice(300)
c.sell()
c.sellMin()

# change the price 'trick'
print("\nChanging function manually - name mangling")
c._Computer__maxprice = 3000 # changing 'private variable !!!'
c.sell()

d = Computer()
d.sell()
d.sellMin()

print('\n')

###############################################################################

"""Polymorphism - example different implementation of sum for str and int"""

print("Polymorphism - example different implementation of sum for str and int")
a, b = 3, 5
print('Sum of integers {}'.format(a + b))

c, d = 'City', 'Herborn'
print('Sum of strings {}\n'.format(c + d))

###############################################################################

"""
Static method
- bound to a class, not to object of the class
- can be called without an object of that class
- cannot modify the state of the object as they are not bound to it
"""

class Calculator:
    # create addNumbers static method

    version = "1.0.1"
    
    @staticmethod # convention to point that it is a static method
    def multiplyNums(x, y):
        return x + y

    @staticmethod
    def vers(name):
        Calculator.version = name

print("\nStatic method @staticmethod")
print('Product:', Calculator.multiplyNums(15, 110))
print(Calculator.version)
Calculator.vers("2.0.1")
print(Calculator.version)

print()
###############################################################################


"""
Class method
- bount to class, not to object of the class
- can be called without an object of that class
- can modify the state of the class
"""

class Pizza:
    pizza_number = 0
    
    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.pizza_number += 1

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

    @classmethod    # class method can also accept additional parameters
    def village(cls, ingredient):
        return cls(['mozzarella', 'tomatoes', ingredient])

    @classmethod
    def new_pizza(cls):
        Pizza.pizza_number += 1

    @staticmethod
    def armagedon():
        Pizza.pizza_number = 1000

##    @staticmethod
##    def change(): 
##        self.ingredients = ['ONION'] # raises NameError

print("Class method @classmethod")
P = Pizza(['cheese'])
print("Number of pizzas: {0}".format(Pizza.pizza_number))
print('Pizza margherita: ', Pizza.margherita())
print("Number of pizzas: {0}".format(Pizza.pizza_number))
print('Pizza prosciutto: ', Pizza.prosciutto())
print("Number of pizzas: {0}".format(Pizza.pizza_number))
print("Number of pizzas: {0}".format(P.pizza_number))
Pizza.new_pizza()
print("Number of pizzas: {0}".format(Pizza.pizza_number))
Pizza.armagedon()
print("Number of pizzas: {0}".format(Pizza.pizza_number))
print("Number of pizzas: {0}".format(P.pizza_number))
print(Pizza.village('sausage'))
