import sys
from array import array


def main() -> int:
    data_input: str = sys.stdin.readline().rsplit()
    data_input.sort()
    limit: int = int(input())
    data: array = array('b', map(int, data_input))
    count: int = 0
    data_length: int = len(data)
    if data_length == 1 and data[0] <= limit:
        return data_length
    h = data_length
    for i in range((data_length+1)//2):
        for j in range(h-1, (h-1)//2, -1):
            if data[i] != limit:
                if data[i] + data[j] <= limit:
                    h -= 1
                    count += 1
                    break
                if data[j] <= limit:
                    count += 1
                    h -= 1
                    break
                if data[i] == limit:
                    count += 1
                    break
                count += 1
                h -= 1
            elif data[i] == limit:
                if data[j] == limit:
                    count += 2
                    h -= 1
                    break
                count += 2
                break
    return count

if __name__ == '__main__':
    print(main())