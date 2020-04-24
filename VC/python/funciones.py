def saludar(nombre):
    return "Hola {} bienvenido al trabajo de Mateo".format(nombre)

print("ingresa tu nombre: ")
nombre  = input()
print(saludar(nombre))

# saludar(nombre) esto es pasar un parametro la cual es la variable nombre
# def saludar(nombre): recepcion de lo que el usuario nos mande