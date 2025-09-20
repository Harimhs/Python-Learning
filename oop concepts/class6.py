import csv

class Item:

    cost_rate = 0.8
    all=[]

    def __init__(self, name: str, price: float, quantity=0):

        assert price >= 0, f"The attribute {price} must be equal or above 0"
        assert quantity >= 0, f"The attribute {quantity} must be equal or above 0"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

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

class phones(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"The attribute {broken_phones} must be equal or above 0"
        self.broken_phones = broken_phones

phones1= phones('iphone', 800, 2)

print(Item.all)
print(phones.all)