alf = "abcdefghijklmopqrstuvwxyz"
alf = list(alf)

strok = input("Введите строку: ")
strok = list(strok)

isNext = False

for i in alf:
    if isNext:
        print(i)
        break
    elif i is strok[0]:
        isNext = True