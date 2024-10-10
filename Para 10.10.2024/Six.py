n = int(input("Введите количество элементов списка: "))
mass = []
for i in range(0,n):
    chislo = int(input(f"Введите {i+1}-ое число: "))
    mass.append(chislo)

mincheslo = min(mass)
maxcheslo = max(mass)

isTrue = False
count = 0
for i in mass:
    if isTrue:
        count+=i
        if i==maxcheslo:
            break
    else:
        if i==mincheslo:
            isTrue=True
            count+=i

print()
print(f"Сумма чисел: {count}")