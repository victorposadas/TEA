try:
    entrada = input("Ingrese el nombre del archivo: ")
    archivo = open(entrada, "r" , encoding="UTF-8")
    for línea in archivo:
        print(línea.upper())
except:
    print("Error, el archivo no existe")