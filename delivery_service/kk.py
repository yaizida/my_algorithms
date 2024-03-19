import sys


def find_two_indexes():
    data = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    expected_result = int(sys.stdin.readline().rstrip())
    platforms = 0
    left_pointer = 0
    right_pointer = len(data) - 1
    my_list = []
    while left_pointer < right_pointer:
        result = data[left_pointer] + data[right_pointer]
        if result == expected_result:
            platforms += 1
            my_list.append(data[left_pointer])
            my_list.append(data[right_pointer])
        if result > expected_result:
            right_pointer -= 1
        else:
            left_pointer += 1

    for i in my_list:
        data.remove(i)
    if len(data) > 1:
        for i in range(len(data)-1):
            result = data[i] + data[i+1]
            if result <= expected_result:
                platforms += 1
                data.remove(data[i])
                data.remove(data[i])
                if len(data) == 1:
                    platforms += 1
                    break
    if len(data) > 1:
        platforms += len(data)
    if len(data) == 1:
        platforms += 1
    return platforms


print(find_two_indexes())
