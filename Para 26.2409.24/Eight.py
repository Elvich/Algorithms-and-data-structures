strok = input("Введите строку: ")
mass = strok.split()
mass.sort()

otvet = ""
for i in mass:
    otvet += f"{i} "

print(otvet)