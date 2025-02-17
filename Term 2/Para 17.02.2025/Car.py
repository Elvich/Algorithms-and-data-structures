class Car:
    def __init__(self, stamp, model, year, mileage = 0):
        self.stamp = stamp
        self.model = model
        self.year = year
        self.mileage = mileage

    def get_info(self):
        return f"Марка - {self.stamp}, Модель - {self.model}, Год выпуска - {self.year}, Пробег - {self.mileage}"

    def get_need_service(self):
        return "Необходимо пройти обслуживание" if self.mileage >= 10000 else f"До ближайшего тех обслуживания еще {10000 - self.mileage}км"

car1 = Car("Porshe", "911", 2025)
car2 = Car("BMW", "m5", 2017, 7500)
car3 = Car("Mersedes", "Maybach S-Класс Седан S 580", 2010, 12000)
car4 = Car("Lada", "Vesta", 2024, 534)
car5 = Car("KIA", "Rio", 2000, 300000)

print(car1.get_info())
print(car1.get_need_service())
print()
print(car2.get_info())
print(car2.get_need_service())
print()
print(car3.get_info())
print(car3.get_need_service())
print()
print(car4.get_info())
print(car4.get_need_service())
print()
print(car5.get_info())
print(car5.get_need_service())
print()
