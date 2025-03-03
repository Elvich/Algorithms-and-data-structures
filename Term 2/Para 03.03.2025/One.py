import abc

class Car(abc.ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abc.abstractmethod
    def get_info(self): pass

    def matches_conditions(self, **conditions):
        return all(getattr(self, attribute, None) == value for attribute, value in conditions.items())


class PassengerCar(Car):
    def __init__(self, brand, model, year, body_type):
        super().__init__(brand, model, year)
        self.body_type = body_type

    def get_info(self):
        print(f"Бренд: {self.brand}, Модель: {self.model}, Год: {self.year}, Тип кузова: {self.body_type}")


class Truck(Car):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def get_info(self):
        print(f"Бренд: {self.brand}, Модель: {self.model}, Год: {self.year}, Грузоподьемность: {self.load_capacity} tons")


class Bus(Car):
    def __init__(self, brand, model, year, seat_count):
        super().__init__(brand, model, year)
        self.seat_count = seat_count

    def get_info(self):
        print(f"Бренд: {self.brand}, Модель: {self.model}, Год: {self.year}, Колличество мест: {self.seat_count}")




cars = [
    PassengerCar("Toyota", "Camry", 2020, "Sedan"),
    PassengerCar("Honda", "Civic", 2018, "Hatchback"),
    Truck("MAN", "TGS", 2019, 15),
    Bus("Mercedes", "Sprinter", 2021, 20),
    Truck("Volvo", "FH16", 2022, 25),
    Bus("Ikarus", "280", 1995, 40),
]

print("Вся информация об автомобилях:\n")
for car in cars:
    car.get_info()


print("-" * 40)


search_brand = "Mercedes"
search_year = 2021

print(f"\n Поиск по бренду '{search_brand}' и году выпуска '{search_year}':\n")
found_cars = [car for car in cars if car.matches_conditions(brand=search_brand, year=search_year)]
if found_cars:
    for car in found_cars:
        car.get_info()
        print("-" * 40)
else:
    print("No cars found.")