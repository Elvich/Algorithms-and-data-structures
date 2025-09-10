from abc import ABC, abstractmethod

class DeliveryCostStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, distance: float, weight: float, order_total: float = 0) -> float:
        pass

class StandardDelivery(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float, order_total: float = 0) -> float:
        return 50 + 2 * distance + 5 * weight

class ExpressDelivery(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float, order_total: float = 0) -> float:
        return 100 + 4 * distance + 10 * weight

class FreeDeliveryThreshold(DeliveryCostStrategy):
    def __init__(self, threshold: float):
        self.threshold = threshold

    def calculate_cost(self, distance: float, weight: float, order_total: float = 0) -> float:
        if order_total >= self.threshold:
            return 0.0
        else:
            return 50 + 2 * distance + 5 * weight
