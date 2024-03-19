import sys


def list_to_string(param):
    return ' '.join(map(str, param))


def sort_by_pattern(b, a):
    C = []
    for i in range(len(a)):
        if a[i] in b:
            C += [a[i]]
    if len(C) != len(b):
        for i in C:
            b.remove(i)
    for i in sorted(b):
        C.append(i)
    return C

if __name__ == '__main__':
    num_length = int(sys.stdin.readline().strip())
    nums = [int(elem) for elem in sys.stdin.readline().strip().split()]
    pattern_length = int(sys.stdin.readline().strip())
    patt = [int(elem) for elem in sys.stdin.readline().strip().split()]
    print(list_to_string(sort_by_pattern(nums, patt)))
