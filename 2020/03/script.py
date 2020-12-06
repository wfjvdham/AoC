from functools import reduce

if __name__ == '__main__':
    input_file = open("2020/03/input")
    lines = input_file.readlines()

    n_trees = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for slope in slopes:
        print(slope)

        n_tree = 0
        x = slope[0]
        y = slope[1]
        while y < len(lines):
            if x > 30:
                x = x - 31
            if lines[y][x] == '#':
                n_tree += 1
            x += slope[0]
            y += slope[1]

        n_trees.append(n_tree)

    print(reduce(lambda x, y: x*y, n_trees))