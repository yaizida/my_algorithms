import sys


def valid_mountain_array(search_list):
    if len(search_list) > 3:
        n = max(1, len(search_list)//2)
        m = list((search_list[i:i+n] for i in range(0, len(search_list), n)))
        if m[0][0] < m[0][1] and m[1][0] > m[1][1]:
            return True

        else:
            return False

    else:
        return False


print(valid_mountain_array([2, 1, 3, 5, 8]))
print(valid_mountain_array([3, 5, 5]))
print(valid_mountain_array([0, 3, 2, 1]))


def valid_mountain_array():
    search_list = list(map(int, sys.stdin.readline().rstrip().split()))
    if len(search_list) > 3:
        n = max(1, len(search_list)//2)
        m = list((search_list[i:i+n] for i in range(0, len(search_list), n)))
        if m[0][0] < m[0][1] and m[1][0] > m[1][1]:
            if sorted(m[0]) == sorted(m[1]):
                return False
            elif len(m[0]) != len(set(m[0])) or len(m[1]) != len(set(m[1])):
                return False
            else:
                return True
        else:
            return False

    else:
        return False


print(valid_mountain_array())
