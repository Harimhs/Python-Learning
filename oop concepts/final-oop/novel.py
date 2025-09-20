class Novel:
    def __init__(self, title, year, type, availability):
        self.title = title
        self.year = year
        self.type = type
        self.availability = availability

    def read(self):
        print("You are reading... ", self.title)