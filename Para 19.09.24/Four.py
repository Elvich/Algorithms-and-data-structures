a = input("Ведите число: ")

if len(a)!=4: print("Число должно быть четырехзначным!")

print(f"{a[0:3:2]} и {a[1:4:2]}" )