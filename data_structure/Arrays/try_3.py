import sys


def valid_mountain_array():
    search_list = list(map(int, sys.stdin.readline().rstrip().split()))
    if len(search_list) > 3:
        n = max(1, len(search_list)//2)
        m = list((search_list[i:i+n] for i in range(0, len(search_list), n)))
        b = 0
        if sorted(m[0]) == sorted(m[1]):
            return False
        for i in range(len(m[0])-1):
            if m[0][i] < m[0][i+1]:
                b += 1
        for i in range(len(m[1])-1):
            if m[1][i] > m[1][i+1]:
                b += 1
        if b > 1:
            return True
        else:
            return False
    else:
        return False


print(valid_mountain_array())