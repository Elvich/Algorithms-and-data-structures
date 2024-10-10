strok = input("Введите строку: ")
mass = strok.split()

count = 0

for i in mass:
    if i == i.upper():
        count+=1

print()
print(f"Количество слов состоящее только из заглавныз букв: {count}")