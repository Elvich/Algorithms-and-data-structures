import random

def remove_elements_with_two_occurrences(arr):
    from collections import Counter

    count = Counter(arr)
    result = [x for x in arr if count[x] != 2]

    return len(result), result


arr = [random.randint(1,100) for i in range(random.randint(1,10))]
print("Содержание изначально массива массива:", arr)
print()
size, new_arr = remove_elements_with_two_occurrences(arr)
print("Размер нового массива:", size)
print("Содержимое нового массива:", new_arr)