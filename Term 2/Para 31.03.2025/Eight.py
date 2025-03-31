bases = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
exponents = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(lambda x, y: x**y, bases, exponents))

print(result)