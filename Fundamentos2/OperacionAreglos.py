def plusNumber(list):
    #plus es la variable en donde nosotros guardaremos el valor en el que se vaya sumando
    par = 0
    impar = 0
    for value in list:
        if value % 2 == 0:
            par = par + value
        else:
            impar = impar +value
    print("Pares",par)
    print("Impares",impar)
