def find_closest_pair(arr, R):
    if len(arr) < 2: 
        return None

    min_diff = float('inf')
    closest_pair = None

    for i in range(len(arr) - 1):
        current_sum = arr[i] + arr[i + 1]
        diff = abs(current_sum - R)

        if diff < min_diff:
            min_diff = diff
            closest_pair = (arr[i], arr[i + 1])

    return closest_pair


arr = [3, 5, 7, 1, 9]
R = 8
result = find_closest_pair(arr, R)
print("Ближайшая пара:", result)