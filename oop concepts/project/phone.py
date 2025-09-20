from item import Item

class phones(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"The attribute {broken_phones} must be equal or above 0"
        self.broken_phones = broken_phones