import time
from collections import deque

elements_count = 100000

start_time = time.time()

data1 = []

for data_index in range(elements_count):
    # Каждый раз вставляем элемент в начало списка.
    data1.insert(0, f'Элемент номер {data_index}')

print(time.time() - start_time)

start_time = time.time()

# Создаем дэк
data2 = deque()
for data_index in range(elements_count):
    # Добовляем элементы в начало очереди.
    data2.appendleft(f'Элемент номер {data_index}')
# Печатаем время для выполнения дэка.
print(time.time() - start_time)