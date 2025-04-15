def find_closest_element(arr, R):
    closest_element = arr[0]
    min_diff = abs(arr[0] - R)

    for num in arr:
        current_diff = abs(num - R)
        if current_diff < min_diff:
            min_diff = current_diff
            closest_element = num

    return closest_element


arr = [4, 7, 1, 9, 5]
R = 6
result = find_closest_element(arr, R)
print("Наиболее близкий элемент:", result)