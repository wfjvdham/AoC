
if __name__ == '__main__':
    input_file = open("2020/12/input")
    raw_lines = input_file.readlines()

    raw_lines = '''F10
N3
F7
R90
F11'''.split('\n')

    x_ship = 0
    y_ship = 0
    x_waypoint = 10
    y_waypoint = 1
    line = raw_lines[4]
    for line in raw_lines:
        line = line.strip()
        action = line[0]
        value = int(line[1:])

        if action == 'F':
            x_ship += value * x_waypoint
            y_ship += value * y_waypoint
        elif action == 'N':
            y_waypoint += value
        elif action == 'S':
            y_waypoint -= value
        elif action == 'E':
            x_waypoint += value
        elif action == 'W':
            x_waypoint -= value
        elif ((action == 'R') and (value == 90)) or ((action == 'L') and (value == 270)):
            tmp = y_waypoint
            y_waypoint = -x_waypoint
            x_waypoint = tmp
        elif ((action == 'R') and (value == 180)) or ((action == 'L') and (value == 180)):
            y_waypoint *= -1
            x_waypoint *= -1
        elif ((action == 'R') and (value == 270)) or ((action == 'L') and (value == 90)):
            tmp = y_waypoint
            y_waypoint = x_waypoint
            x_waypoint = -tmp

    print(abs(x_ship) + abs(y_ship))