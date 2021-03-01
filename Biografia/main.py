import re

print("INFORMACION PERSONAL")

while True:
    print("Como se llama?")
    nom = input()
    res = re.findall(r'[0-9]+', nom)
    res = ','.join(map(str, res))
    if res.isalnum() is False:
        break


print("Cual es su fecha de nacimiento?")
date = input()
print("Cual es su direccion?")
add = input()
print("cuales son sus metas personales?")
goal = input()

print(f"-nombre: {nom}")
print(f"-Fecha de Nacimiento: {date}")
print(f"-Direccion: {add}")
print(f"-Metas Personales: {goal}")
