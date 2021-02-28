# Adivina el Numero

#### Practica en python 

En este codigo se presenta un juego de azar para adivinar el numero random que se genero del 1 al 10 , teniendo 5 oportunidades de adivinarlo

## Teoria

La clase Random proporciona un generador de números aleatorios que es más flexible que la función estática random de la clase Math. Para crear una secuencia de números aleatorios tenemos que seguir los siguientes pasos: Proporcionar a nuestro programa información acerca de la clase Random.

## Expresiones
##### >> Se guarda en una variable el numero random generado del 1 al 10
```python
import random

numero = random.randint(1, 10)
```
##### >> Se inicia un ciclo while y un contador en 0 , durante cada intento se sumara un intento a la variable y al terminar el 5 intento se saldra del while o una vez que se adivine el numero 
```python
while veces < 5:
    veces = veces + 1
    number = input("Introduce un numero del 1 al 10")
    if int(number) < numero:
        print("El numero es mas alto al introducido")
    if int(number) > numero:
        print("el numero es mas bajo al introducido")
    elif int(number) == numero:
        break
```
