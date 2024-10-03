strok = input("Введите строку: ")
mass = strok.split(",")

slovo = ""

for i in mass:
    if len(i) > len(slovo):
        slovo = i

print(slovo)