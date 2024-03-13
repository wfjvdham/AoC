import os
import json

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def compare(el1, el2):
    ordered = True
    for i in range(len(el1)):
        if el1[i] > el2[i]:
            ordered = False
    return ordered
        


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input") as f:
        lines = f.read().splitlines() 

        for i in range(0, len(lines), 3):
            element1 = json.loads(lines[i])
            element2 = json.loads(lines[i + 1])
            print(compare(element1, element2))
            break