import math

if __name__ == '__main__':
    input_file = open("2020/13/input")
    raw_lines = input_file.readlines()

    raw_lines = '''939
1789,37,47,1889,x'''.split('\n')

    raw_lines = '''939
17,x,13,19'''.split('\n')

    arrival_time = int(raw_lines[0])
    busses = raw_lines[1].split(',')

    i_factor = 1
    i_bus = 1
    t = 0

    for bus in busses:
        if bus == 'x':
            i_bus += 1
            continue

        while (t + i_bus) % int(bus) > 0:
            t += i_factor

        i_factor *= int(bus)
        i_bus += 1
    print(t + 1)

    indexes = range(len(busses))
    busses_dict = dict(zip(busses, indexes))
    busses = [x for x in busses if x != 0]
    busses.sort(reverse=True)
    max_value = max(busses)
    step_size = max_value
    t = max_value - busses_dict[max_value] + (int(100000000000000 / max_value) * max_value)
    last_bus = 1
    while True:
        valid_time = True
        for i in range(len(busses)):
            bus = busses[i]
            min_later = t % bus
            if min_later == 0:
                x = 0
            else:
                x = bus - min_later
            if not (x == busses_dict[bus]):
                valid_time = False
                if i > last_bus:
                    step_size *= busses[i-1]
                    last_bus = i
                t += step_size
                break
        if valid_time:
            break
    print(t)

    busID = math.inf
    min_wait = math.inf
    for bus in busses:
        if bus != 'x':
            x = arrival_time % int(bus)
            min_wait_bus = int(bus) - x
            if min_wait_bus < min_wait:
                min_wait = min_wait_bus
                busID = int(bus)
    print(busID * min_wait)