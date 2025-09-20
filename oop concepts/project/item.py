import csv

class Item:

    cost_rate = 0.8
    all=[]

    def __init__(self, name: str, price: float, quantity=0):

        assert price >= 0, f"The attribute {price} must be equal or above 0"
        assert quantity >= 0, f"The attribute {quantity} must be equal or above 0"

        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    #To not allow to set the attribute and read only
    @property
    def name(self):
        return self.__name

    #To allow to set the name 
    @name.setter
    def name(self, value):
        if len(value)>10:
            raise Exception("Too long")
        else:
            self.__name= value

    def calculate_item(self):
        return self.price * self.quantity

    def calculate_discount(self):
        self.price= self.price * self.cost_rate

    @classmethod
    def from_csv(cls):
        with open('item.csv', 'r') as d:
            read= csv.DictReader(d)
            items= list(read)
        
        for item in items:
            print(item)

    @staticmethod
    def is_integer(abc):
        if isinstance(abc, float):
            return abc.is_integer()
        elif isinstance(abc, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price})"