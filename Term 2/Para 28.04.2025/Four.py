def remove_negatives(stack):
    temp_stack = []
    while stack:
        element = stack.pop()
        if element >= 0:
            temp_stack.append(element)
    while temp_stack:
        stack.append(temp_stack.pop())
    return stack

stack = [10, -3, 4, -7, 15, 2, -11]
print("Исходный стек:", stack)
filtered_stack = remove_negatives(stack)
print("Стек после удаления отрицательных элементов:", filtered_stack)