# from tqdm import tqdm
# arr = [3, 1, 0, 2, 6, 5, 4, 7]
govno = input()
arr = list(map(int, (input().split())))
print(min(arr))
blocks = []
blocks.append([])
for i in range(len(arr)):
    blocks[0].append(arr[i])
    if min(arr) in blocks[0] and 1 in blocks[0]:
        if 2 in blocks[0]:
            break
last_item = 0
while arr[-1] != blocks[-1][-1]:
    start_range = arr.index(blocks[-1][-1]) + 1
    blocks.append([])
    last_item += 1
    for i in range(start_range, len(arr)):
        blocks[last_item].append(arr[i])
        if arr[-1] == blocks[-1][-1]:
            break
        if blocks[last_item][-1] - arr[i+1] == 1:
            continue
        elif blocks[last_item][-1] + (-1*arr[i+1]) == -1:
            continue
        else:
            break


print(blocks)
print(len(blocks))
