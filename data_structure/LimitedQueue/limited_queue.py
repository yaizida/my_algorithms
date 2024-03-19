class LimitedQueue:

    def __init__(self, max_n) -> None:
        self.max_n = max_n
        # Максимальная длина списка известна, значит,
        # можно инцизизировать сразу все элементы списка,
        # что бы не тратить время на реализацию
        self.queue = [None] * self.max_n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        # Если очередь пустая вернется True
        return self.size == 0

    def push(self, value):
        if self.size < self.max_n:
            pass
