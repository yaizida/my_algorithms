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
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item

        # просто крассиввый вывод - что бы понимать
        def __str__(self):
            return f'[{self.value}] -->\n{self.next_item}'


def solution(node, idx):
    # Если индекс равен нулю, то удаляем голову списка.
    if idx == 0:
        return node.next_item

    # Иначе ищем элемент с нужным индексом.
    current = node
    for i in range(idx - 1):
        current = current.next_item

    # Удаляем элемент из списка.
    current.next_item = current.next_item.next_item

    # Возвращаем голову обновленного списка.
    print(node)


def test():
    node4 = Node("Задача 5: Обследовать грунт в радиусе 3 м", None)
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", node4)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
