def validate_numeric_arguments(func):
    # Декоратор для проверки, что все аргументы функции являются числами.

    def wrapper(*args, **kwargs):
        # Проверяем позиционные аргументы
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"Аргумент {arg} не является числом!")

        # Проверяем именованные аргументы
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"Аргумент {key} со значением {value} не является числом!")

        # Если все аргументы корректны, вызываем оригинальную функцию
        return func(*args, **kwargs)

    return wrapper



@validate_numeric_arguments
def add_numbers(a, b):
    return a + b

# Тестирование
try:
    print(add_numbers(5, 10))
    print(add_numbers("5", 10))
except ValueError as e:
    print(e)