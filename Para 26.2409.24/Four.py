strok = str(input("Введите строку: "))
mass = strok.split()

print(f"{mass[0][1::-1]}{mass[0][2:]} {mass[1][1::-1]}{mass[1][2:]}")