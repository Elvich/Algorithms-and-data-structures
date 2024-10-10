n = int(input("Введите количество элементов списка: "))
mass = []
for i in range(0,n):
    chislo = int(input(f"Введите {i+1}-ое число: "))
    mass.append(chislo)

print()
k = int(input("Введите число  K: "))

newMass = []
for i in mass:
    if i<k:
        newMass.append(i)

print()
print(sorted(newMass))