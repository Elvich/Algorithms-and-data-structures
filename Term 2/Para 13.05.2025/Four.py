
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class Purchase:
    def __init__(self, product_name, price, quantity, date):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.date = date

    def __str__(self):
        return f"{self.product_name} | {self.price} руб x {self.quantity} | {self.date}"


purchase_list = DoublyLinkedList()
purchase_list.append(Purchase("Телефон", 25000, 1, "2025-04-01"))
purchase_list.append(Purchase("Чехол", 500, 2, "2025-04-01"))

purchase_list.display_forward()