nombre = input("Nombre del archivo: ")

try:
    with open(nombre, "r") as archivo:
        print(archivo.read())

except FileNotFoundError:
    print("Error: no existe el archivo ingresado")

finally:
    print("Fin del programa. Gracias por usar.")
    