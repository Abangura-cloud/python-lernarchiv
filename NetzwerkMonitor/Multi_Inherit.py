class Flyer:
    def fly(self):
        print("Flying high!")

class Swimmer:
    def swim(self):
        print("Swimming deep!")

# Duck inherits from BOTH classes!
class Duck(Flyer, Swimmer):
    pass

daffy = Duck()
daffy.fly()
daffy.swim()

