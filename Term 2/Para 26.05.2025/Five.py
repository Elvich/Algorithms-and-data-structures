import DoublyLinkedList

class CircularDoublyLinkedList(DoublyLinkedList.DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def append(self, data):
        super().append(data)
        self.tail.next = self.head
        self.head.prev = self.tail


def find_index_in_circular(cdl, target):
    if not cdl.head:
        return -1

    index = 0
    current = cdl.head
    visited = set()
    while current not in visited:
        if current.data == target:
            return index
        visited.add(current)
        current = current.next
        index += 1

    return -1



cdl = CircularDoublyLinkedList()
cdl.append(10)
cdl.append(20)
cdl.append(30)

print("Индекс элемента 20:", find_index_in_circular(cdl, 20))
print("Индекс элемента 40:", find_index_in_circular(cdl, 40))