n = int(input("Введите число: "))

k = 0

while True:
    if 3**(k+1)<n:
        k+=1
    else:
        break

print(k)