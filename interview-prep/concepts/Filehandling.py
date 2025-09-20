filename = 'Readfile.txt'

try:
    file = (filename, 'r')
    content = file.read()
    print(content)

except:
    print("File not found")

finally:
    print("closed bro")

