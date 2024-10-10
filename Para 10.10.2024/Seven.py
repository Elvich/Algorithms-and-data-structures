n = int(input("Введите количество элементов списка: "))
mass = []
for i in range(0,n):
    chislo = int(input(f"Введите {i+1}-ое число: "))
    mass.append(chislo)

max1 = mass[0]
max2 = mass[1]

for i in range(2, n):
    if mass[i]>=max1:
        max1 = max2
        max2 = mass[i]

print()
print(f"Наибольшие числа: {max1} {max2}")

min1 = mass[len(mass)-1]
min2 = mass[len(mass)-2]

for i in range(n-1, -1, -1):
    if mass[i]<=min1:
        min1 = min2
        min2 = mass[i]

print()
print(f"Наименьшие числа: {min1} {min2}")