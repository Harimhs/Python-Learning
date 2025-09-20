class Item:

    cost_rate = 0.8

    def __init__(self, name: str, price: float, quantity=0):

        assert price >= 0, f"The attribute {price} must be equal or above 0"
        assert quantity >= 0, f"The attribute {quantity} must be equal or above 0"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_item(self):
        return self.price * self.quantity

    def calculate_discount(self):
        self.price= self.price * self.cost_rate

item1 = Item("mobile", 100, 3)
item1.calculate_discount()
print(item1.price)

item2 = Item("laptop", 1000, 5)
item2.cost_rate= 0.7
item2.calculate_discount()
print(item2.price)

#item3 = Item("cable", 10, 3)
#item4 = Item("mouse", 50, 2)
#item5 = Item("keyboard", 25, 6)

