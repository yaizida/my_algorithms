list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

list_superset(list_set_1, list_set_2)
# Набор [1, 3, 5, 7] - супермножество.

list_superset(list_set_2, list_set_3)
# Набор [5, 3, 7, 1] - супермножество.

list_superset(list_set_1, list_set_3)
# Наборы равны.
list_superset(list_set_2, list_set_4)
# Супермножество не обнаружено.