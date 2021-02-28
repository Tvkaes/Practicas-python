print("Calcula tu propina \n")
subtotal = float(input("Ingresa el total de tu consumo MXN\n"))
print("Elige la opcion de el porcentaje de propina que desea dar")
opcion = int (input("1.- 10% \n" + "2.- 15%\n" + "3.- 20% \n"))

if opcion == 1:
    total = subtotal * .10
    total = total + subtotal
    print("Su Total es: ", total)
elif opcion == 2:
    total = subtotal * .15
    total = total + subtotal
    print("Su total es : ", total)
elif opcion == 3:
    total = subtotal * .20
    total = total + subtotal
    print("Su total es: ", total)
