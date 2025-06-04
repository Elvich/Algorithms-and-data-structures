import DoublyLinkedList

def is_palindrome(dll):
    values = dll.to_list()
    return values == values[::-1]



palindrome_list = DoublyLinkedList.DoublyLinkedList()
palindrome_list.append(1)
palindrome_list.append(2)
palindrome_list.append(3)
palindrome_list.append(2)
palindrome_list.append(1)

print("Является ли список палиндромом:", is_palindrome(palindrome_list))  