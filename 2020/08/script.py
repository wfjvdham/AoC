import copy

def runProgram(lines):
    i = 0
    acc = 0
    visited_inst = set()
    while True:
        if i == len(lines):
            return acc
            break
        elif i in visited_inst:
            return None
            break
        else:
            visited_inst.add(i)
            instruction = lines[i].split(' ')
            operation = instruction[0]
            argument = instruction[1].strip()

            if operation == "acc":
                acc += int(argument)
                i += 1
            elif operation == 'jmp':
                i += int(argument)
            else:
                i += 1

if __name__ == '__main__':
    input_file = open("2020/08/input")
    raw_lines = input_file.readlines()

    for n in range(len(raw_lines)):
        instruction = raw_lines[n].split(' ')
        operation = instruction[0]
        argument = instruction[1].strip()

        lines = copy.deepcopy(raw_lines)

        if operation == 'acc':
            continue
        elif operation == 'jmp':
            operation = 'nop'
        elif operation == 'nop':
            operation = 'jmp'

        lines[n] = operation + ' ' + argument
        result = runProgram(lines)

        if result is not None:
            print(result)
            break
