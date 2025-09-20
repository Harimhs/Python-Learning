novel = ["TBATE", "Magic emperor", 3, "ORV"]
print(novel[1])
# Output: Magic emperor
novel[3]= "the greatest estate developer"
print(novel[3])
# Output: The greatest estate developer
print(novel[1:3])
# Output: ['Magic emperor', True, 3]
novel.append("COTE")
novel.extend(["Jobless reincarnation", "Re-zero"])
print(novel)
# Output: ['TBATE', 'Magic emperor', 'The greatest estate developer', 'ORV', 'COTE', 'Jobless reincarnation', 'Re-zero']
novel+= ["LOTM"]
print(novel)
# Output: ['TBATE', 'Magic emperor', 'The greatest estate developer', 'ORV+ LOTM']
novel.remove(3)
novel.insert(2, "teis")
print(novel)

#sorting lists
novel.sort()
print(novel)
novel.sort(key=str.lower)
print(novel)