import random

def count_increasing_segments(arr):
    if not arr:
        return 0

    n = len(arr)
    count = 0
    is_increasing = False

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            if not is_increasing:
                count += 1
                is_increasing = True
        else:
            is_increasing = False

    return count


arr = [random.randint(1,100) for i in range(random.randint(1,100))]
print("Массив:", arr)
result = count_increasing_segments(arr)
print("Количество возрастающих участков:", result)