mass = []
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
mass.append(a)
mass.append(b)
mass.append(c)
sorted(mass)

print("")
print(mass[2]//mass[1] == mass[1]//mass[0])