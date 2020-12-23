import copy

def applyRules(grid, new_grid, x, y, z, w):
    n_active = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for n in range(-1, 2):
                    if not (i == 0 and j == 0 and k == 0 and n == 0):
                        if (grid[w + n][z + i][y + j][x + k]) == '#':
                            n_active += 1
    if not (grid[w][z][y][x] == '#' and (n_active == 2 or n_active == 3)):
        new_grid[w][z][y][x] = '.'
    if grid[w][z][y][x] != '#' and (n_active == 3):
        new_grid[w][z][y][x] = '#'
    return new_grid


if __name__ == '__main__':
    input_file = open("2020/17/input")
    raw_lines = input_file.readlines()

    raw_lines = '''.#.
..#
###'''.split('\n')

    raw_lines = list(map(list, raw_lines))

    grid = []
    #x horizontal (which col)
    #y vertical (which row)
    #zyx
    n_steps = 6
    n_rows = len(raw_lines)
    n_cols = len(raw_lines[0])
    for w in range(4 * n_steps + 1):
        x_field = []
        for z in range(4 * n_steps + 1):
            field = []
            for x in range(4 * n_steps + n_rows + 1):
                row = []
                for y in range(4 * n_steps + n_cols + 1):
                    if w == (2 * n_steps) and z == (2 * n_steps) and (2 * n_steps) <= y < (2 * n_steps + n_cols) and (2 * n_steps) <= x < (2 * n_steps + n_rows):
                        row.append(raw_lines[x - (2 * n_steps)][y - (2 * n_steps)])
                    else:
                        row.append(" ")
                field.append(row)
            x_field.append(field)
        grid.append(x_field)

    for i in range(n_steps):
        actual_step = i
        new_grid = copy.deepcopy(grid)
        for w in range(2 * n_steps - actual_step - 1, 2 * n_steps + actual_step + 2):
            for z in range(2 * n_steps - actual_step - 1, 2 * n_steps + actual_step + 2):
                for y in range(2 * n_steps - actual_step - 1, 2 * n_steps + actual_step + 1 + n_rows):
                    for x in range(2 * n_steps - actual_step - 1, 2 * n_steps + actual_step + 1 + n_cols):
                        new_grid = applyRules(grid, new_grid, x, y, z, w)
        grid = copy.deepcopy(new_grid)

    n_active = 0
    for w in range(4 * n_steps + 1):
        for z in range(4 * n_steps + 1):
            for x in range(4 * n_steps + n_rows):
                for y in range(4 * n_steps + n_cols):
                    if grid[w][z][y][x] == '#':
                        n_active += 1
    print(n_active)
