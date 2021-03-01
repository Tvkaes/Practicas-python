# Letras de canciones

#### Practica en python 
en esta practica se representa la lectura de datos de archivos externos en este caso archivos .txt



## Expresiones
##### >>Con la funcion open abriremos un archivo txt con la informacion dentro con permiso de lectura

```python 
x = open('valentin.txt', 'r')
```
##### >>Con la funcion read se leera la informacion que contiene el archivo y se imprimira la informacion guardada en la variable 

```python 
        valentin1 = x.read()
        print(valentin1)
        x.close()
```
