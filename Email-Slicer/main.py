print("SEPARADOR DE EMAIL \n")
correo = input("Introduce tu correo electronico \n").strip("")

separador = correo.index('@')
usuario = correo[:separador]
dominio = correo[separador+1:]

print("Correo: " + correo)
print("Usuario: " + usuario)
print("Dominio: " + dominio)

