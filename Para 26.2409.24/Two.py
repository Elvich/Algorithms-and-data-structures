strok = str(input("Введите строку: "))
mass = strok.split()

word = mass[0]

for i in mass:
    if len(word)>len(i):
        word = i

print(len(word))