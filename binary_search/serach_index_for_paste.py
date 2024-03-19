import sys


def main():
    search_list = list(map(int, sys.stdin.readline().rstrip().split()))
    need_num = int(sys.stdin.readline().rstrip())
    left = 0
    right = len(search_list)-1
    if need_num == search_list[0]:
        return 0
    while left <= right:
        mid = (left + right) // 2
        if search_list[mid] == need_num:
            return mid
        if search_list[mid] < need_num:
            left = mid + 1
        else:
            right = mid - 1
    if need_num > search_list[mid]:
        return mid+1
    else:
        return mid


print(main())
