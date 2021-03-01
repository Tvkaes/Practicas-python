# Email Slicer

#### Practica en python 
con este codigo se mostrara una manera de cortar un correo electronico y mostrar el usuario y dominio de uno





## Expresiones
##### >>con la funcion strip devuelve el texto introducido pero eliminando los espacios que se hayan introducido

```python 
correo = input("Introduce tu correo electronico \n").strip("")
```
##### >> con la funcion index se ingresaran las palabras del usuario y la parte del dominio excluyendo el "@"
```python
separador = correo.index('@')
```
##### >> dentro de la lista creada por el index se tomara la parte inicial de la lista que es el usuario y despues se tomara el dominio + 1 para no tomar en cuenta el espacio creado por "@"
```python
usuario = correo[:separador]
dominio = correo[separador+1:]

print("Correo: " + correo)
print("Usuario: " + usuario)
print("Dominio: " + dominio)
```
