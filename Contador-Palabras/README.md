# Contador de Palabras

#### Practica en python 

en esta practica se hizo un contador de palabras en un parrafo ingresado por el usuario 
## Teoria
Contador de palabras y contador de caracteres es una herramienta que te permite contar la cantidad de palabras o de caracteres que posee un texto. ... Además, el contador de palabras muestra automáticamente las diez palabras más utilizadas y la densidad de las mismas dentro del artículo que estás escribiendo.


## Expresiones
##### >>con la funcion split se crea una lista separa las palabras del parrafo introducido por ejemplo:

```python 
texto=["hola","ayer","hoy"]
```
##### >> con la funcion len se contaran el numero de palabras que habra en este lista que se creo
```python
texto = input("Ingresa el texto \n")
print("El texto es: "+ texto)
contador= len(texto.split())
```
