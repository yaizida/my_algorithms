def list_superset(list_set_1, list_set_2):
    # Не меняйте названия функции и параметров. Напишите решение здесь.

    sorted_list1 = sorted(list_set_1)
    sorted_list2 = sorted(list_set_2)

    if sorted_list1 == sorted_list2:
        return "Наборы равны."
    elif all(elem in sorted_list1 for elem in sorted_list2):
        return f"Набор {list_set_1} - супермножество."
    elif all(elem in sorted_list2 for elem in sorted_list1):
        return f"Набор {list_set_2} - супермножество."
    else:
        return "Супермножество не обнаружено."


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
