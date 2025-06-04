class FilteredNumberQueue:
    def __init__(self, even=True):
        self.queue = []
        self.filter_even = even

    def enqueue(self, number):
        if isinstance(number, int):
            if (number % 2 == 0 and self.filter_even) or (number % 2 != 0 and not self.filter_even):
                self.queue.append(number)

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



print("Очередь только четных чисел:")
even_q = FilteredNumberQueue(even=True)
even_q.enqueue(4)
even_q.enqueue(5)
even_q.enqueue(6)
print(even_q)

print("\nОчередь только нечетных чисел:")
odd_q = FilteredNumberQueue(even=False)
odd_q.enqueue(3)
odd_q.enqueue(4)
odd_q.enqueue(5)
print(odd_q)