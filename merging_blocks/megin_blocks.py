# import sys


def merge_sort(nums):
    blocks = []
    for i in range(len(nums)-1):
        if (nums[i+1]) - nums[i] == 1:
            print(nums[i], nums[i+1])


nums = [0, 1, 3, 2]
merge_sort(nums)
print(nums)

#if __name__ == '__main__':
    #num_length = int(sys.stdin.readline().strip())
    #nums = list(map(int, (sys.stdin.readline().strip().split())))
    #print(merge_sort(nums))
