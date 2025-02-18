import math


class Circle():
    def __init__(self, radius = 1):
        self.radius = radius
        self.color = ""

    def get_info(self):
        return self.radius if self.color == "" else f"{self.radius} {self.color}"

    def get_circumference_length(self):
        return math.pi * self.radius

    def get_square(self):
        return math.pi * self.radius**2

    def set_color(self, color):
        self.color = color


cir = Circle(3)

print(cir.get_info())
print(cir.get_circumference_length())
print(cir.get_square())

print()
cir.set_color("Red")
print(cir.get_info())