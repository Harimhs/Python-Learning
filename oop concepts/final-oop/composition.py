class Novel:

    def __init__(self, type, author, publish, chapters):
        self.type = type
        self.author = author
        self.year = Year(publish)
        self.volumes = [Volumes(chapters) for chapter in range(12)]

    def display(self):
        print(f"Type: {self.type} is written by {self.author} and published in {self.year.publish} that has {self.volumes[2].chapters} volumes!")

class Year:

    def __init__(self, publish):
        self.publish = publish

class Volumes:

    def __init__(self, chapters):
        self.chapters = chapters


novel = Novel("Manhwa", "Kim", 2010, 16)

novel.display()
        