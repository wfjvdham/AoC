import copy
import math

if __name__ == '__main__':
    input_file = open("2020/20/input")
    raw_lines = input_file.readlines()

    tiles = dict()

    id = 0
    tile = dict()
    line = raw_lines[1]
    i = 0
    while i < len(raw_lines):
        print(i)
        line = raw_lines[i].strip()
        if line == "":
            i += 1
        elif line.startswith("Tile"):
            id = int(line.split(" ")[1][:-1])
            i += 1
        else:
            tile[1] = copy.deepcopy(line)
            tile[2] = copy.deepcopy(raw_lines[i+9].strip())
            left = ''
            right = ''
            for j in range(i, i+10):
               line = raw_lines[j].strip()
               left += line[0]
               right += line[9]
            tile[3] = copy.deepcopy(right)
            tile[4] = copy.deepcopy(left)
            tiles[id] = copy.deepcopy(tile)
            i += 10

    example_tile = tiles[1913]

    #12 x 12
    grid = []
    for i in range(23):
        grid_line = []
        for j in range(23):
            if i == j == 11:
                grid_line.append(example_tile)
            else:
                grid_line.append('')
        grid.append(grid_line)

    # 2r
    #3 1
    # 4r

    # 1
    #4 2
    # 3

    corners = []

    for id in tiles:
        example_tile = tiles[id]
        n_borders = 0
        for id_compare in tiles:
            if id == id_compare:
                continue
            else:
                for border_nr in range(1, 5):
                    current_tile = tiles[id_compare]
                    for border_name in current_tile.keys():
                        border = current_tile[border_name]
                        match = False
                        if border == example_tile[border_nr]:
                            match = True
                            #print('normal')
                        elif border[::-1] == example_tile[border_nr]:
                            match = True
                            #print('flipped')
                        if match:
                            n_borders += 1
        if n_borders == 2:
            corners.append(id)

    math.prod(corners)