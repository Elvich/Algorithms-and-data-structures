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

class ExhibitRating:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __str__(self):
        return f"{self.name}: {self.rating}/10"


class MuseumVisitor:
    def __init__(self, first_name, last_name, visit_date, exhibits_rated):
        self.first_name = first_name
        self.last_name = last_name
        self.visit_date = visit_date
        self.exhibits_rated = exhibits_rated  # Список объектов ExhibitRating

    def __str__(self):
        rated = ", ".join([f"{er.name}({er.rating})" for er in self.exhibits_rated])
        return f"{self.first_name} {self.last_name}, {self.visit_date} | Оценки: {rated}"



visitor_list = DoublyLinkedList()
exhibits = [
    ExhibitRating("Динозавры", 9),
    ExhibitRating("Космос", 8)
]
visitor_list.append(MuseumVisitor("Иван", "Петров", "2025-04-01", exhibits))

visitor_list.display_forward()