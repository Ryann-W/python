
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

class name:
    z = 0
    name = ""
    def __init__(self,v):
        self.name = v
        print(self.name, "constructed")

    def dog(self):
        self.z = self.z + 1
        print(self.name, "pretty count", self.x)


car = name("jim")
car.dog()

car2 = name("frank")
car.dog()
car2.dog()
