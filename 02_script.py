import copy


def program_output(noun, verb, start_program):
    program = copy.deepcopy(start_program)
    print(str(noun) + ", " + str(verb))
    program[1] = noun
    program[2] = verb
    i = 0
    while True:
        if program[i] == 99:
            return program[0]
        if program[i] == 1:
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
            i += 4
        if program[i] == 2:
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
            i += 4


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = open("02_input")
    lines = input_file.readlines()
    start_program = list(map(int, lines[0].split(",")))

    for noun in range(99):
        for verb in range(99):
            output = program_output(noun, verb, start_program)
            if output == 19690720:
                print(100 * noun + verb)
                quit()
            else:
                continue
