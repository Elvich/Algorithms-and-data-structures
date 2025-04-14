def validate_return_value(validation_func, default_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Вызываем оригинальную функцию и получаем её результат
            result = func(*args, **kwargs)

            # Проверяем корректность результата
            if not validation_func(result):
                print(f"Некорректное значение: {result}. Используется значение по умолчанию: {default_value}")
                return default_value  # Возвращаем предопределенное значение

            # Если результат корректен, возвращаем его
            return result

        return wrapper

    return decorator



def is_positive_number(x):
    return isinstance(x, (int, float)) and x > 0

@validate_return_value(is_positive_number, default_value=1)
def get_number():
    import random
    return random.randint(-10, 10)

for _ in range(5):
    print(get_number())