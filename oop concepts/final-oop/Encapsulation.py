class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property #getter
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

    @width.setter #setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    @width.deleter
    def width(self):
        del self._width
        print("Delected!!!!")
    
    @height.deleter
    def height(self):
        del self._height
        print("Delected!!!!")

rectangle = Rectangle(3, 4)
print(rectangle.height)
rectangle.width=9 
print(rectangle.width)
del rectangle.width
