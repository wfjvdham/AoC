import copy

def doRound(grid):
    new_grid = copy.deepcopy(grid)
    c = len(grid[0])
    r = len(grid)
    for i in range(c):
        for j in range(r):
            n_occupied = 0
            #boven
            for n in range(j - 1, -1, -1):
                if grid[n][i] == '#':
                    n_occupied += 1
                    break
                elif grid[n][i] == 'L':
                    break
            #beneden
            for n in range(j + 1, r):
                if grid[n][i] == '#':
                    n_occupied += 1
                    break
                elif grid[n][i] == 'L':
                    break
            #rechts
            for n in range(i + 1, c):
                if grid[j][n] == '#':
                    n_occupied += 1
                    break
                elif grid[j][n] == 'L':
                    break
            #links
            for n in range(i - 1,  -1, -1):
                if grid[j][n] == '#':
                    n_occupied += 1
                    break
                elif grid[j][n] == 'L':
                    break
            #rechtsboven
            end = min(j, c - i - 1)
            for n in range(1, end + 1):
                if grid[j - n][i + n] == '#':
                    n_occupied += 1
                    break
                elif grid[j - n][i + n] == 'L':
                    break
            # rechtsonder
            end = min(r - j - 1, c - i - 1)
            for n in range(1, end + 1):
                if grid[j + n][i + n] == '#':
                    n_occupied += 1
                    break
                elif grid[j + n][i + n] == 'L':
                    break
            # linksonder
            end = min(r - j - 1, i)
            for n in range(1, end + 1):
                if grid[j + n][i - n] == '#':
                    n_occupied += 1
                    break
                elif grid[j + n][i - n] == 'L':
                    break
            # linksboven
            end = min(j, i)
            for n in range(1, end + 1):
                if grid[j - n][i - n] == '#':
                    n_occupied += 1
                    break
                elif grid[j - n][i - n] == 'L':
                    break

            if grid[j][i] == 'L' and n_occupied == 0:
                new_grid[j][i] = '#'
            elif grid[j][i] == '#' and n_occupied >= 5:
                new_grid[j][i] = 'L'
    return new_grid

if __name__ == '__main__':
    input_file = open("2020/11/input")
    raw_lines = input_file.readlines()
    raw_lines = list(map(str.strip, raw_lines))

    grid = raw_lines
    grid = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.split('\n')
    grid = list(map(list, grid))

    while True:
        new_grid = doRound(grid)
        new_grid_str = "".join(list(map("".join, new_grid)))
        grid_str = "".join(list(map("".join, grid)))
        if grid_str == new_grid_str:
            break
        grid = copy.deepcopy(new_grid)

    print(new_grid_str.count('#'))

