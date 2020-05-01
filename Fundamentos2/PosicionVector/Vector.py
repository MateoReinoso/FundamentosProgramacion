number = [1,2,3,4,5]

for position in range(0,len(number)):
    print("posicion",position+1,"",number[position])

print("________________________________________________")

for position, value in enumerate(number):
    print("posicion",position+1,"",value)