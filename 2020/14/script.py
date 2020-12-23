import copy

if __name__ == '__main__':
    input_file = open("2020/14/input")
    raw_lines = input_file.readlines()

    raw_lines = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''.split('\n')

    memory = dict()

    for i in range(len(raw_lines)):
        line = raw_lines[i]
        if line.startswith('mask'):
            mask = line.split('=')[1].strip()
        else:
            values = line.split('[')[1].split(']')
            address = int(values[0])
            value = int(values[1].split('=')[1].strip())

            address_bit = [1 if x == '1' else 0 for x in '{:36b}'.format(address)]

            float_bits = []
            result = []
            for j in range(len(address_bit)):
                if mask[j] == '0':
                    result.append(address_bit[j])
                elif mask[j] == '1':
                    result.append(1)
                else:
                    result.append('X')
                    float_bits.append(j)

            if len(float_bits) == 0:
                result = int("".join(list(map(str, result))), 2)
                memory[result] = value
            else:
                for k in range(2**len(float_bits)):
                    bit_options = [1 if x == '1' else 0 for x in ('{:' + str(len(float_bits)) + 'b}').format(k)]

                    result_option = copy.deepcopy(result)
                    for n in range(len(float_bits)):
                        result_option[float_bits[n]] = bit_options[n]
                    result_int = int("".join(list(map(str, result_option))), 2)
                    memory[result_int] = value

    sum_of_all = 0
    for value in memory.values():
        sum_of_all += value
    print(sum_of_all)
    #1166446174853 too low