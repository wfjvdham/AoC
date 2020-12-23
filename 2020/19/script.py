import re

def construct_regex(current_rule_index, depth):
    current_rule = rules[current_rule_index]
    if current_rule_index == '8':
        return "(" + construct_regex('42', depth) + ')+'
    elif current_rule_index == '11':
        return "(" + construct_regex('42', depth) + '){' + str(depth) + '}(' + construct_regex('31', depth) + '){' + str(depth) + '}'
    elif current_rule.count('"') > 0:
        return current_rule[1]
    elif current_rule.count('|') > 0:
        parts = current_rule.split(' ')
        result = '('
        for part in parts:
            if part == '|':
                result += '|'
            else:
                result += construct_regex(part, depth)
        result += ')'
        return result
    else:
        result = ''
        parts = current_rule.split(' ')
        for part in parts:
            result += construct_regex(part, depth)
        return result

if __name__ == '__main__':
    input_file = open("2020/19/input")
    raw_lines = input_file.readlines()

    raw_lines = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''.split('\n')

    n_rules = 132
    rules = dict()

    for i in range(n_rules):
        line = raw_lines[i].strip()
        parts = line.split(':')
        rule_nr = parts[0]
        rule = parts[1].strip()
        rules[rule_nr] = rule

    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'

    regexs = []
    for i in range(1, 10):
        regexs.append('^' + construct_regex('0', depth=i) + '$')

    n_valid = 0
    for i in range(n_rules + 2, len(raw_lines)):
        message = raw_lines[i].strip()
        for regex in regexs:
            if re.match(regex, message):
                n_valid += 1
                break
    print(n_valid)
    # 351 too high
