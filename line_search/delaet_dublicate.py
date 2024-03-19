import sys

"""
def delete_dublecate(my_massive, len_list):
    my_new_massive = list()
    for i in my_massive:
        if i not in my_new_massive:
            my_new_massive.append(i)
    while len(my_new_massive) != int(len_list):
        my_new_massive.append('_')
    return my_new_massive


len_list = sys.stdin.readline()
my_massive = sys.stdin.readline()
my_massive = my_massive.split()

print(delete_dublecate(my_massive, len_list))"""


def delete_dublecate():
    len_list = int(sys.stdin.readline().rstrip())
    my_massive = sys.stdin.readline().rstrip().split()
    unique = set(my_massive)
    unique_list = sorted(map(int, list(unique))) # ['2','5','6'] -> map -> [2,5,6]
    my_string = ' '.join(map(str, unique_list))
    my_string += ' _' * (len_list - len(unique_list))
    print(my_string)


# delete_dublecate()


def cut_delete_dublicate():
    len_list = int(sys.stdin.readline().rstrip())
    my_massive = sys.stdin.readline().rstrip().split()
    my_string = ' '.join(map(str, sorted(map(int, list(set(my_massive))))))
    my_string += ' _' * (len_list - len(sorted(map(int, list(set(my_massive))))))
    print(my_string)


cut_delete_dublicate()
