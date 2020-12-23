

if __name__ == '__main__':
    input_file = open("2019/06/06_input")
    lines = input_file.readlines()
    line = lines[0]

    network = dict()
    network['B'] = 'COM'
    network['C'] = 'B'
    network['D'] = 'C'
    network['E'] = 'D'
    network['F'] = 'E'
    network['G'] = 'B'
    network['H'] = 'G'
    network['I'] = 'D'
    network['J'] = 'E'
    network['K'] = 'J'
    network['L'] = 'K'

    network = dict()
    for line in lines:
        relationship = line.strip().split(")")
        network[relationship[1]] = relationship[0]

    all_orbits = 0
    for planet in network:
        n_orbirts = 0
        current_planet = planet
        while True:
            if current_planet in network:
                current_planet = network[current_planet]
                n_orbirts += 1
            else:
                break
        all_orbits += n_orbirts

    print(all_orbits)

    you_route = []
    current_planet = 'YOU'
    while True:
        if current_planet in network:
            current_planet = network[current_planet]
            you_route.append(current_planet)
        else:
            break

    san_route = []
    current_planet = 'SAN'
    while True:
        if current_planet in network:
            current_planet = network[current_planet]
            san_route.append(current_planet)
        else:
            break

    crossing_point = list(set(you_route).intersection(set(san_route)))[-1]
    you_index = you_route.index(crossing_point)
    san_index = san_route.index(crossing_point)
    you_length = len(you_route)
    san_length = len(san_route)
    (you_length - you_index) + (san_length - san_index)
    #108 to low