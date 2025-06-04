import DoublyLinkedList

class CircularDoublyLinkedList(DoublyLinkedList.DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def append(self, data):
        super().append(data)
        self.tail.next = self.head
        self.head.prev = self.tail

def sort_circular_desc(cdl):
    if not cdl.head:
        return

    values = sorted(cdl.to_list(), reverse=True)
    cdl.head = cdl.tail = None
    for val in values:
        cdl.append(val)

    cdl.tail.next = cdl.head
    cdl.head.prev = cdl.tail


cdl = CircularDoublyLinkedList()
for i in [3, 1, 4, 1, 5, 9, 2]:
    cdl.append(i)

sort_circular_desc(cdl)
print("Отсортированный список по убыванию:", cdl.to_list())