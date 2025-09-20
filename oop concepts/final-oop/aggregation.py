class Novel:
    def __init__(self, name):
        self.name =name
        self.characters=[]

    def total_charact(self, character):
        self.characters.append(character)

    def list_characters(self):
        return [f"The popular {novel.name} characters, {character.male}" for character in self.characters]

class Characters:
    def __init__(self, male, female, genre):
        self.male = male
        self.female = female
        self.genre = genre

novel = Novel("The begining after the end")

characters = Characters("Arthur Leywin", "Tessa", "Isekai")
characters1 = Characters("Kim gogja", "Raviel", "Gates")

novel.total_charact(characters)
novel.total_charact(characters1)
print(novel.list_characters())

for character in novel.list_characters():
    print(character)