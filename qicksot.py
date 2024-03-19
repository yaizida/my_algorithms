import random


"""O(log n)"""


def find_element(sorted_numbers, element):
    left = 0
    right = len(sorted_numbers)
    while left < right:
        mid = (left + right) // 2
        if sorted_numbers[mid] == element:
            return sorted_numbers[:mid] + [sorted_numbers[mid]]
        if sorted_numbers[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return None


def fill_array():
    a = set()
    while len(a) < 25:
        a.add(random.randint(0, 100))
    a = list(a)
    a.sort()
    print(a)
    return a


print(find_element(fill_array(), int(input())))
