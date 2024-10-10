n = int(input("Введите количество натуральных чисел: "))
mass = []
for i in range(0,n):
    chislo = int(input(f"Введите {i+1}-ое число: "))
    mass.append(chislo)
print()
for i in range(0,n):
    chislo = mass[i]
    count = 0
    while chislo>0:
        if(chislo%10)%2==0:
            count+=1
        chislo//=10
    print(f"В числе №{i+1} - {count} ")