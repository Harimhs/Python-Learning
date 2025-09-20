print("Hello World!")

# naming and using variables
message = "Hello Python Crash Course world!"
print(message)

# strings: changing case in strings with methods
# title refers sentance
name = "hello world"
print(name.title())

# lower and upper cases
name = "hello world"
print(name.lower())
print(name.upper())

# use variables in strings
first = "abc"
last = 4
name = f"{first} {last}"
print(name)

# format method
print("first name is {} last name is {}".format(first, last))

# % method
print("first name is %s last name is %d." % (first, last))

#whitespace concepts
#tab
print("python")
print("\tpython")

#newline
print("languages: \npython\nc\nJS")

print("languages: \n\tpython\n\tc\n\tJS")

#lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())

#user input list
a= input("First letter:")
b= input("second letter:")
c= input("third letter:")
letters= []
letters.append(a)
letters.append(b)
letters.append(c)
print(letters)

#append
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#insert
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#delete
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#removing using pop
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

