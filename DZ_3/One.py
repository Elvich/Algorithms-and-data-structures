m = int(input("Введите число строк: "))
n = int(input("Введите число столбцов: "))

A = []
for i in range(0,m):
    row = [i]*n
    A.append(row)

print(A)