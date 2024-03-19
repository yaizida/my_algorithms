import random


def fill_array_and_linesearch():
    my_set = set()
    while len(my_set) != 25:
        my_set.add(random.randint(0, 1000))
    print(list(my_set))
    a = int(input())
    for i in list(my_set):
        if i == a:
            return 'Число найдено'


if __name__ == '__main__':
    print(fill_array_and_linesearch())
