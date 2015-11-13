class Bird(object):
    def __init__(self, n):
        print "Bird Created!"
        self.name = n
        self.size = ""

    def fly(self):
        return self.name + " is flying!"

class Duck(Bird):
    def __init__(self, n):
        print "Duck Created!"
        super(Duck, self).__init__(n)

    def quack(self):
        return self.name + " is quacking!"

class Daffy(Duck):
    def __init__(self):
        self.movies = "Space Jam"
        super(Daffy, self).__init__()

duck = Duck("Daffy")
print duck.name
print duck.quack()
print duck.fly()