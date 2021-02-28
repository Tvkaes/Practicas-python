while True:
    print("Letras de Canciones")
    print("Selecciona una cancion  para saber la letra\n")
    print("1.- Vete ya - Valentin Elizalde")
    print("2.- Te quiero asi - Valentin Elizalde")
    print("3.- Cuando Yo Me Muera - Valentin Elizalde")
    print("4.- salir")
    opc = int(input())

    if opc == 1:
        x = open('valentin.txt', 'r')
        valentin1 = x.read()
        print(valentin1)
        x.close()
        pass
    if opc == 2:
        x = open('valentin2.txt', 'r')
        valentin1 = x.read()
        print(valentin1)
        x.close()
        pass
    elif opc == 3:
        x = open('valentin3.txt', 'r')
        valentin1 = x.read()
        print(valentin1)
        x.close()
        pass
    if opc == 4:
        break


