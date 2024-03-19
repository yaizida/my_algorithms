def find_element_index_in_unordered_list(desired_element, unordered_list):
    """
    Находит индекс первого вхождения искомого элемента
    в неотсортированном списке.
    """
    # Применяем к списку функцию enumerate(), итерируемся
    # по полученному объекту enumerate и распаковываем его кортежи:
    # в переменную index сохраняем индекс элемента, в item - его значение.
    for index, item in enumerate(unordered_list):
        # Если значение текущего элемента равно искомому...
        if item == desired_element:
            # ...возвращаем его индекс:
            return index
    # Если цикл пройден, но нужное значение не найдено,
    # то возвращаем None.
    # Явно возвращать None не обязательно, эту строку можно вообще не писать:
    # если в функции нет оператора return, она возвращает None.
    return None


wins = [7495938, 1223125, 2128437, 4567890, 2128500, 2741001, 9314543, 4567687]
my_ticket = 2128506
result = find_element_index_in_unordered_list(my_ticket, wins)
if result is not None:
    print(f'Индекс элемента {my_ticket} в массиве: {result}')
else:
    print(f'Элемент {my_ticket} не найден в массиве.')



"""
def find_element_index_in_unordered_list(desired_element, unordered_list):
    'Находит индекс первого вхождения искомого элемента
    в неотсортированном списке.'
    # Формируем цикл с количеством шагов, равным длине списка.
    for index in range(len(unordered_list)):
        # Берём элемент из списка по его индексу.
        if unordered_list[index] == desired_element:
            return index
    return None
"""

