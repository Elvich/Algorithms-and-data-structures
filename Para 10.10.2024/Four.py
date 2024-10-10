n = int(input("Введите количество элементов списка: "))
mass = []
for i in range(0,n):
    chislo = int(input(f"Введите {i+1}-ое число: "))
    mass.append(chislo)

print()
k = int(input("Введите число K: "))-1
l = int(input("Введите число L: "))-1

if k<=0:
    print("'K' должно быть больше 1")
elif k>l:
    print("'K' не может быть больше 'L'")
elif l>n-1:
    print("'L' не может быть больше 'N'")
else:
    count = 0
    for i in range(0,n):
        if i>=k and i<=l: continue

        count+=mass[i]

    print()
    print(f"Сумма = {count}")
