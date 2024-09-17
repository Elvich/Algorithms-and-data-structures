from math import sqrt

a = int(input("Введите длину первой стороны: "))
b = int(input("Введите длину втрой стороны: "))
c = int(input("Введите длину третей стороны: "))

p = (a+b+c)/2

print((p*(p-a)*(p-b)*(p-c)**0.5))