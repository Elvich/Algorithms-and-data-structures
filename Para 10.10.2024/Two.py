a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

for i in range(2, max(a,b)):
    if a%i==0 and b%i==0:
        print(f"Наименьшее общее кратное: {i}")
        break
    if i > min(a,b):
        print("Такого числа нет")
        break