a = int(input("Введите число: "))

mass = []
b = 0

awhile = a
while awhile>0:
    mass.append(awhile%10)
    awhile//=10

for i in mass:
    b+= i**len(mass)

print(b == a)