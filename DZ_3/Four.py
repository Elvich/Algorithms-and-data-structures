n = int(input("Введите число: "))
A = []
for i in range(0,n):
    row = []
    for j in range(0,n):
        if (i+j+1)==n:
            row.append(1)
        else:
            row.append(0)
    A.append(row)

print(A)