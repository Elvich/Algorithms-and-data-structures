class Product():
    def __init__(self, name, price, count = 0):
        self.name = name
        self.price = price
        self.count = count
        self.type = ""

    def get_info(self):
        text = f"{self.name} {self.price} {self.count}"
        text = text if self.type == "" else text + f" {self.type}"
        return text

    def get_has_product(self):
        return "Товар есть" if self.count >=0 else "Товара нет"

    def set_type(self, type):
        self.type = type


pr1 = Product("Яблоки", 120, 3)
pr1.set_type("Фрукт")
pr2 = Product("Счастье", "Бесценно")
pr3 = Product("car", 1000000000, 150)
pr4 = Product("Диван", 90909, 10)
pr5 = Product("God of war", 5400, 1)

print(pr1.get_info())
print(pr1.get_has_product())
print()
print(pr2.get_info())
print(pr2.get_has_product())
print()
print(pr3.get_info())
print(pr3.get_has_product())
print()
print(pr4.get_info())
print(pr4.get_has_product())
print()
print(pr5.get_info())
print(pr5.get_has_product())
print()
