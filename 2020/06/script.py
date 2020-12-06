if __name__ == '__main__':
    input_file = open("2020/06/input")
    lines = input_file.readlines()
    lines = ''.join(lines)

    groups = lines.split('\n\n')
    groups = groups[:-1]

    #group = groups[2]
    counts = []
    for group in groups:
        n_persons = len(group.split("\n"))
        group = group.replace('\n', '')
        count = {}
        for ch in group:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        result = {key: value for (key, value) in count.items() if value >= n_persons}
        counts.append(len(result))

    print(sum(counts)) #11186 too high