class Novel:
    def __init__(self, title, author, year, type):
        self.title = title
        self.author = author
        self.year = year
        self.type = type

    def description(self):
        print(f"The popular novel {self.title} by {self.author} is {'Available' if self.type else 'Not Available'}")

class Manhua(Novel):
    def __init__(self, title, author, year, type, chinese):
        super().__init__(title, author, year, type)
        self.type = type
        self.chinese = chinese 

class Manhwa(Novel):
    def __init__(self, title, author, year, type, korean):
        super().__init__(title, author, year, type)
        self.type = type
        self.korean = korean

    def description(self):#method overriding
        super().description()

class Manga(Novel):
    def __init__(self, title, author, year, type, japanese):
        super().__init__(title, author, year,  type)
        self.type = type
        self.japanese = japanese

naruto =  Manga("Naruto", "Kishimoto", 2002, True, "Japanese")
solo_leveling = Manhwa("Solo leveling", "Chugong", 2018, False, "Korean")

print(naruto.title)
print(solo_leveling.title)
solo_leveling.description()