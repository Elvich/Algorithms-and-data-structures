import DoublyLinkedList

class CircularDoublyLinkedList(DoublyLinkedList.DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def append(self, data):
        super().append(data)
        self.tail.next = self.head
        self.head.prev = self.tail

def remove_duplicates_in_circular(cdl):
    if not cdl.head:
        return

    seen = set()
    current = cdl.head
    prev = None

    while True:
        if current.data in seen:
            if prev:
                prev.next = current.next
            if current.next:
                current.next.prev = prev
            if current == cdl.head:
                cdl.head = current.next
            if current == cdl.tail:
                cdl.tail = prev
        else:
            seen.add(current.data)
            prev = current
        current = current.next
        if current == cdl.head:
            break

    if cdl.head:
        cdl.tail.next = cdl.head
        cdl.head.prev = cdl.tail


cdl = CircularDoublyLinkedList()
for i in [1, 2, 3, 2, 4, 1, 5]:
    cdl.append(i)

remove_duplicates_in_circular(cdl)
print("После удаления дубликатов:", cdl.to_list())