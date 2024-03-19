import sys


def valid_mountain_array():
    search_list = list(map(int, sys.stdin.readline().rstrip().split()))
    a = []
    if len(search_list) > 3:
        for i in range(len(search_list)):
            a.append(i)
        return a
    else:
        return False


print(valid_mountain_array())
