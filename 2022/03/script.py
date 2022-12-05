import os
import string

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = open("input")
    lines = input_file.readlines()

    # prios = []

    # for line in lines:
    #     split_point = len(line)//2
    #     firstpart, secondpart = line[:split_point], line[split_point:]
        
    #     for char in firstpart:
    #         if secondpart.find(char) != -1:
    #             # print(char)
    #             prios.append(string.ascii_letters.find(char) + 1)
    #             break

    # print(sum(prios))

    prios = []

    for i in range(0, len(lines), 3):
        char = set(lines[i][:-1]). \
            intersection(set(lines[i + 1])). \
            intersection(set(lines[i + 2]))
        prios.append(string.ascii_letters.find(str(char)[2]) + 1)

    print(sum(prios))