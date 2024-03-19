class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.nextcat = None

    def __str__(self):  # При вызове print элемента - крассивый вывод
        return f'[{self.cat}]->{self.nextcat}'


class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, cat):
        lastbox = self.head
        while (lastbox):
            if cat == lastbox.cat:
                return True
            else:
                lastbox = lastbox.nextcat
            return False

    def removeBox(self, rmcat):
        headcat = self.head

        if headcat is not None:
            if headcat.cat == rmcat:
                self.head = headcat.nextcat
                headcat = None
                return
        while headcat is not None:
            if headcat.cat == rmcat:
                break
        lastcat = headcat
        headcat = headcat.nextcat
        if headcat is None:
            return
        lastcat.nextcat = headcat.nextcat
        headcat = None


node3 = Box("Задача 4: Обследовать грунт в радиусе 3 м", None)
node2 = Box("Задача 3: Измерить температуру атмосферы", node3)
node1 = Box("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
node0 = Box("Задача 1: Фотосъёмка 360°", node1)

example = LinkedList(node0)
print(example.removeBox(1))
