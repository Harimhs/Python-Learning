def factorial(n):
    if(n==1): return 1
    return n * factorial(n-1)

print(factorial(5))

def string(word):
    if(len(word)==0): return ""
    return word[0] + string(word[1:])

print(string("bro"))