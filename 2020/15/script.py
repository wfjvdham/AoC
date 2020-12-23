
if __name__ == '__main__':
    start_numbers = list(map(int, '0,3,6'.split(',')))
    start_numbers = list(map(int, '1,20,11,6,12,0'.split(',')))

    last_turn = dict()
    previous_turn = dict()
    last_number = 0

    for i in range(1, 30000000+1):
        if i <= len(start_numbers):
            last_number = start_numbers[i-1]
            last_turn[last_number] = i
        else:
            if last_number in previous_turn:
                last_number = last_turn[last_number] - previous_turn[last_number]
                if last_number in last_turn:
                    previous_turn[last_number] = last_turn[last_number]
                    last_turn[last_number] = i
                else:
                    last_turn[last_number] = i
            else:
                last_number = 0
                previous_turn[last_number] = last_turn[last_number]
                last_turn[last_number] = i
    print(last_number)


