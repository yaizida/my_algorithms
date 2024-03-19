
first = '3[a]2[bc]'  # aaabcbc
second = '3[a2[c]]'  # accaccacc
third = '2[abc]3[cd]ef'  # abcabccdcdcdef


my_first = 3*'a' + 2*'bc'
my_second = 3*('a'+2*'c')
my_third = 2*'abc'+3*'cd'+'ef'


print(my_first)
print(my_second)
print(my_third)
