n = int(input("Введите количество элементов списка: "))
mass = []
for i in range(0,n):
    chislo = int(input(f"Введите {i+1}-ое число: "))
    mass.append(chislo)

print()
neChetMass = []
for i in range(0,n):
    if mass[i]%2==0:
        print(mass[i])
    else:
        neChetMass.append(mass[i])

print()
for i in range(len(neChetMass)-1, -1, -1):
    print(neChetMass[i])
