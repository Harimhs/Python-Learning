from abc import ABC, abstractmethod

class Shapes(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
 
class Square(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Pizza(Circle):
    def __init__(self, radius, toppings):
        super().__init__(radius)
        self.toppings = toppings

shapes = [Circle(3), Square(4), Pizza(6, "pepporicon")]

for shape in shapes:
    print(shape.area())
