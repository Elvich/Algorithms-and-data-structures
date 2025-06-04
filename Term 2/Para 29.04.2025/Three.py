class LimitedQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def enqueue(self, item):
        if len(self.queue) < self.capacity:
            self.queue.append(item)
        else:
            self.queue.pop(0)
            self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def get_capacity(self):
        return self.capacity

    def __str__(self):
        return str(self.queue)


q = LimitedQueue(3)
print("Добавляем элементы в очередь ограниченной ёмкости:")
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)

print("\nДобавление нового элемента — очередь переполнена:")
q.enqueue(4)
print(q)

print("\nУдаление элемента из начала:")
q.dequeue()
print(q)