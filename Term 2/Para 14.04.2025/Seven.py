class progression:

    def element(self, j):
        raise NotImplementedError("Метод должен быть реализован в дочерних классах")

    def sum(self, n):
        raise NotImplementedError("Метод должен быть реализован в дочерних классах")

    def get_sum(self, n):
        return f"Сумма первых {n} элементов: {self.sum(n)}"

class arithmetic(progression):

    def __init__(self, first, difference):
        self.first_element = first
        self.difference = difference

    def element(self, j):
        return self.first_element + (j-1) * self.difference

    def sum(self, n):
        return n/2 * (2 * self.first_element + (n - 1) * self.difference)

class geometric(progression):
    def __init__(self, first, denominator):
        self.first_element = first
        self.denominator = denominator

    def element(self, j):
        return self.first_element * (self.denominator ** (j - 1))

    def sum(self, n):
        if self.denominator == 1:
            return n * self.first_element
        return self.first_element * (1 - self.denominator ** n) / (1 - self.denominator)


def print_sum(progressions, n):
    for i, progres in enumerate(progressions, start=1):
        print(f"{i}-ая прогрессия {progres.get_sum(n)}")

progressions = [
    arithmetic(first=1, difference=2),
    geometric(first=1, denominator=2),
    arithmetic(first=3, difference=5),
    geometric(first=2, denominator=3)
]

print_sum(progressions, 5)