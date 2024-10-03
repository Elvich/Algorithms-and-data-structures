strok = input("Введите строку: ")
mass = strok.split()

newMass = []

for i in mass:
    if newMass.count(i): continue

    newMass.append(i)

newStrok = ""
for i in newMass:
    newStrok += f"{i} "

print(newStrok)