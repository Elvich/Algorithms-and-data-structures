from functools import reduce

numbers = [12, 7, 9, 4, 11, 6, 15, 3, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
odd_numbers_sorted = sorted(odd_numbers, reverse=True)
product = reduce(lambda x, y: x * y, odd_numbers_sorted) if odd_numbers_sorted else 0

print("Исходный список:", numbers)
print("Нечетные числа (по убыванию):", odd_numbers_sorted)
print("Произведение нечетных чисел:", product)