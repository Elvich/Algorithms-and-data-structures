# Отчет по лабораторной работе №2

## Тема: Система обработки заказов с динамическими скидками (Декоратор + Стратегия)

### 1. Постановка задачи

Разработать систему обработки заказов, где к базовому заказу можно применять различные скидки (паттерн Декоратор), а расчет стоимости доставки осуществляется по разным алгоритмам (паттерн Стратегия).

### 2. Структура решения

- **Order (Компонент)** — абстрактный класс заказа с методами `get_total_cost()` и `get_description()`.
- **BasicOrder** — конкретный заказ, содержащий товары.
- **OrderDiscountDecorator** — базовый декоратор для скидок.
    - **PercentageDiscount** — скидка в процентах.
    - **FixedAmountDiscount** — скидка фиксированной суммой.
    - **LoyaltyDiscount** — скидка для лояльных клиентов.
- **DeliveryCostStrategy** — интерфейс стратегии расчета доставки.
    - **StandardDelivery** — стандартная доставка.
    - **ExpressDelivery** — экспресс-доставка.
    - **FreeDeliveryThreshold** — бесплатная доставка при достижении порога суммы заказа.
- **OrderProcessor** — интеграция заказа и стратегии доставки.

### 3. Пример использования

```python
from order import BasicOrder, PercentageDiscount, FixedAmountDiscount, LoyaltyDiscount
from delivery import StandardDelivery, ExpressDelivery, FreeDeliveryThreshold
from order_processor import OrderProcessor

items = {
    "Laptop": (1000, 1),
    "Mouse": (50, 2),
    "Keyboard": (150, 1)
}
order = BasicOrder(items)
order = PercentageDiscount(order, 10)
order = FixedAmountDiscount(order, 100)
order = LoyaltyDiscount(order, 2)

processor = OrderProcessor(order, StandardDelivery())
print(processor.get_order_summary(distance=10, weight=3))
```

### 4. Результаты работы

В результате работы программы выводится информация о заказе, применённых скидках, стоимости доставки по разным стратегиям и итоговой сумме.

Пример вывода:

```
--- Standard Delivery ---
Order: Laptop x1, Mouse x2, Keyboard x1 | 10% discount | -100 fixed discount | Loyalty discount level 2
Order cost: 855.00
Delivery cost: 71.00
Total: 926.00

--- Express Delivery ---
Order: Laptop x1, Mouse x2, Keyboard x1 | 10% discount | -100 fixed discount | Loyalty discount level 2
Order cost: 855.00
Delivery cost: 142.00
Total: 997.00

--- Free Delivery Threshold ---
Order: Laptop x1, Mouse x2, Keyboard x1 | 10% discount | -100 fixed discount | Loyalty discount level 2
Order cost: 855.00
Delivery cost: 71.00
Total: 926.00
```
