import DoublyLinkedList

class Order:
    def __init__(self, dish_name, price, quantity, date, status="в обработке"):
        self.dish_name = dish_name
        self.price = price
        self.quantity = quantity
        self.date = date
        self.status = status

    def __str__(self):
        return f"{self.dish_name} | {self.price} руб x {self.quantity} | {self.date} | Статус: {self.status}"


order_list = DoublyLinkedList.DoublyLinkedList()
order_list.append(Order("Паста", 500, 2, "2025-04-05"))
order_list.append(Order("Салат", 300, 1, "2025-04-05", "готов"))

order_list.display_forward()