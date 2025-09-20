name = "er users 334"
print(name.isalpha()) #to check is a string has only string
print(name.isalnum()) #to check is a string has only alphanumeric characters
print(name.isdecimal()) #to check is a string has only decimal numbers
print(name.lower()) #to convert a string to lower case
print(name.islower()) #to check is a string has only lower case
print(name.upper()) #to convert a string to upper case
print(name.isupper()) #to check is a string has only upper case
print(name.startswith("er")) #to check if a string starts with a specified value
print(name.endswith("334")) #to check if a string ends with a specified value
print(name.replace("er", "bro")) #to replace a specified value in a string
print(name.split("s")) #to split a string into a list where each word is a list item
print(name.strip()) #to remove leading and trailing characters from a string
print(name.join("bro")) #to join a list of strings into a single string
print(name.find("s")) #to find the index of the first occurrence of a specified value in a string

#substring finding
print("er" in name)