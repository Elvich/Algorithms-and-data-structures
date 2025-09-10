from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def get_total_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

class BasicOrder(Order):
    def __init__(self, items: dict):
        """
        Элементы: dict[str, tuple[float, int]]  # {item_name: (price, quantity)}
        """
        self.items = items

    def get_total_cost(self) -> float:
        return sum(price * qty for price, qty in self.items.values())

    def get_description(self) -> str:
        desc = ', '.join(f"{name} x{qty}" for name, (price, qty) in self.items.items())
        return f"Заказ: {desc}"

class OrderDiscountDecorator(Order):
    def __init__(self, order: Order):
        self._order = order

    def get_total_cost(self) -> float:
        return self._order.get_total_cost()

    def get_description(self) -> str:
        return self._order.get_description()

class PercentageDiscount(OrderDiscountDecorator):
    def __init__(self, order: Order, percent: float):
        super().__init__(order)
        self.percent = percent

    def get_total_cost(self) -> float:
        cost = self._order.get_total_cost()
        return cost * (1 - self.percent / 100)

    def get_description(self) -> str:
        return self._order.get_description() + f" | {self.percent}% скидка"

class FixedAmountDiscount(OrderDiscountDecorator):
    def __init__(self, order: Order, amount: float):
        super().__init__(order)
        self.amount = amount

    def get_total_cost(self) -> float:
        cost = self._order.get_total_cost()
        return max(0, cost - self.amount)

    def get_description(self) -> str:
        return self._order.get_description() + f" | -{self.amount} Фиксированная скидка"

class LoyaltyDiscount(OrderDiscountDecorator):
    def __init__(self, order: Order, loyalty_level: int):
        super().__init__(order)
        self.loyalty_level = loyalty_level

    def get_total_cost(self) -> float:
        cost = self._order.get_total_cost()
        discount = 0.05 * self.loyalty_level  # 5% per level
        return cost * (1 - discount)

    def get_description(self) -> str:
        return self._order.get_description() + f" | Уровень скидокb {self.loyalty_level}"
