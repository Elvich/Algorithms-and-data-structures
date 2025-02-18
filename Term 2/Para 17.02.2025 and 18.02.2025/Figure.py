import abc
import math

class Figure(abc.ABC):

    @abc.abstractmethod
    def get_info (self): pass

    @abc.abstractmethod
    def get_area (self): pass

    @abc.abstractmethod
    def get_square (self): pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_info(self):
        return f"Это прямоугольник со сторонами {self.width} и {self.height}"

    def get_area(self): return 2*(self.width + self.height)

    def get_square(self): return  self.width * self.height

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_info(self):
        return f"Это круг с радиусом {self.radius}"

    def get_area(self): return math.pi * self.radius

    def get_square(self): return math.pi * self.radius**2

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c


    def get_info(self):
        return f"Это треугольник со сторонами {self.side_a}, {self.side_b} и {self.side_c}"

    def get_area(self): return self.side_a + self.side_b + self.side_c

    def get_square(self):
        p = self.side_a + self.side_b + self.side_c
        s = math.sqrt(p*(p-self.side_a)*(p-self.side_b)*(p-self.side_c))
        return s


rectangle = Rectangle(5,2)

print(rectangle.get_info())
print(f"P = {rectangle.get_area()}")
print(f"S = {rectangle.get_square()}")
print()

circle = Circle(5)

print(circle.get_info())
print(f"P = {circle.get_area()}")
print(f"S = {circle.get_square()}")
print()

triangle = Triangle(2, 4, 7)

print(triangle.get_info())
print(f"P = {triangle.get_area()}")
print(f"S = {triangle.get_square()}")
print()
