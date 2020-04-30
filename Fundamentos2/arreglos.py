#un arreglo es una lista en python
colores = ["Verde", "Amarillo", "Morado"]
persona = {"name":"Daniel",
           "lastNAme":"Reinoso",
           "age":22}


#de esta forma recorremos el arreglo
for value in colores:
    print(value)

#de esta forma nosotros recorremos el valor de un diccionario imprimiendo todos sus itemes
for key, value in persona.items():
    print(key,value)