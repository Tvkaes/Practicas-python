# Piedra Papel Tijera

#### Practica en python 
La funcion del codigo consiste en generar de manera aleatoria un numero del 1 al 3 (siendo piedra ,papel y tijera respectivamente)
## Teoria
Los jugadores cuentan juntos «1, 2, 3…, ¡piedra, papel o tijera!»

Justo al acabar muestran todos al mismo tiempo una de sus manos, de modo que pueda verse el elemento que cada uno ha elegido:

##### Piedra: un puño cerrado.
##### Papel: todos los dedos extendidos, con la palma de la mano de lado, mirando hacia abajo o hacia arriba
##### Tijera: dedos índice y corazón extendidos y separados formando una «V».
El objetivo es vencer al oponente seleccionando el arma que gana, según las siguientes reglas:

###### La piedra aplasta la tijera. (Gana la piedra.)
###### La tijera corta el papel. (Gana la tijera.)
###### El papel envuelve la piedra. (Gana el papel.)
En caso de empate (que dos jugadores elijan el mismo elemento o que tres jugadores elijan cada uno un objeto distinto), se juega otra vez.


## Expresiones
##### >> se genera un numero random del 1 al 3 para la jugada de la computadora
```python 
import random
pc = random.randint(1,3)
#1-piedra 2-papel 3-tijera
```
##### >> Con tres comparaciones se decidira si gana el usuario o la computadora 

```python 
if jugada=="papel" and pc==1:
    print("Ganaste papel vence a piedra")

elif jugada=="piedra" and pc==3:
    print("Ganaste piedra vence a tijeras")

elif jugada=="tijeras" and pc==2:
    print("Ganaste tijeras vence a papel")
```

