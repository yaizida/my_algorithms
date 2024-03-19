class Node:
    def __init__(self, data):
        self.data = data  # Данные сохроняем в качестве свойства
        self.next = None  # Cсылка на следующий элемент

    def __str__(self):  # При вызове print элемента - крассивый вывод
        return f'[{self.data}]->{self.next}'


class LinkedList:
    def __init__(self):
        self.head = None  # После вызова равен Node(1)

    def __str__(self):
        return str(self.head)

    def lenght(self):
        count = 0  # счетчик
        temp = self.head  # временный узел - текущий головной элемент
        while temp:  # пока элемент temp не None
            print(temp)
            count += 1  # Добовляем к счетчику + 1
            temp = temp.next  # И берем следующий элемент
        return count

    def delete_idx(self, idx):
        count = 0
        temp = self.head
        prev = None
        while count != idx:
            count += 1
            prev = temp
            temp = temp.next
        prev.next = temp.next
        return temp


if __name__ == '__main__':
    linked_list = LinkedList()  # Объект связанного списка
    temp = Node(1)  # Временный элемент с значением 1
    # Назначаем головным элементом тот самый временный элемент
    linked_list.head = temp
    for i in range(2, 5):  # Назначаем доп. узлы
        temp.next = Node(i)  # Назначем новый элемент с значение из for
        temp = temp.next

    # print(linked_list)
    # print(linked_list.lenght())
    print(linked_list.delete_idx(1))
