class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_item(self):
        return self.price * self.quantity


item1 = Item("mobile", 1000, 3)
print("Total Price is:", item1.calculate_item(item1.price, item1.quantity))

item2 = Item("laptop", 5000, 5)
print("Total Price is:", item2.calculate_item(item2.price, item2.quantity))
