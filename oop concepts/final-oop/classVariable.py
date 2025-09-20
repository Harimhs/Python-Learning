class Main:

    year= 2025
    no_of_novels = 0

    def __init__(self, title, type):
        self.title = title
        self.type = type
        Main.no_of_novels+=1

main1 = Main("The Great Gatsby", "Novel")
main2 = Main("The Great Gatsby", "Novel")

print(Main.no_of_novels)
print(f"Totally {Main.no_of_novels} novels have been written in {Main.year}.")