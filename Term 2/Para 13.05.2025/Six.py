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

def merge_sorted_lists(list1, list2, list3=None):
    merged = DoublyLinkedList()

    def add_all_from(source):
        current = source.head
        while current:
            merged.append(current.data)
            current = current.next

    add_all_from(list1)
    add_all_from(list2)
    if list3:
        add_all_from(list3)

    return merged


list1 = DoublyLinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = DoublyLinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

merged_list = merge_sorted_lists(list1, list2)
merged_list.display_forward()