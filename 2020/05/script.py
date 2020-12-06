if __name__ == '__main__':
    input_file = open("2020/05/input")
    lines = input_file.readlines()

    all_ids = set()
    for line in lines:
        line = line.strip()
        lowest_row = 0
        highest_row = 2**7 - 1
        for i in range(7):
            change = 2**(6-i)
            if line[i] == 'F':
                highest_row = highest_row - change
            else:
                lowest_row = lowest_row + change

        line = line[-3:]
        lowest_chair = 0
        highest_chair = 2**3 - 1
        for i in range(3):
            change = 2**(2-i)
            if line[i] == 'L':
                highest_chair = highest_chair - change
            else:
                lowest_chair = lowest_chair + change

        seat_id = (highest_row * 8) + lowest_chair
        all_ids.add(seat_id)

    for id_ in all_ids:
        if id_+1 not in all_ids:
            if id_-1 not in all_ids:
                print(id_)

    minid = min(all_ids)
    maxid = max(all_ids)
    possible_ids = set(range(minid, maxid+1))
    missing_ids = possible_ids - all_ids
    len(missing_ids)