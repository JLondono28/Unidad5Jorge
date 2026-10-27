lista = ["El fin de la eternidad", "La biblia", "Sapiens", "Cadaver exquisito"]
lista2 = []

lista3 = [123, "hola", 34.5, "programación"]
lista4 = []

for libro in lista:
    lista2.append(libro+"\n")

for indice, dato in enumerate(lista3):
    lista3[indice] = str(dato)+"\n"

archivo = open("libros.txt", "a")
archivo.writelines(lista2)
archivo.writelines(lista3)
archivo.close()