print("INFORMACION PERSONAL")
print("Como se llama? \n")
nom = input()
if not type(nom) is str:
    raise TypeError("Solo se Permite letras, intentelo otra vez ")

print("Cual es su fecha de nacimiento?")
date = input()
print("Cual es su direccion?")
add = input()
print("cuales son sus metas personales?")
goal = input()

print(f"-nombre: {nom}")
print(f"Fecha de Nacimiento: {date}")
print(f"Direccion: {add}")
print(f"Metas Personales: {goal}")
