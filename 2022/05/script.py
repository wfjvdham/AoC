import os
import string

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = open("input")
    lines = input_file.readlines()

    mode = 'setup'

    stacks = []
    for m in range(0):
        stacks.append([])

    for j in range(1, 37, 4):
        stack = []
        for i in range(7, -1, -1):     
            crate = lines[i][j]
            if crate != ' ':
                stack.append(crate)
        stacks.append(stack)

    for i in range(10, len(lines)):
        line = lines[i]
        #print(line)
        commands = line.split(" ")

        ammount = int(commands[1])
        from_loc = int(commands[3])
        to_loc = int(commands[5])

        # for _ in range(ammount):
        #     crate = stacks[from_loc - 1].pop()
        #     stacks[to_loc - 1].append(crate)

        # print('from')
        # print(stacks[from_loc - 1])

        # print('to')
        # print(stacks[to_loc - 1])

        crates = stacks[from_loc - 1][-ammount:]

        # print('crates')
        # print(crates)

        stacks[from_loc - 1] = stacks[from_loc - 1][:-ammount]

        # print('from_after')
        # print(stacks[from_loc - 1])

        stacks[to_loc - 1] = stacks[to_loc - 1] + crates

        # print('to_after')
        # print(stacks[to_loc - 1])

    for stack in stacks:
        print(stack.pop())


