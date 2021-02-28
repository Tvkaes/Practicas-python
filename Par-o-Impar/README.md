# Par o Impar

#### Practica en python 

Codigo para saber si el numero introducido por el usuario es par o impar 

## Teoria

Un número par es un número que es múltiplo de 2, osea que lo podemos expresar como 2 multiplicado por otro número y esa expresión resulta equivalente. Un número impar es un número que no es múltiplo de 2.

Un número par es divisible por 2, es decir que al dividir el número por 2 el resto de la división es 0, en cambio, la división entre un número impar y 2 siempre tendrá resto 1. Podemos usar este hecho para programar un algoritmo que compruebe si un número es par o impar.

## Expresion
```python
n = int(numero)
if (n % 2) == 0:
    print('el numero  es par')
else:
    print('el numero  es impar')
```
