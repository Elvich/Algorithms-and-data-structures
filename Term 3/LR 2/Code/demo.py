from order import BasicOrder, PercentageDiscount, FixedAmountDiscount, LoyaltyDiscount
from delivery import StandardDelivery, ExpressDelivery, FreeDeliveryThreshold
from order_processor import OrderProcessor

# Пример заказа
items = {
    "Ноутбук": (1000, 1),
    "Мышь": (50, 2),
    "Клавиатура": (150, 1)
}

# Базовый заказ
order = BasicOrder(items)
# Применяем скидки: 10% + 100 фиксированная + лояльность 2 уровня
order = PercentageDiscount(order, 10)
order = FixedAmountDiscount(order, 100)
order = LoyaltyDiscount(order, 2)

# Стратегии доставки
standard = StandardDelivery()
express = ExpressDelivery()
free_threshold = FreeDeliveryThreshold(1200)

# Интеграция и вывод
print("--- Стандартная доставка ---")
processor = OrderProcessor(order, standard)
print(processor.get_order_summary(distance=10, weight=3))

print("\n--- Экспресс-доставка ---")
processor = OrderProcessor(order, express)
print(processor.get_order_summary(distance=10, weight=3))

print("\n--- Бесплатная доставка ---")
processor = OrderProcessor(order, free_threshold)
print(processor.get_order_summary(distance=10, weight=3))
