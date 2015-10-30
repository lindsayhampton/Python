__author__ = 'lindsayhampton'

import random

class Dog:
    def __init__(self):
        print "Dog created!"
        self.color = ""
        self.name = ""
        self.age = 0
    def bark(self):
        return "Woof!"


# my_dog = Dog()
# my_dog.name = "Max"
# print my_dog.name
#
# joes_dog = Dog()
# joes_dog.name = "Oscar"
# print joes_dog.name

dog_kennel = []
names = ["Rover", "Snoopy", "Coco", "Fido", "Marley", "Kujo"]
for d in range(100):
    dog = Dog()
    dog.name = names[random.randrange(0, len(names))]
    dog_kennel.append(dog)
    print dog.name

