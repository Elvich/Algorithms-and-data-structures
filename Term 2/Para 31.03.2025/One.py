import random

lam = lambda a: a * random.randint(1,100)

cheslo = int(input("Введите случайное число: "))
print(f"а) Умножение на случайное чиело: {lam(cheslo)}")
print()

mass = [random.randint(1,1000) for i in range(random.randint(1, 25))]

print(f"б) Массив: {mass}")
print()
dell = random.randint(12, 13)
mass2 = [element for element in mass if element%dell==0]
print(f"Из них на {dell} делится {mass2}")
print()

mass = [random.random() for i in range(random.randint(1,26))]
lam3 = lambda massLam: len(massLam)
print(f"в) Список всех чисел: {mass}")
print()
print(f"Колличество вещественных чисел: {lam3(mass)}")
