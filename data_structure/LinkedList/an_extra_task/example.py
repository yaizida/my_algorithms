class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Функция для удаления элемента из связного списка
def delete_node(head, target):
    if head is None:
        return head

    # Если элемент, который нужно удалить, находится в голове списка
    if head.data == target:
        head = head.next
        return head

    curr = head
    prev = None

    # Поиск элемента, который нужно удалить,
    # и получение ссылки на предыдущий элемент
    while curr is not None and curr.data != target:
        prev = curr
        curr = curr.next

    # Если элемент не найден
    if curr is None:
        return head

    # Обход удаляемого элемента
    prev.next = curr.next

    # Освобождение памяти удаляемого элемента
    curr = None

    return head


# Пример использования функции удаления
head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.next = node2
node2.next = node3

print("Исходный связный список: ", end="")
curr = head
while curr is not None:
    print(curr.data, end=" ")
    curr = curr.next
print()

target = 2
head = delete_node(head, target)

print("Связный список после удаления элемента {}: ".format(target), end="")
curr = head
while curr is not None:
    print(curr.data, end=" ")
    curr = curr.next
print()
