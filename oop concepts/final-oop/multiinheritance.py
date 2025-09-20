class Animals:
    def __init__(self, name):
        self.name= name

    def living(self):
        print(f"The {self.name} is living!")

    def not_living(self):
        print(f"The {self.name} is not living!")

class Prey(Animals):

    def hunted(self):
        print(f"The {self.name} is being hunted!")

class Predator(Animals):

    def hunting(self):
        print(f"The {self.name} is hunting!")

class rabbit(Prey):
    pass

class wolf(Predator):
    pass

class fish(Predator, Prey): #multiple inheritance
    pass

rabbit1 = rabbit("bunny")
rabbit1.living()
rabbit1.hunted()
rabbit1.hunted()
fish1 = fish("nemo")
fish1.living()
fish1.hunting()
fish1.hunted()