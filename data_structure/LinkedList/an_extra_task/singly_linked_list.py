class Node:
    def __init__(self, data):
        self.data = data  # Данные сохроняем в качестве свойства
        self.next = None  # Cсылка на следующий элемент

    def __str__(self):  # При вызове print элемента - крассивый вывод
        return f'[{self.data}]->'


class LinkedList:
    def __init__(self, head) -> None:
        self.head = head

    def append(self, data):
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(data=data)

    def output(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end='\n')
            tmp = tmp.next

    def search_idx(self, idx):
        count = 0  # счетчик
        tmp = self.head  # временный узел - текущий головной элемент
        while count != idx:  # пока элемент tmp не None
            print(tmp)
            count += 1  # Добовляем к счетчику + 1
            tmp = tmp.next  # И берем следующий элемент
        print(str(tmp))


data = Node("Задача 1: Фотосъёмка 360°")
ll = LinkedList(head=data)
ll.append('Задача 2: Пробурить скважину глубиной 0.5 м')
ll.append("Задача 3: Измерить температуру атмосферы")
ll.append("Задача 4: Обследовать грунт в радиусе 3 м")
ll.output()

ll.search_idx(1)
