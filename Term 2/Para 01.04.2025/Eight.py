def args_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Аргументы функции {func.__name__}:")
        for i, arg in enumerate(args, start=1):
            print(f"  Аргумент {i}: значение = {arg}, тип = {type(arg)}")
        for key, value in kwargs.items():
            print(f"  Ключевой аргумент {key}: значение = {value}, тип = {type(value)}")
        return func(*args, **kwargs)
    return wrapper

@args_decorator
def add(a, b):
    return a + b

@args_decorator
def greet(name, age=None):
    if age:
        return f"Hello, {name}! You are {age} years old."
    else:
        return f"Hello, {name}!"

add(5, 3)
greet("Alice", age=30)
greet("Bob")