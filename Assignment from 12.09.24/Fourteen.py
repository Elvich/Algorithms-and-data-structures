a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a%2==0 or b%2==0:
    print(a**2 + b**2)
else:
    print(abs(a**2 - 5**2))