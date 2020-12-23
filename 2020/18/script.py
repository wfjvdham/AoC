
def calcExpression(chars):
    if chars.count(' ') <= 1:
        return chars
    i = 0
    while i < len(chars):
        char = chars[i]
        if char in ('+', '*'):
            break
        i += 1

    if chars[i] == '+':
        result = int(chars[:i]) + int(calcExpression(chars[i + 1:]))
    else:
        result = int(chars[:i]) * int(calcExpression(chars[i + 1:]))
    return str(result)

def calcSequence(chars):
    if chars.count('(') > 0:
        i = 0
        while i < len(chars):
            char = chars[i]
            if char == '(':
                end = i + 1
                n_opening = 1
                n_closing = 0
                while n_opening != n_closing:
                    if chars[end] == ')':
                        n_closing += 1
                    elif chars[end] == '(':
                        n_opening += 1
                    end += 1
                chars_new = chars[:i] + calcSequence(chars[i+1:end-1]) + chars[end:]
                return calcSequence(chars_new)
            i += 1
    if chars.count('+') > 0:
        char_list = chars.split(' ')
        operator_index = char_list.index('+')
        result = int(char_list[operator_index - 1]) + int(char_list[operator_index + 1])
        result_list = char_list[0:operator_index - 1] + [str(result)] + char_list[operator_index + 2:]
        chars_new = ' '.join(result_list)
        return calcSequence(chars_new)
    else:
        return calcExpression(chars)

if __name__ == '__main__':
    input_file = open("2020/18/input")
    raw_lines = input_file.readlines()

    chars = '1 + 2 * 3 + 4 * 5 + 6'
    chars = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'

    calcSequence(chars)

    result = []
    for line in raw_lines:
        result.append(int(calcSequence(line.strip())))

    print(sum(result))
