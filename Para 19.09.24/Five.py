a = int(input("Ведите число: "))
isTrue = False

while a>0:
    if a%10 == 7:
        isTrue = True
        break
    a//=10

print(isTrue)