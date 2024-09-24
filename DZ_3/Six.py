x = int(input("Введите число: "))

if x%400==0:
    print("Високосный")
elif x%100==0:
    print("невисокосные")
elif x%4==0:
    print("Високосный")
else:
    print("невисокосные")