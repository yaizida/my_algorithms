data = [2, 2, 2]
elements_in_slice = 2

# Сперва посчитаю сумму элементов в первом срезе,
# с индексами от 0 до elements_in_slice:
window_sum = sum(data[0:elements_in_slice])
# Сразу напечатаю:
print(window_sum)

# Теперь переберу массив data по индексам,
# от второго элемента в массиве до (len(data) - elements_in_slice) включительно:
for index in range(2, len(data) - elements_in_slice + 1):
    # Считаю сумму для текущего среза:
    # к сумме предыдущего среза прибавляю
    # значение последнего элемента текущего среза...
    window_sum += data[index + elements_in_slice-1]
    # ...и вычитаю значение первого элемента предыдущего среза:
    window_sum -= data[index - 1]
    print(window_sum)