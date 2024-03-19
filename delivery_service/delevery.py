import sys
from itertools import zip_longest


def delevery():
    search_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    need_num = int(sys.stdin.readline().rstrip())
    pairs = list(zip_longest(search_list[::2], search_list[1::2]))
    count = 0
    my_list = []
    for i in range(len(pairs)-1):
        if pairs[i][0] + pairs[i][1] < need_num or pairs[i][0] + pairs[i][1] == need_num:
            count += 1
            my_list.append(i)
    for i in my_list:
        del pairs[i]

    return count, my_list, pairs



print(delevery())


# Наивный метод поиска пары в списке с заданной суммой
def findPair(nums, target):
    # учитывает каждый элемент, кроме последнего
    for i in range(len(nums) - 1):
        # начинается с i-го элемента до последнего элемента
        for j in range(i + 1, len(nums)):
            # если искомая сумма найдена, вывести ее
            if nums[i] + nums[j] == target:
                print('Pair found', (i, j))
                return

    # В списке нет пары с указанной суммой
    print('Pair not found')


if __name__ == '__main__':

    nums = [8, 7, 2, 5, 3, 1]
    target = 10

    findPair(nums, target)