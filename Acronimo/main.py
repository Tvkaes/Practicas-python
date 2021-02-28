print("GENERADOR DE ACRONIMOS \n")
texto = input("introduce el termino para el acronimo \n")
termino = (texto.replace('de','')).split()
acronimo = ""

for palabra in termino:
    acronimo = acronimo + palabra[0].upper()

print("el acronimo del termino: " + str(texto) + " es " + acronimo)