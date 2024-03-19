import string


def decode_string(code_string):
    stack, num, current_value = [], '', ''
    for item in code_string:
        if item in string.digits:
            num += item
        elif item == '[':
            stack.append((current_value, int(num)))
            current_value = ''
            num = ''
        elif item == ']':
            previous_value, count = stack.pop()
            current_value = previous_value + current_value * count
        else:
            current_value += item
    return current_value # Конечный результат


if __name__ == '__main__':
    code_string = input()
    print(decode_string(code_string))
