import sys


def list_to_string(param):
    return ' '.join(map(str, param))


def sort_by_pattern(nums, patt, num_length, pattern_length):
    my_list = []
    for i in range(pattern_length):
        for j in range(num_length):
            if patt[i] == nums[j]:
                my_list.append(nums[j])
    l3 = [x for x in nums if x not in my_list]
    return my_list + sorted(l3)


if __name__ == '__main__':
    num_length = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    pattern_length = int(sys.stdin.readline().strip())
    patt = list(map(int, sys.stdin.readline().rstrip().split()))
    print(list_to_string(
        sort_by_pattern(
            nums,
            patt,
            num_length,
            pattern_length)))
