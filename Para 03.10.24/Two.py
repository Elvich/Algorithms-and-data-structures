strok = input("Введите строку: ")
mass = strok.split(",")

newMass = []

for i in mass:
    slovo = ""
    slovo += i[::2]
    slovo += i[::-2]
    newMass.append(slovo)

newStrok = ""
for i in newMass:
    newStrok += f"{i},"

print(newStrok)
