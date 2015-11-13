import random

class Soda():
    def __init__(self, name):
        self.color = ""
        self.name = name
        self.id = random.randrange(0,100000)
        #VARIABLES ARE A BIG NO NO - CANT BE CALLED BY OTHER FUNCTIONS
        brand = "Pepsi"


    def explode(self):
        pass

    def fizz(self):
        pass

dew = Soda("Mountain Dew")
print dew.name

dr = Soda("Dr. Pepper")
print dr.name

pallet = []
for i in range(100):
    soda = Soda("Mountain Dew")
    pallet.append(soda)
    print soda.name + " " + str(soda.id)

print "The ID of the 10th soda is: " + str(pallet[9].id) + "."