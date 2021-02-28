import random

numero = random.randint(1, 10)
print("ADIVINA EL NUMERO")
print("Tienes 5 intentos \n")
veces = 0
while veces < 5:
    veces = veces + 1
    number = input("Introduce un numero del 1 al 10")
    if int(number) < numero:
        print("El numero es mas alto al introducido")
    if int(number) > numero:
        print("el numero es mas bajo al introducido")
    elif int(number) == numero:
        break
print("numero de intentos: ", veces)
