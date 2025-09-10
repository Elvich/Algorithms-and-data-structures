from order import Order
from delivery import DeliveryCostStrategy

class OrderProcessor:
    def __init__(self, order: Order, delivery_strategy: DeliveryCostStrategy):
        self.order = order
        self.delivery_strategy = delivery_strategy

    def calculate_delivery_cost(self, distance: float, weight: float) -> float:
        return self.delivery_strategy.calculate_cost(distance, weight, self.order.get_total_cost())

    def get_order_summary(self, distance: float, weight: float) -> str:
        order_cost = self.order.get_total_cost()
        delivery_cost = self.calculate_delivery_cost(distance, weight)
        total = order_cost + delivery_cost
        return (
            f"{self.order.get_description()}\n"
            f"Стоимость заказа: {order_cost:.2f}\n"
            f"Стоимость доставки: {delivery_cost:.2f}\n"
            f"Итого: {total:.2f}"
        )
