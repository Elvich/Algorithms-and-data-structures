n = int(input("Введите число: "))
isSover = False

if n>0:
    summ = 0
    for i in range(1, n):
        if n%i==0:
            summ+=i

    if summ == n:
        isSover = True


if isSover:
    print(f"{n} - совершенное чило ")
else:
    print(f"{n} - не совершенное чило ")