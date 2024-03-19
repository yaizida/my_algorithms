import sys


def fuckin_min():
    search_list = list(map(int, sys.stdin.readline().rstrip().split()))
    result = []

    for i in range(len(search_list)):
        a = 0
        for j in range(len(search_list)):
            if search_list[i] > search_list[j]:
                a += 1
        result.append(a)
    return ' '.join(map(str, result))


print(fuckin_min())
