
# Objected Programming

# one example for class
# class is a reserved word

class PartyAnial:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("so far", self.x)

an = PartyAnial()

print(an.party())
print(an.party())
print(an.party())

print(type(an))
print(dir(an))

class PartyAnimal:
    y = 0

    def __init__(self):
        print('i am the beginning')  # setup the initial value of the class , the constructor

    def play(self):
        self.y = self.y + 1
        print(self.y)

    def __del__(self):
        print('this is the end of the code') # setup the end of the class , the destructor


ann = PartyAnimal()

print(ann.play())
print(ann.play())

ann = 34
print(ann)
ann = 'ble'
print(ann)

# the constructor used to set up variables, the destructor is seldom used.


# reference from freecodecamp

# we can create lots of obejects - the class is the template for the object

# we can store each distinct object in its own variable

# we call this having multiple instances of the same class

# each instance has its own copy of the instance variables.

class PartyAnimals:
    x = 0
    name = ""
    def __init__(self,z):
        self.name = z
        print(self.name, "constructed")

    def parties(self):
        self.x = self.x + 1
        print(self.name,"parties count", self.x)

s = PartyAnimals("sally")
s.parties()

j = PartyAnimals("Jim")
j.parties()
s.parties()   # the value return 2 bacause s.parties already have 1, and not becasue the j.parties

# Inheritance

# Some definitions of class reference from FreeCodeCamp

# Class - a template (a shape of a thing)
# Attribute - A variable within a class
# Method - A function within a class
# Object - A particular instance of a class
# Constructor - Code that runs when an object is created
# Inheritance - The ability to extend a class to make a new class

# the new class(child) has all the capabilities of the old class(parent) - and then some more

# one example

class FootballFun(PartyAnimals):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.parties()
        print(self.name, "points", self.points)


g = FootballFun("Mij")
g.parties()
g.touchdown()