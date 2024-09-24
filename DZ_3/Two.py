n = int(input("Введите число: "))
A = []
for i in range(0,n):
    row = []
    for j in range(0,n):
        if j==i:
            row.append(1)
        else:
            row.append(0)
    A.append(row)

print(A)
