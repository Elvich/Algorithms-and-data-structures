import abc

class Product(abc.ABC):
    def __init__(self, name, manufacturer, price):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price

    @abc.abstractmethod
    def get_info(self): pass


    def matches_conditions(self, **conditions):
        return all(getattr(self, attribute, None) == value for attribute, value in conditions.items())


class Electronics(Product):
    def __init__(self, name, manufacturer, price, device_type):
        super().__init__(name, manufacturer, price)
        self.device_type = device_type

    def get_info(self):
        print(f"Название: {self.name}, Производитель: {self.manufacturer}, Цена: {self.price} руб, Тип устройства: {self.device_type}")


class Clothing(Product):
    def __init__(self, name, manufacturer, price, size):
        super().__init__(name, manufacturer, price)
        self.size = size

    def get_info(self):
        print(f"Название: {self.name}, Производитель: {self.manufacturer}, Цена: {self.price} руб, Размер: {self.size}")


class Food(Product):
    def __init__(self, name, manufacturer, price, expiration_date):
        super().__init__(name, manufacturer, price)
        self.expiration_date = expiration_date

    def get_info(self):
        print(f"Название: {self.name}, Производитель: {self.manufacturer}, Цена: {self.price} руб, Срок годности: {self.expiration_date}")


# Список товаров
products = [
    Electronics("Смартфон", "Samsung", 50000, "Телефон"),
    Electronics("Ноутбук", "Apple", 120000, "Компьютер"),
    Clothing("Куртка", "Nike", 10000, "L"),
    Clothing("Джинсы", "Levi's", 7000, "M"),
    Food("Молоко", "Простоквашино", 120, "10.03.2025"),
    Food("Шоколад", "Аленка", 200, "01.12.2025"),
]

print("Вся информация о товаров:\n")
for product in products:
    product.get_info()

print("-" * 40)

# Поиск товаров напрямую через list comprehension
search_name = "Ноутбук"
search_price = 120000

found_products = [product for product in products if product.matches_conditions(name=search_name, price=search_price)]

# Вывод результатов
print(f"\nРезультаты поиска для названия '{search_name}' и цены '{search_price}' руб:\n")
if found_products:
    for product in found_products:
        product.get_info()

else:
    print("Товары не найдены.")