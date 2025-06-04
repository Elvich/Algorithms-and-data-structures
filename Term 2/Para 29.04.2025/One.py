class UniqueQueue:
    def __init__(self):
        self.queue = []
        self.elements = set()

    def enqueue(self, item):
        if item not in self.elements:
            self.queue.append(item)
            self.elements.add(item)

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            self.elements.remove(item)
            return item
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)



q = UniqueQueue()
print("Добавляем уникальные элементы:")
q.enqueue(10)
q.enqueue(20)
q.enqueue(10)
q.enqueue(30)
print(q)

print("\nУдаляем элементы из очереди:")
print(q.dequeue())
print(q)

print("\nПопытка добавить дубликат после удаления:")
q.enqueue(20)
print(q)