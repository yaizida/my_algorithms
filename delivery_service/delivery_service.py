#102182134
def platforms_count(data, expected_result):
    data.sort()
    platforms, left_pointer, right_pointer = 0, 0, len(data) - 1
    while left_pointer <= right_pointer:
        result = data[left_pointer] + data[right_pointer]
        if result <= expected_result:
            left_pointer += 1
        platforms += 1
        right_pointer -= 1

    return platforms


if __name__ == '__main__':
    data = [int(elem) for elem in input().split()]
    expected_result = int(input())
    print(platforms_count(data, expected_result))
