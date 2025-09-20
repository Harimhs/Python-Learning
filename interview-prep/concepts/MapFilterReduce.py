from functools import reduce

novels= [1, 2, 3, 4, 5]
novel = map(lambda x: x+2, novels)
print(list(novel))

def novels_func(a):
    return a+2
result = list(map(novels_func, novels))
print(result)

novel = filter(lambda x=2: x-2, novels)
print(list(novel))

novel_reduce= reduce(lambda x, y: x+y, novels)
print(novel_reduce)
