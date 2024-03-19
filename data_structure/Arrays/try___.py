import sys


def valid_mountain_array():
    search_list = list(map(int, sys.stdin.readline().rstrip().split()))
    if len(search_list) > 3:
        flag = 0
        b = 0
        for i in range(len(search_list)):
            if search_list[i+1] > search_list[i]:
                b += 1
            elif search_list[i+1] == search_list[i]:
                return False
            elif search_list[i+1] < search_list[i]:
                flag += 1
            elif b == len(search_list):
                return False
            if flag > 0:
                if search_list[i+1] < search_list[i]:
                    b += 1
                elif search_list[i+1] >= search_list[i]:
                    return False
                elif b == len(search_list):
                    return True
            else:
                return b, flag
    else:
        return False


print(valid_mountain_array())
