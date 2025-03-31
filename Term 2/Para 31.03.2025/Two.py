import random

kor = [('English',88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lam = lambda korLam: sorted(korLam, key=lambda a: a[1])
print(lam(kor))
print()

lam2 = lambda massLam: [elemet for elemet in massLam if elemet.lower() == elemet[::-1].lower()]
words = [ "Кит",
    "Дом",
    "Радар",  # палиндром
    "Собака",
    "Уровень",
    "Лес",
    "Шалаш",  # палиндром
    "Море",
    "Город",
    "Зима",
    "Лето",
    "Путь"]
print(lam2(words))
print()

mass = [random.randint(1,1000) for i in range(random.randint(1, 25))]
lam3 = lambda massLam: [(max(massLam), massLam.index(max(massLam))),(min(massLam), massLam.index(min(massLam)))]
print(f"Список: {mass}")
mass = lam3(mass)
print(f"Максимальное число: {mass[0][0]}, по индексу {mass[0][1]}")
print(f"Минимальное число: {mass[1][0]}, по индексу {mass[1][1]}")