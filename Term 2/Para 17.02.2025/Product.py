class Product():
    def __init__(self, name, price, count = 0):
        self.name = name,
        self.price = price,
        self.count = count

    def get_info(self):
        return f"{self.name}  {self.price} {self.count}"

    def get_has_product(self):
        return "Товар есть" if self.count >=0 else "Товара нет"


pr1 = Product("Яьлоки", 120, 3)
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
