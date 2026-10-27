nombre_archivo = input("Nombre del nuevo archivo: ")

with open(nombre_archivo, "w+") as archivo:
    datos = input("Escribe tu primer decreto: ")
    archivo.write(datos)
    archivo.seek(0)
    frase = archivo.read()
    print(frase)