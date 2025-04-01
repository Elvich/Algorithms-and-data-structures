def calculate_ratios(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    total_count = len(arr)
    if total_count == 0:
        return (0, 0, 0)
    positive_ratio = positive_count / total_count
    negative_ratio = negative_count / total_count
    zero_ratio = zero_count / total_count
    return (positive_ratio, negative_ratio, zero_ratio)

arr1 = [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]
result1 = calculate_ratios(arr1)
print(f"Массив {arr1} → {result1}")

arr2 = [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]
result2 = calculate_ratios(arr2)
print(f"Массив {arr2} → {result2}")