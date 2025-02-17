import math


class Circle():
    def __init__(self, radius = 1):
        self.radius = radius

    def get_info(self):
        return self.radius

    def get_circumference_length(self):
        return math.pi * self.radius

    def get_square(self):
        return math.pi * self.radius**2


cir = Circle(3)

print(cir.get_info())
print(cir.get_circumference_length())
print(cir.get_square())