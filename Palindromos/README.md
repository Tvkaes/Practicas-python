# Numero Palindromo

#### Practica en python 
en esta practica se representa la lectura de datos de archivos externos en este caso archivos .txt

## Teoria
Un número natural es un palíndromo si se lee igual de izquierda a derecha y de derecha a izquierda. Por ejemplo, 14941 es un palíndromo, mientras que 81924 no lo es.

## Expresiones
##### >> El numero introducido por el usuario se introducira en una lista y guardandola en una variable nueva 

```python 
x = list(numero)
```
##### >> Con el ciclo for se invertiran las variables numero y x para despues compararse entre ellos 

```python 
reversa =[x[i-1] for i in range(len(x),0,-1)]

if x == reversa:
    print("si es")
else:
    print("no es")
```
