
def do_move(cups, current_cup, current_cup_index):
    pick_up = []
    for i in range(3):
        pick_up.append(cups[(current_cup_index + i + 1) % cups_len])
    new_cups = []
    for cup in cups:
        if cup not in pick_up:
            new_cups.append(cup)

    i = 1
    while True:
        destination = current_cup - i
        if destination == 0:
            destination = max_label
            i = i - max_label
        if destination in new_cups:
            break
        else:
            i += 1
    destination_index = new_cups.index(destination)
    for i in range(len(pick_up)):
        new_cups.insert(destination_index + i + 1, pick_up[i])
    new_current_cup_index = new_cups.index(current_cup)
    new_current_cup_index = (new_current_cup_index + 1) % cups_len
    return new_cups, new_cups[new_current_cup_index], new_current_cup_index

if __name__ == '__main__':
    cups = list(map(int, list('583976241')))
    #cups = list(map(int, list('389125467')))

    max_label = max(cups)
    cups = cups + list(range(max_label + 1, 1000000 + 1))

    max_label = max(cups)
    cups_len = len(cups)

    current_cup = cups[0]
    current_cup_index = cups.index(current_cup)

    for i in range(10000000):
        cups, current_cup, current_cup_index = do_move(cups, current_cup, current_cup_index)

    index_1 = cups.index(1)
    print(index_1)
    result = ''
    for i in range(8):
        index_i = (index_1 + i + 1) % cups_len
        result += str(cups[index_i])
    print(result)
    result = []
    for i in range(2):
        index_i = (index_1 + i + 1) % cups_len
        result.append(cups[index_i])
    print(result)