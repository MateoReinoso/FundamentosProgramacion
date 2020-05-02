def x(y):
    y=y*2
    return y

print(x(5))

# lo que se realizo arriba en la funcion aca se hizo en una sola linea
x= lambda y: y*2
print(x(5))

numeros = [1,2,3,4,5,]
update = []
for value in numeros:
    update.append(value*2)
print(update)

#usando map
def opeation(value):
    return value*2

print(list(map(opeation,numeros)))

#usando lamda
print(list(map((lambda value:value*2),numeros)))


#sinfilter
num = [1,2,3,4,5]
par =[]
for value in num:
    if (value%2==0):
        par.append(value)
print(par)

def PAr(nume):
    return nume%2==0

print(list(filter(PAr,num)))

print(list(filter((lambda numes:numes%2==0),num)))
