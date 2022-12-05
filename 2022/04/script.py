import os
import string

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = open("input")
    lines = input_file.readlines()

    n_full_contained = 0

    for line in lines:

        elfs = line.split(',')

        elf_1 = elfs[0].split("-")
        elf_2 = elfs[1].split("-")

        elf_1_start = int(elf_1[0])
        elf_1_end = int(elf_1[1])
        elf_2_start = int(elf_2[0])
        elf_2_end = int(elf_2[1])

        if (
            # (
            #     (elf_1_start <= elf_2_start) and
            #     (elf_1_end >= elf_2_end)
            # ) or (
            #     (elf_2_start <= elf_1_start) and
            #     (elf_2_end >= elf_1_end)
            # )
            (
                (elf_1_start <= elf_2_start) and
                (elf_2_start <= elf_1_end)
            ) or (
                (elf_2_start <= elf_1_start) and
                (elf_1_start <= elf_2_end)
            )
        ):
            n_full_contained += 1

    print(n_full_contained)
        
    # higher then 354
    # lower then 1000