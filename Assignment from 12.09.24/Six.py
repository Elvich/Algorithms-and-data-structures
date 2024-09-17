alf = "abcdefghijklmopqrstuvwxyz"
mass = list(alf)
isTrue = True

strok = input("Введите строку: ")

for i in mass:
    if i in strok:
        continue
    else:
        isTrue = False
        break

print(" ")
print(isTrue)