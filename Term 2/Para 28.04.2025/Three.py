def find_extreme_in_stack(stack, find_max):
    temp_stack = []
    extreme_value = None

    while stack:
        element = stack.pop()
        if extreme_value is None or (find_max and element > extreme_value) or (not find_max and element < extreme_value):
            extreme_value = element
        temp_stack.append(element)

    while temp_stack:
        stack.append(temp_stack.pop())

    return extreme_value

stack = [10, 3, 4, 7, 15, 2, 11]
print("Исходный стек:", stack)
max_value = find_extreme_in_stack(stack, True)
print("Максимальный элемент:", max_value)
min_value = find_extreme_in_stack(stack, False)
print("Минимальный элемент:", min_value)