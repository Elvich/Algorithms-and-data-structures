a = input("Введите меньшую строку: ")
b = input("Введите большую строку: ")

a = list(a)
isTrue = True

for i in a:
    if i in b:
        continue
    else:
        isTrue = False
        break

print("")
print(isTrue)