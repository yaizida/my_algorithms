import sys


def find_two_indexes(data, expected_result):
    # В начале работы
    # - левый указатель указывает на первый элемент списка (с индексом 0):
    left_pointer = 0
    # - правый указатель указывает на последний элемент;
    # индекс этого элемента на единицу меньше длины списка.
    right_pointer = len(data) - 1
    # Пока индекс левого указателя меньше индекса правого указателя.
    while left_pointer < right_pointer:
        # Считаем сумму двух элементов.
        result = data[left_pointer] + data[right_pointer]
        # Если она совпадает с искомой...
        if result == expected_result:
            # ...возвращаем ответ:
            return left_pointer, right_pointer
        # Если сумма больше искомой, то...
        if result > expected_result:
            # ...надо уменьшить сумму: уменьшаем значение правого указателя.
            right_pointer -= 1
        # Все остальные варианты относятся к случаям, когда сумма меньше искомой.
        else:
            # Сумму надо увеличить, для этого увеличиваем значение левого указателя.
            left_pointer += 1


if __name__ == '__main__':
    data = list(map(int, input().split()))
    expected_result = int(input())
    print(find_two_indexes(data, expected_result))
