# Acronimos

#### Practica en python 

Codigo para generar acronimos una vez que el ususario introduzca la frase o palabras

## Teoria

Un acrónimo, en lingüística moderna puede ser una sigla que se pronuncia como una palabra ―y que por el uso acaba por incorporarse al léxico habitual en la mayoría de casos, ​ como láser o radar ― o también puede ser un vocablo formado al unir parte de dos ―o a veces más― palabras.

## Expresiones
##### >> Se eliminan los conectores de palabras en este caso "de"
```python
termino = (texto.replace('de','')).split()
```
##### >> Se inicia un ciclo para tomar la primera letra de cada palabra y se vuelven mayusculas
```python
for palabra in termino:
    acronimo = acronimo + palabra[0].upper()
```
