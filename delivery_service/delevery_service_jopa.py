
def find_two_indexes():
    data = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    expected_result = int(sys.stdin.readline().rstrip())
    platforms = 0
    left_pointer = 0
    right_pointer = len(data) - 1
    my_list = []

    elements_in_slice = 2



    if len(set(data)) == 1 and len(data) % 2 == 0:

        window_sum = sum(data[0:elements_in_slice])

        for index in range(1, len(data) - elements_in_slice + 1):

            window_sum += data[index + elements_in_slice-1]

            window_sum -= data[index - 1]

            if window_sum == expected_result:

                my_list.append(window_sum)

            else:

                my_list.append(window_sum//2)

        if sum(my_list) != sum(data):

            platforms += len(data) - len(my_list)

        for i in range(len(my_list)):

            if my_list[i] == expected_result:

                platforms += 1

        return platforms



    while left_pointer < right_pointer:

        result = data[left_pointer] + data[right_pointer]

        if result == expected_result:

            platforms += 1

            my_list.append(data[left_pointer])


            my_list.append(data[right_pointer])

        if result > expected_result:

            right_pointer -= 1

        else:

            left_pointer += 1



    if len(data) == len(my_list):

        return platforms



    for i in my_list:

        data.remove(i)



    if len(data) > 1:

        for i in range(len(data)-1):

            result = data[i] + data[i+1]

            if result <= expected_result:

                platforms += 1

                data.remove(data[i])

                data.remove(data[i])

                if len(data) == 1:

                    break



    if len(data) > 1:

        platforms += len(data)



    if len(data) == 1:

        platforms += 1



    return platforms





print(find_two_indexes())

