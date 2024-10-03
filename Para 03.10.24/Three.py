strok = input("Введите строку: ")
n = int(input("Введите число: "))

newStrok = ""

for i in strok:
    newStrok += f"{i}{'#'*n}"

print(newStrok)