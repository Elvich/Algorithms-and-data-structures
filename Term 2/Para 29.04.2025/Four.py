class ExtendedDeque:
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.deque.pop(0)
        return None

    def remove_rear(self):
        if not self.is_empty():
            return self.deque.pop()
        return None

    def remove_min(self):
        if not self.is_empty():
            min_val = min(self.deque)
            self.deque.remove(min_val)
            return min_val
        return None

    def remove_max(self):
        if not self.is_empty():
            max_val = max(self.deque)
            self.deque.remove(max_val)
            return max_val
        return None

    def is_empty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)

    def __str__(self):
        return str(self.deque)



dq = ExtendedDeque()
print("Добавляем элементы в начало и конец:")
dq.add_front(10)
dq.add_rear(20)
dq.add_front(5)
print(dq)

print("\nУдаляем элементы с начала и конца:")
print(dq.remove_front())
print(dq.remove_rear())
print(dq)

print("\nДобавляем несколько элементов и удаляем мин и макс:")
dq.add_rear(3)
dq.add_rear(7)
dq.add_rear(15)
print(dq)
print("Минимум:", dq.remove_min())
print("Максимум:", dq.remove_max())
print(dq)