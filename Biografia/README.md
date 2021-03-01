# Biografia

#### Practica en python 

Con este codigo se mostrara cuando un usuario ingrese un int en vez de un String y mostrara el mensaje de error utilizando **expresiones regulares**

## Teoria
Una expresión regular (o RE, por sus siglas en inglés) especifica un conjunto de cadenas que coinciden con ella; las funciones de este módulo permiten comprobar si una determinada cadena coincide con una expresión regular dada (o si una expresión regular dada coincide con una determinada cadena, que se reduce a lo mismo).



## Expresiones
##### >> usando las expresiones regulares se analiza los datos introducidos por el usuario y se verifica que no haya ingresado datos numericos , si es asi se volvera a preguntar que ingrese los datos nuevamente
```python
import re

while True:
    nom = input()
    res = re.findall(r'[0-9]+', nom)
    res = ','.join(map(str, res))
    if res.isalnum() is False:
        break
```
