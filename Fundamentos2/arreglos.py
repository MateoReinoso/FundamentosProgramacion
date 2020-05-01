#un arreglo es una lista en python
# primero lista
# segundo diccionario
colores = ["Verde", "Morado", "Amarillo"]
numeros = [1,2,3,4,5,6,7,8,9]
persona = {"name":"Daniel",
           "lastName":"Reinoso",
           "age":22}

#listas
#primer metodo pop este metodo nos devuelve el elemento en la posicion en la que nosotros especifiquemos en la lista y luego lo borra
print(colores.pop(2))
print("________________________________________________-")

# con append nosotros añadimos un elemento al final de la lista
colores.append("Rojo")



for value in colores:
    print(value)
print("________________________________________________-")
# si deseamos ingresar un valor en cualquier posicion de la lista usamos insert
colores.insert(0,"Verde")

# para remover un elemento se usa remove
colores.remove("Rojo")
# con este metodo contamos cuantos elementos iguales tenemos que sean parecidos en la lista
print(colores.count("Verde"))



#de esta forma recorremos el arreglo
for value in colores:
    print(value)
print("_________________________________________________")
#de esta forma nosotros recorremos el valor de un diccionario imprimiendo todos sus itemes
for key, value in persona.items():
    print(key,value)
print("_________________________________________________")
#si deseamos imprimer de forma reversa debemos emplear el metodo reverse
numeros.reverse()
#con el metodo extende se realiza la union de dos listas
numeros.extend(colores)
#para modificar un elemento dentro de una lista usamos
colores[0]="Azul"
for value in colores:
    print(value)

for value in numeros:
    print(value)