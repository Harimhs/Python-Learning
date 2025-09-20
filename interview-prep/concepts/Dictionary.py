novels = {"manga":"naruto", "manhwa":"The greatest estate developer", "manhua":"Magic emperor"}
novels["manhwa"]= "solo leveling"

print(novels)
print(novels.get("manhua"))
# print(novels.pop("manga"))
# print(novels.popitem()) remove last pair
print(list(novels.keys()))
print(list(novels.items())) #lists all the content
novels["novel"]= "Lord of the mystery"
print(novels) #add new key value pair
# print(novels.clear()) #clears all the content
del novels["novel"]
print(novels) #delete a key value pair