cadena = "X-DSPAM-Confidence:0.8475"

pos1 = cadena.find(":")
print("Inicia en el Indice: "+ str(pos1))

pos2 = cadena.find("5")
print("Termina en: "+ str(pos2))

final = len(cadena)
substring = cadena[pos1+1:final]
numerico = float (substring)

print(numerico)
print(type(numerico))
