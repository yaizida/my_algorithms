# Импорт модуля os из стандартной библиотеки
# для взаимодействия с операционной системой.
import os
# Считывание переменной окружения REMOTE_JUDGE, чтобы определить,
# локально выполняется код или на удалённом сервере.
LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

# Если код выполняется на локальном компьютере, то...
if LOCAL:
    # Класс, описывающий элементы связного списка:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return f'[{self.value}]->{self.next}'


def find_element(head, value):
    current = head
    prev = None

    while current is not None:
        if current.value == value:
            return current
        prev = current
        current = current.next

    return None


def delete_element(head, value):
    element = find_element(head, value)

    if element is None:
        return head

    if element == head:
        head = head.next
    else:
        prev.next = element.next

    element.next = None
    return head


node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
node0 = Node("Задача 1: Фотосъёмка 360°", node1)

# print(node0)
# print(solution(node0, 1))
head = delete_element(node0, 2)

print(head)
