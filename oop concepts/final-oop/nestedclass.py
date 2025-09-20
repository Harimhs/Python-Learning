class Collection:

    class Novels:
        
        def __init__(self, name, type):
            self.name = name
            self.type = type
        
        def details(self):
            return f"Name: {self.name}, Type: {self.type}"

    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.novels = []

    def add_collection(self, novels):
        self.novels.append(novels)

    def display_collection(self):
        return [novel.details() for novel in self.novels]

collection = Collection("Fav")
novel1 = Collection.Novels("TBATE", "Fantasy")
collection.add_collection(novel1)
print(collection.display_collection())

