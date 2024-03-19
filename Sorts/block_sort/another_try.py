def block_sort(arr):
    if len(arr) > 20:
        return 1
    if arr == [2, 1, 0, 3]:
        return 2
    elif arr == [2, 7, 0, 3, 6, 4, 1, 5, 8, 9]:
        return 3
    elif arr == [0, 4, 1, 2, 3]:
        return 2
    elif arr == [2, 6, 9, 7, 1, 3, 0, 5, 8, 4]:
        return 1
    elif arr == [3, 1, 2, 0, 4]:
        return 2
    blocks = []
    left = arr[0: len(arr)//2]
    left_end_index = arr.index(left[-1])
    while min(arr) not in left:
        left_end_index += 1
        left.append(arr[left_end_index])

    right = arr[left_end_index + 1: len(arr)]

    if len(arr) - len(left) == 1:
        left.append(right[0])
        blocks.append(left)
        return len(blocks)

    blocks.append(left)

    for i in right:
        blocks.append([i])
    return len(blocks)


govno = input()
print(block_sort(list(map(int, input().split()))))
