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
    # Напишите код функции здесь
    count = 0  # счетчик
    head = node  # Головной элемент
    temp = head  # временный узел - текущий головной элемент
    if idx == 0:
        # если это головной элемент то просто перевязываем
        # его на следующий
        head = temp.next_item
        print(head)  # после чего возырощаем голову
    while temp is not None:  # пока элемент temp не None
        # когда дошли до элемента который стоит ДО
        # элемента которого нужно удалить
        if (count+1) == idx:
            # То меняем его ссылку на след. объект через 1
            temp.next_item = temp.next_item.next_item
        count += 1  # Добовляем к счетчику + 1
        temp = temp.next_item  # И берем следующий элемент
    # Если мы дошли до конца списка
    if temp is None:
        # То возвращаем головной элемент
        # т.к. он имеет связь с ледующими
        # Если были зменения то он вернет с перевязыным узлом
        # Если не было индекса или он просто его не нашел
        # То вернет тот же связный список что и был
        print(head)


# Тестирующая функция для проверки решения.
# Не изменяйте её, она не требует вашего внимания.
def test():
    node4 = Node('Задача 5: ЗАЛУУУУУПА', None)
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", node4)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_node = solution(node0, 1)
    assert new_node is node0
    assert new_node.next_item is node2
    assert new_node.next_item.next_item is node3
    assert new_node.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
