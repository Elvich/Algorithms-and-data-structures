def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_stack(stack):
    temp_stack = []
    while stack:
        element = stack.pop()
        if is_prime(element):
            temp_stack.append(element)
    while temp_stack:
        stack.append(temp_stack.pop())
    return stack

stack = [10, 3, 4, 7, 15, 2, 11]
print("Исходный стек:", stack)
filtered_stack = filter_stack(stack)
print("Стек после фильтрации:", filtered_stack)