n = int(input("Введите число: "))
A = []

isTrue = True
for i in range(0,n):
    row = []
    for j in range(0,n):
        if isTrue:
            row.append("w")
            isTrue = False
        else:
            row.append("b")
            isTrue = True
    A.append(row)



print(A)