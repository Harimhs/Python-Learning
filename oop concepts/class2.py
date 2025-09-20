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


item1 = Item("mobile", 100, 3)
item2 = Item("laptop", 1000, 5)

print(Item.__dict__)
print(item1.__dict__)
