import sys


def valid_mountain_array():
    search_list = list(map(int, sys.stdin.readline().rstrip().split()))
    if len(search_list) > 3:
        b = 0
        for i in range(len(search_list)-1):
            if search_list[i] == search_list[i+1]:
                return False
            elif search_list[i] > search_list[i+1] and b == 0:
                b += 1
            elif search_list[i] < search_list[i+1] and b != 0:
                b += 1
            elif search_list[0] > search_list[len(search_list)-1]:
                return False
        if b == 1:
            return True
        else:
            return False
    else:
        return False


print(valid_mountain_array())
