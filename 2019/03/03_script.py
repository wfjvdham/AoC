import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = open("03_input")
    lines = input_file.readlines()
    path_coords = []
    for line in lines:
        coords = []
        path = line.split(",")
        current_location = (0, 0)
        for instruction in path:
            direction = instruction[0]
            distance = int(instruction[1:len(instruction)])
            if direction == "U":
                x = current_location[0]
                for y in range(current_location[1] + 1, current_location[1] + distance + 1):
                    coords.append((x, y))
            elif direction == "D":
                x = current_location[0]
                for y in range(current_location[1] - 1, current_location[1] - distance - 1, -1):
                    coords.append((x, y))
            elif direction == "R":
                y = current_location[1]
                for x in range(current_location[0] + 1, current_location[0] + distance + 1):
                    coords.append((x, y))
            else:
                y = current_location[1]
                for x in range(current_location[0] - 1, current_location[0] - distance - 1, -1):
                    coords.append((x, y))
            current_location = (x, y)
        path_coords.append(coords)
    crosses = set(path_coords[0]).intersection(set(path_coords[1]))
    min_distance = math.inf
    solution = None
    for cross in crosses:
        #distance = abs(cross[0]) + abs(cross[1])
        distance = path_coords[0].index(cross) + path_coords[1].index(cross) + 2
        if distance < min_distance:
            min_distance = distance
    print(min_distance)
