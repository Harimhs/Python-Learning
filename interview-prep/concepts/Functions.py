def novel(name):
    return name
print(novel("LOTM")) #LOTM

def novel(name= "ORV"):
    return name
print(novel()) #ORV, without parameter passing

def novel(name, year):
    return "The novel " + name + " was published in " + str(year)
print(novel("LOTM", 1990)) #The novel LOTM was published in 1990

# nested function
def novel(name):
    print(name)

    def fiction():
        print("This is a fiction novel")
    
    fiction()
novel("Magic emperor")
