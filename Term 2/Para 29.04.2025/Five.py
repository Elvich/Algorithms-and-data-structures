class FilterableQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue_all_greater(self, value):
        self.queue = [x for x in self.queue if x <= value]

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


fq = FilterableQueue()
print("Добавляем элементы в очередь:")
fq.enqueue(10)
fq.enqueue(25)
fq.enqueue(5)
fq.enqueue(30)
print(fq)

print("\nУдаляем все элементы больше 20:")
fq.dequeue_all_greater(20)
print(fq)

print("\nУдаляем элемент из начала:")
fq.dequeue()
print(fq)