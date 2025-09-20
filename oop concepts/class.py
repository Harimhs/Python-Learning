class Item:
    def calculate_item(self, a, b):
        return a * b

item1 = Item()
item1.name = "mobile"
item1.price = 10000
item1.quantity = int(input("Enter the quantity: "))
print("Total Price is:", item1.calculate_item(item1.price, item1.quantity))

item2 = Item()
item2.name = "laptop"
item2.price = 30000
item1.quantity = int(input("Enter the quantity: "))
print("Total Price is:", item2.calculate_item(item2.price, item2.quantity))
