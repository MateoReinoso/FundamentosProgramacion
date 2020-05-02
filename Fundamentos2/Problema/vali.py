def validar(message):
    while True:
        try:
            data=float(input("Coloca "+message))
            return data
        except ValueError:
            print("El dato debe ser entero o decimal")
