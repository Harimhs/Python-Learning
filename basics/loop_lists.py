# looping in list
animes = ["naruto", "bleach", "haikyuu", "bluelock", "JJK"]
for anime in animes:
    print(anime)

# process within the loop
chars = [
    "02",
    "mai",
    "chizuru",
    "rin",
]
for char in chars:
    print(f"{char.title()}, best character!")

# process after the loop
chars = [
    "02",
    "mai",
    "chizuru",
    "rin",
]
for char in chars:
    print(f"\t{char.title()}, best character!")
print("Everyone are amazing chars")
