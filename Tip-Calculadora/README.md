# Calcular Tips

#### Practica en python 
Se calcula el monto del tip(propina) segun tu total de consumo y el porcentaje de tip(propina)
## Teoria
La propina es una recompensa generalmente económica que se otorga como agradecimiento por un buen servicio y por el producto consumido.​En la mayoría de los sitios, el cliente decide si da o no una propina y el monto de ésta.

Es costumbre para algunos países dejar propina y en otros es una obligación, como Estados Unidos. En el país norteamericano, una propina estándar en un restaurante puede llegar al 25% de la cuenta. Según señala la BBC, dejar 15% es aceptable. Y ofrecer una propina de 10% o menos puede ser considerado un insulto.




## Expresiones
##### >> se ingresa en float el subtotal a pagar por el consumo 
```python 
subtotal = float(input("Ingresa el total de tu consumo MXN\n"))
```
##### >> se ingresa la opcion del porcentaje en cuestion de propina

```python 
opcion = int (input("1.- 10% \n" + "2.- 15%\n" + "3.- 20% \n"))
```
##### >> se calcula el monto de la propina segun el porcentaje elegido y el monto del subtotal
```python 
if opcion == 1:
    total = subtotal * .10
    total = total + subtotal
    print("Su Total es: ", total)
elif opcion == 2:
    total = subtotal * .15
    total = total + subtotal
    print("Su total es : ", total)
elif opcion == 3:
    total = subtotal * .20
    total = total + subtotal
    print("Su total es: ", total)
```
