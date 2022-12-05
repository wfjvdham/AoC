import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = open("input")
    lines = input_file.readlines()

    elf_calories = []

    curr_elf = 0
    for line in lines:
        if line == "\n":
            elf_calories.append(curr_elf)
            curr_elf = 0
        else:
            cal = int(line)
            curr_elf += cal

    print(max(elf_calories))

    print(sum(sorted(elf_calories)[-3:]))