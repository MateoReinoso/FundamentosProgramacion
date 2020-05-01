persona = {"name":"Daniel",
           "lastName":"Reinoso",
           "age":22}

mascotas = {
    "name1":"Nena",
    "name2":"Lala",
    "name3":"Lupe"
}

print(len(mascotas))

# con el metodo pop nos muestra el elemento que va hacer borrado
print(persona.pop("lastName"))
print("___________________________________________")
#para agregar un dato se debe usar el metodo update y este se agrega al final de la lista
persona.update({"phono":"123456789"})
persona.update({"name":"Mateo"})
for key, value in persona.items():
    print(key,value)

print("___________________________________________")
#para fucionar dos diccionarios usamos tambien update
persona.update(mascotas)
for key, value in persona.items():
    print(key, value)