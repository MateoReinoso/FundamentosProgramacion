import functools
numbers = [1,2,3,4,5]
res=0
for value in numbers:
    res = res + value
print(res)

#realizado en una sola linea
print(str(functools.reduce((lambda x, y: x+y),numbers)))