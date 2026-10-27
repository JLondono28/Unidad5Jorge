file = open("texto_ejemplo.txt", "r", encoding="utf-8")

#read() leo el número de caracteres indicados
# texto_leido = file_read()
# si read() no tiene parámetro, se lee todo el archivo
# readline() lee hasta que encuentra un "\n"
# texto_leido = file.readline()

#readlines() lee el archivo en un lista, cada elemento es una línea
datos = file.readlines()
print(datos[0])

file.close()