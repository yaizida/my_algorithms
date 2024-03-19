import sys


def is_correct_bracket_seq():
    bracket = sys.stdin.readline().rstrip()
    a = 0
    b = 0
    c = 0
    d = 0
    f = 0
    g = 0
    if len(bracket) == 0:
        return True
    elif bracket[1] == '[' and bracket[2] == ')':
        return False
    for i in bracket:
        if i == '(':
            a += 1
        elif i == '[':
            b += 1
        elif i == '{':
            c += 1
        elif i == ')':
            d += 1
        elif i == ']':
            f += 1
        elif i == '}':
            g += 1
    if bracket[0] == ')':
        return False
    elif a == d and b == f and c == g:
        return True
    else:
        return False


print(is_correct_bracket_seq())
