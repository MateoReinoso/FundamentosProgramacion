#Nombres = [
  #            {"name1":"Daniel","name2":"Mateo","name3":"Juan"},
 #             {"name4":"Paula","name5":"Erika","name6":"Lizeth"},
#    {"name7":"Sandy","name8":"Yuleis","name9":"Vanesa"}
#]

#print(Nombres[2]["name9"])

zapatoss ={
    #trabajamos con listas internas
    "Nike":["tenis1","tenis2","tenis3"],
    "Adidas":["tenis4","tenis5","Tenis6"],
    "Converse":["Tenis7","tenis8","tenis9"]
}
print(zapatoss["Nike"][1])

val = 0
for key, list in zapatoss.items():
    for value in list:
        if value % 2 == 0:
            print("Estos son los zapatos", key, value)