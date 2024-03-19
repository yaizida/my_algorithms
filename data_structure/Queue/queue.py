
class Queue:
    def __init__(self) -> None:
        # Как и для стека используем для хранения список.
        self.__items = []

    def push(self, item):
        """Добавить элемент в очередь."""
        # В отличие от стека, здесь добовляем элемент не в конец списка
        # а в начало - на место с индексом 0.
        self.__items.insert(0, item)

    def pop(self):
        """Вернуть элемент из очереди."""
        return self.__items.pop()

    def peek(self):
        """Вернуть последний элемент, но не удалить его из очереди"""
        return self.__items[-1]

    def size(self):
        """Вернуть размер очереди."""
        return len(self.__items)


queue = Queue()
queue.push('task1')  # Добовляем элементы
queue.push('task2')
queue.push('task3')
queue.push('task4')
item = queue.pop()  # Вернули элемент из очереди
print(item)  # Вернется первый элемент
print(queue.size())
