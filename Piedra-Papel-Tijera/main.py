import random
print("PIEDRA PAPEL TIJERA \n")
jugada = input("Introduce tu jugada \n")

pc = random.randint(1,3)
#1-piedra 2-papel 3-tijera
if jugada=="papel" and pc==1:
    print("Ganaste papel vence a piedra")

elif jugada=="piedra" and pc==3:
    print("Ganaste piedra vence a tijeras")

elif jugada=="tijeras" and pc==2:
    print("Ganaste tijeras vence a papel")

else:
    print("Perdiste, Intentalo denuevo")
