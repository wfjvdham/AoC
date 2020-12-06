
def get_value(current_program, position, mode):
    if mode == "0":
        result = current_program[int(current_program[position])]
    else:
        result = current_program[position]
    return int(result)


def run_program(program, ID):
    i = 0
    while True:
        instruction = program[i]
        if len(instruction) > 2:
            opcode = instruction[-1]
            modes = "000" + instruction[0:-2]
        else:
            opcode = instruction
            modes = "000"
        if opcode == "99":
            exit()
        if opcode == "1":
            program[int(program[i + 3])] = str(get_value(program, i + 1, modes[-1]) + get_value(program, i + 2, modes[-2]))
            step_size = 4
        if opcode == "2":
            program[int(program[i + 3])] = str(get_value(program, i + 1, modes[-1]) * get_value(program, i + 2, modes[-2]))
            step_size = 4
        if opcode == "3":
            program[int(program[i + 1])] = ID
            step_size = 2
        if opcode == "4":
            print(get_value(program, i + 1, modes[-1]))
            step_size = 2
        if opcode == "5":
            if get_value(program, i + 1, modes[-1]) != 0:
                i = get_value(program, i + 2, modes[-2])
                step_size = 0
            else:
                step_size = 3
        if opcode == "6":
            if get_value(program, i + 1, modes[-1]) == 0:
                i = get_value(program, i + 2, modes[-2])
                step_size = 0
            else:
                step_size = 3
        if opcode == "7":
            program[int(program[i + 3])] = str(int(get_value(program, i + 1, modes[-1]) < get_value(program, i + 2, modes[-2])))
            step_size = 4
        if opcode == "8":
            program[int(program[i + 3])] = str(int(get_value(program, i + 1, modes[-1]) == get_value(program, i + 2, modes[-2])))
            step_size = 4
        i += step_size


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = open("05_input")
    lines = input_file.readlines()
    program = lines[0].split(",")

    ID = "5"
    run_program(program, ID)
