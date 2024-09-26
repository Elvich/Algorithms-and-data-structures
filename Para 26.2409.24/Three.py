strok = str(input("Введите строку: "))
mass = strok.split()

count = 0

for i in mass:
    for j in i:
        if j.lower() == j:
            count+=1

print(count)