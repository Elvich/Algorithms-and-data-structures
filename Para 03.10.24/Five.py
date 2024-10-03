alf = 'abcdefghijklmnopqrstuvwxyz'

strok = input("Введите строку: ")
strok.lower()
mass = strok.split()

newMass = []
for i in mass:
    slovo = ""
    for j in i:
        isTrue = False
        for a in alf:
            if isTrue:
                slovo+=a
                break
            if j==a:
                isTrue = True
                if a=="z":
                    slovo+="a"


    newMass.append(slovo)

newStrok = ""
for i in newMass:
    newStrok += f"{i} "

print(newStrok)