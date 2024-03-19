def find_two_indexes(data, expected_sum):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == expected_sum:
                return (i, j)






if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))
