import re

def searchBagsThatCanContain(bags, rules):
    new_bags = []
    for bag in bags:
        for item in rules.items():
            if bag in item[1]:
                new_bags.append(item[0])
    return list(set(new_bags + bags))

def calcContainingBags(bag):
    if len(rules[bag]) == 0:
        return 0
    else:
        total = 0
        for contained in rules[bag]:
            code = contained.split(':')
            total += int(code[0])
            total += int(code[0]) * calcContainingBags(code[1])
        return total


if __name__ == '__main__':
    input_file = open("2020/07/input")
    lines = input_file.readlines()

    rules = dict()

    for line in lines:
        parts = re.compile("([0-9])").split(line)

        if len(parts) == 1:
            color = parts[0].split(' ')[0:2]
            rules[color[0] + ' ' + color[1]] = []
        else:
            colors = []
            for i in range(len(parts)):
                if i == 0:
                    part = parts[i]
                    color = part.strip().split(' ')[0:2]
                    colors.append(color[0] + ' ' + color[1])
                if (i % 2) == 0:
                    continue
                else:
                    combined = parts[i] + parts[i+1]
                    color = combined.split(' ')[0:3]
                    colors.append(
                        color[0] + ':' + color[1] + ' ' + color[2]
                    )

            rules[colors[0]] = colors[1:]

    calcContainingBags('shiny gold')

    new_length = 0
    while True:
        prev_length = len(bags)
        bags = searchBagsThatCanContain(bags, rules)
        new_length = len(bags)
        if prev_length == new_length:
            break

    print(new_length - 1)
