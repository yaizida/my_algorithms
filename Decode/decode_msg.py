# 102312697

def decode_string(code_string):
    stack = []
    stack.append(["", 1])
    num = ""
    for i in code_string:
        if i.isdigit():
            num += i
        elif i == '[':
            stack.append(["", int(num)])
            num = ""
        elif i == ']':
            seq, count = stack.pop()
            stack[-1][0] += seq * count
        else:
            stack[-1][0] += i
    return stack[0][0]


if __name__ == '__main__':
    code_string = input()
    print(decode_string(code_string))
