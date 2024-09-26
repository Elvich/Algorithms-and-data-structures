strok = input("Введите строку: ")
mass = strok.split()

count = 0

for i in mass:
    if "А" in i:
        count+=1

print(count)