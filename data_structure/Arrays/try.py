import sys


def valid_mountain_array():
    search_list = list(map(int, sys.stdin.readline().rstrip().split()))
    if len(search_list) > 3:
        n = max(1, len(search_list)//2)
        m = list((search_list[i:i+n] for i in range(0, len(search_list), n)))
        if m[0][0] < m[0][1] and m[1][0] > m[1][1]:
            if sorted(m[0]) == sorted(m[1]):
                return False
            elif len(m[1]) != len(set(m[1])) or len(m[0]) != len(set(m[0])):
                return False
            else:
                return True
        else:
            b = 0
            for i in range(len(search_list)-1):
                if search_list[i] == search_list[i+1]:
                    return False
                elif search_list[i] > search_list[i+1] and b == 0:
                    b += 1
                elif search_list[i] < search_list[i+1] and b != 0:
                    b += 1
            if b == 1:
                return True
            else:
                return False
    else:
        return False


print(valid_mountain_array())
