from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def living(self):
        pass
    
    def eat(self):
        print("Eating...")

class Prey(Animal):

    def living(self):
        print("living...")
    
    def run(self):
        print("running...")

prey = Prey()
prey.eat()
prey.living()
