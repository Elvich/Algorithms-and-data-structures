numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Чётные числа:", even_numbers)
print("Нечётные числа:", odd_numbers)
print()

words = ['orange', 'red', 'green', 'blue', 'white', 'black']
words_to_remove = ['orange', 'black']
filtered_words = list(filter(lambda x: x not in words_to_remove, words))
print("Отфильтрованный список:", filtered_words)
print()

list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 2, 4, 5]
is_sorted_list1 = all(map(lambda x, y: x <= y, list1[:-1], list1[1:]))
is_sorted_list2 = all(map(lambda x, y: x <= y, list2[:-1], list2[1:]))
print("Список list1 отсортирован:", is_sorted_list1)
print("Список list2 отсортирован:", is_sorted_list2)