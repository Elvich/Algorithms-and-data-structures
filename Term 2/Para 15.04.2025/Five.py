def replace_series(A, L):
    result = []
    current_value = A[0]
    count = 1

    for i in range(1, len(A)):
        if A[i] == current_value:
            count += 1
        else:
            if count < L:
                result.append(0)
            else:
                result.extend([current_value] * count)
            current_value = A[i]
            count = 1

    if count < L:
        result.append(0)
    else:
        result.extend([current_value] * count)

    return result

A = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]
L = 3
B = replace_series(A, L)
print("Исходный массив:", A)
print("Модифицированный массив:", B)