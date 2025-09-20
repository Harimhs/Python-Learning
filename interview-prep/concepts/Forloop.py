novels = ["TBATE", "ORV", "LOTM", "TGED"]
for novel in novels:
    print(novel)

for index, novel in enumerate(novels):
    print(index, novel)

for i in range(1, 5+1):
    print("DAY", i)
    for j in range(1, 8):
        print(j+8, "-", j+9)