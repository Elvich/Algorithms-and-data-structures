n = int(input("Введите число: "))

a1 = 0
a2 = 1
summ = a1+a2

for i in range(3,n+1):
    a = a1 + a2

    a1 = a2
    a2 = a
    summ+=a

print(f"{n}-ое число фибоначчи: {a2}")
print(f"Сумма первых {n} чисел фибоначчи: {summ}")