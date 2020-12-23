
def isValid(preamble, number):
    for i in range(len(preamble)):
        for j in range(len(preamble)):
            if preamble[i] != preamble[j]:
                if (int(preamble[i]) + int(preamble[j])) == number:
                    return True
    return False

if __name__ == '__main__':
    input_file = open("2020/09/input")
    raw_lines = input_file.readlines()

    raw_lines = '''35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576'''.split('\n')

    raw_lines = list(map(int, raw_lines))
    preamble_length = 25

    for i in range(preamble_length, len(raw_lines)):
        number = int(raw_lines[i])
        preamble = raw_lines[i - preamble_length:i]
        if not isValid(preamble, number):
            print(number)
            break

    answer_part_1 = 18272118

    start = 0
    end = start + 2

    while True:
        sum_value = sum(raw_lines[start:end])
        if sum_value == answer_part_1:
            print(min(raw_lines[start:end]) + max(raw_lines[start:end]))
            break
        else:
            if sum_value < answer_part_1:
                end += 1
            else:
                start += 1
                end = start + 2

    #2009521 too low