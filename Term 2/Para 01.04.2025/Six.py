from functools import reduce

numbers = [10, 3, 5, 8, 7, 2, 9, 4, 6, 1]
even_position_numbers = numbers[::2]
sorted_numbers = sorted(even_position_numbers)
total_sum = reduce(lambda x, y: x + y, sorted_numbers) if sorted_numbers else 0

print("Исходный список:", numbers)
print("Числа на четных позициях (по возрастанию):", sorted_numbers)
print("Сумма этих чисел:", total_sum)