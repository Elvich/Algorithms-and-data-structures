import DoublyLinkedList

def split_list(dll, pivot):
    less = DoublyLinkedList.DoublyLinkedList()
    greater_or_equal = DoublyLinkedList.DoublyLinkedList()

    current = dll.head
    while current:
        if current.data < pivot:
            less.append(current.data)
        else:
            greater_or_equal.append(current.data)
        current = current.next

    return less, greater_or_equal



num_list = DoublyLinkedList.DoublyLinkedList()
for i in [3, 7, 1, 8, 5, 2]:
    num_list.append(i)

less, greater = split_list(num_list, 5)
print("Меньше 5:", less.to_list())
print("Больше или равно 5:", greater.to_list())