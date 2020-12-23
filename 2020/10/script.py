
def countArrangements(raw_lines, n_arrangements):
    n_arrangements += 1
    for i in range(len(raw_lines) - 1):
        start = raw_lines[i]
        end = start + 3
        n_options = sum((n <= end) & (n > start) for n in raw_lines)
        if n_options == 1:
            continue
        elif n_options == 2:
            n_arrangements = countArrangements(raw_lines[i + 2:], n_arrangements)
        elif n_options == 3:
            n_arrangements = countArrangements(raw_lines[i + 2:], n_arrangements)
            n_arrangements = countArrangements(raw_lines[i + 3:], n_arrangements)
    return n_arrangements

if __name__ == '__main__':
    input_file = open("2020/10/input")
    raw_lines = input_file.readlines()

    raw_lines = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.split('\n')

    raw_lines = '''16
10
15
5
1
11
7
19
6
12
4'''.split('\n')

    raw_lines = list(map(int, raw_lines))
    raw_lines.append(0)
    raw_lines.sort()
    raw_lines.append(raw_lines[len(raw_lines)-1]+3)

    start = 0
    n_options = 0
    total = 1
    pre_calc = dict()
    for i in range(len(raw_lines) - 1):
        if (raw_lines[i + 1] - 3) == raw_lines[i]:
            if n_options not in pre_calc:
                new_list = raw_lines[start:i + 1]
                pre_calc[n_options] = countArrangements(raw_lines[start:i+1], 0)
            if n_options != 0:
                total *= pre_calc[n_options]
            start = i
            n_options = 0
        else:
            n_options += 1
    print(total)