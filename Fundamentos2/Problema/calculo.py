def validar(message):
    #en esta seccion de codigo validamos para que no se ingrese otro tipo de dato
    while True:
        try:
            data=float(input("Coloca "+message))
            return data
        except ValueError:
            print("El dato debe ser entero o decimal")
"""
En esta secion inferior e encuentra la parte del menu principalr
"""
#Datos de entrada
largo = validar("el largo en mts: ")
ancho = validar("Ingrese el ancho en mts: ")
m2Xcaja = validar("Coloque los metros cuadrados por caja")
precioXm2 = validar("coloque el precio por metro cuadrado")
"""
Aqui se ha realizado una regla de tres 
"""
precioXcaja = (m2Xcaja*precioXm2)
m2Cuarto = largo * ancho
cajas = m2Cuarto/m2Xcaja
precioTotal = cajas*precioXcaja
print("Total de cajas a usar", cajas)
print("Precio total",precioTotal)
