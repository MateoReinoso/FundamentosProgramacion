mat1 = [
    [1,2,3],
    [7,8,9],
    [13,14,15]
]
mat2 = [
    [4,5,6],
    [10,11,12],
    [16,17,18]
]
mat3 = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

mat3[0][0]=mat1[0][0]+mat2[0][0]

print(mat3[0][0])

print(mat1[0][0])
print(mat2[0][0])

for rowPosition, value in enumerate(mat1):
    for columPosition, value2 in enumerate(value):
        mat3[rowPosition][columPosition] = value2 + mat2[rowPosition][columPosition]


print(mat3.reverse())

for rowPosition, value in enumerate(mat3):
    for columPosition, value2 in enumerate(mat3):
        print(mat3[rowPosition][columPosition])

