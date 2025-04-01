from functools import reduce

numbers = [20, 10, 5, 25, 3, 14, 18, 7, 1]
filtered_numbers = list(filter(lambda x: x < 15, numbers))
sorted_numbers = sorted(filtered_numbers, reverse=True)
total_sum = reduce(lambda x, y: x + y, sorted_numbers) if sorted_numbers else 0

print("Исходный список:", numbers)
print("Числа меньше 15 (по убыванию):", sorted_numbers)
print("Сумма этих чисел:", total_sum)