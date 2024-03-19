import sys
from array import array

# Определяем объём памяти, который занимает список.
# Получим результат в байтах.
data_1 = [1, 2, 3]
print(sys.getsizeof(data_1))

# Определяем объём памяти, который занимает array.
data_2 = array('b', [1, 2, 3])
print(sys.getsizeof(data_2))