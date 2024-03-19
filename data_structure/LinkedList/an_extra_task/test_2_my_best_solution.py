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

        def __str__(self):
            return f'[{self.value}]->{self.next_item}'


def solution(node, idx):
    # Напишите код функции здесь.
    # ヽ(´▽`)/\
    node.headtask = None
    headtask = node.haedtask
    node.head = None
    head = node.head
    if headtask is not None:
        if headtask.value == idx:
            head = headtask.next_item
            headtask = None
            return
    while headtask is not None:
        if headtask.value == idx:
            break
        last_task = headtask
        headtask = headtask.next_item


node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
node0 = Node("Задача 1: Фотосъёмка 360°", node1)

# print(node0)
print(solution(node0, 1))
