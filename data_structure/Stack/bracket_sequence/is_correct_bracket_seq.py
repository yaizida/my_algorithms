import sys


def is_correct_bracket_seq():
    bracket = sys.stdin.readline().rstrip()
    s1 = bracket[: len(bracket) // 2]
    s2 = bracket[len(bracket) // 2:]
    if len(bracket) == 0:
        return True
    elif len(s1) != len(s2):
        return False
    elif s1[0] != ']' and s1[0] != '}' and s1[0] != ')':
        return True
    elif s2[len(s2)-1] != '[' and s2[len(s2)-1] != '{' and s2[len(s2)-1] != '(':
        return True
    else:
        return False


print(is_correct_bracket_seq())
