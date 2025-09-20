class Fiction:

    def __init__(self, title, availability):
        self.title = title
        self.availability = availability

    def reading(self):
        print(f"The book {self.title} is available for reading.")

    def adaption(self):
        print(f"The fiction book {self.title} is now ready for adaption.")

class Manhua(Fiction):
    def reading(self):
        print(f"The manhua {self.title} is a chinese comic book.")

class Manhwa(Fiction):
    def reading(self):
        print(f"The manhwa {self.title} is a korean comic book.")

class Manga(Fiction):
    def reading(self):
        print(f"The manga {self.title} is a japanese comic book.")

manhua = Manhua("Magic Emperor", True)
manhwa = Manhwa("Solo leveling", True)
manga = Manga("Naruto", True)

print(manga.reading())
print(manga.adaption())
manhua.reading()