print("NUMERO PALINDROMO \n")
numero = input("Ingresa un numero \n")

x = list(numero)
reversa =[x[i-1] for i in range(len(x),0,-1)]
if x == reversa:
    print("si es")
else:
    print("no es")



