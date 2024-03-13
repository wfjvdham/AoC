import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input") as f:
        lines = f.read().splitlines() 

        X = 1
        cycle_list = []
        cycle = 1
        crt = []
        crt_row = ""

        for line in lines:
            if (cycle == X) or (cycle == X + 1) or (cycle == X + 2):
                crt_row += "#"
            else:
                crt_row += "."
            cycle += 1
            if cycle % 41 == 0:
                crt.append(crt_row)
                crt_row = ""
                cycle -= 40
            if line == 'noop':
                
                cycle_list.append(X)
            else:
                commands = line.split()
                if (cycle == X) or (cycle == X + 1) or (cycle == X + 2):
                    crt_row += "#"
                else:
                    crt_row += "."
                cycle += 1
                if cycle % 41 == 0:
                    crt.append(crt_row)
                    crt_row = ""
                    cycle -= 40
                cycle_list.append(X)
                cycle_list.append(X)
                X += int(commands[1])

        # cycles_of_interest = [20, 60, 100, 140, 180, 220]
        # result = 0
        # for cycle_i in cycles_of_interest:
        #     result += cycle_list[cycle_i - 1] * cycle_i
        # print(result)
        for crt_row in crt:
            print(crt_row)
