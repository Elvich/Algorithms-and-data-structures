def result_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Результат выполнения функции {func.__name__}: {result}")
        return result
    return wrapper

@result_decorator
def add(a, b):
    return a + b

@result_decorator
def multiply(a, b, c):
    return a * b * c

add(5, 3)
multiply(2, 3, 4)