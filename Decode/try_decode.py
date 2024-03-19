from time import sleep


def decode(my_str):
    my_list = my_str.replace('[', '*').replace(']', '+')[::-1]
    # print(my_list)
    lit = 'abcdef'
    # symb = '*+'
    if my_list[0] == '+' or my_list[0] == '*':
        for i in range(len(my_list)-1):
            if my_list[i] in lit:
                my_list = my_list[(i):]
                break
    my_new_str = ''
    for i in my_list:
        pass
    return my_list.split('+')


first = '3[a]2[bc]'  # aaabcbc
second = '3[a2[c]]'  # accaccacc
third = '2[abc]3[cd]ef'  # abcabccdcdcdef
print(decode(first))
print(decode(second))
print(decode(third))
